#!/bin/bash

# 🖼️ 简化版图片优化脚本 (macOS/Linux)
#
# 功能：
# - JPG/JPEG/PNG 基本优化
# - WebP 转换
# - 持久化增量处理（记忆功能）
#
# 使用方法：
# ./scripts/optimize-images-simple.sh [目标目录]

set -euo pipefail

# 配置变量
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
TARGET_DIR="${1:-public}"
CACHE_DIR="${PROJECT_DIR}/.image-cache"
STATE_DIR="${CACHE_DIR}/state"
LOG_FILE="${CACHE_DIR}/optimization.log"
CACHE_FORMAT_VERSION="v1"
SHOW_SKIPPED="${SHOW_SKIPPED:-1}"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

optimized_count=0
skipped_count=0

# 初始化
echo -e "${BLUE}🚀 图片优化脚本启动${NC}"
echo -e "${BLUE}📁 目标目录: ${TARGET_DIR}${NC}"

# 检查目标目录
if [[ ! -d "$TARGET_DIR" ]]; then
    echo -e "${RED}❌ 错误: 目标目录 '${TARGET_DIR}' 不存在${NC}"
    exit 1
fi

# 创建缓存目录
mkdir -p "$CACHE_DIR" "$STATE_DIR"

# 检查依赖工具
echo -e "${BLUE}🔧 检查依赖工具...${NC}"
missing_tools=()

if ! command -v cwebp &> /dev/null; then
    missing_tools+=("webp")
fi

if ! command -v optipng &> /dev/null; then
    missing_tools+=("optipng")
fi

if ! command -v jpegoptim &> /dev/null; then
    missing_tools+=("jpegoptim")
fi

if [[ ${#missing_tools[@]} -gt 0 ]]; then
    echo -e "${RED}❌ 缺少以下工具:${NC}"
    for tool in "${missing_tools[@]}"; do
        echo -e "${YELLOW}   - $tool${NC}"
    done
    echo -e "${BLUE}💡 请运行: brew install ${missing_tools[*]}${NC}"
    exit 1
fi

echo -e "${GREEN}✅ 所有依赖工具已安装${NC}"

# 获取文件大小
get_file_size() {
    local file="$1"
    if [[ -f "$file" ]]; then
        stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null || echo 0
    else
        echo 0
    fi
}

# 统一哈希命令（macOS: shasum, Linux: sha256sum）
hash_file() {
    local file="$1"
    if command -v shasum &> /dev/null; then
        shasum -a 256 "$file" | awk '{print $1}'
    else
        sha256sum "$file" | awk '{print $1}'
    fi
}

# 将路径转换为项目相对路径，保证缓存可迁移
relative_to_project() {
    local p="$1"
    case "$p" in
        "$PROJECT_DIR"/*)
            echo "${p#"$PROJECT_DIR"/}"
            ;;
        *)
            echo "$p"
            ;;
    esac
}

# 状态文件路径（按图片路径哈希）
state_file_for() {
    local img="$1"
    local rel
    local key

    rel="$(relative_to_project "$img")"
    if command -v shasum &> /dev/null; then
        key="$(printf '%s' "$rel" | shasum -a 256 | awk '{print $1}')"
    else
        key="$(printf '%s' "$rel" | sha256sum | awk '{print $1}')"
    fi

    echo "$STATE_DIR/${key}.state"
}

# 判断是否命中缓存（记忆）
is_cache_hit() {
    local img="$1"
    local state_file="$2"
    local rel
    local src_sha
    local webp_path
    local webp_flag="0"
    local cache_version cache_rel cache_sha cache_webp

    if [[ ! -f "$state_file" ]]; then
        return 1
    fi

    rel="$(relative_to_project "$img")"
    src_sha="$(hash_file "$img")"
    webp_path="${img%.*}.webp"

    if [[ -f "$webp_path" ]]; then
        webp_flag="1"
    fi

    IFS='|' read -r cache_version cache_rel cache_sha cache_webp < "$state_file" || return 1

    if [[ "$cache_version" != "$CACHE_FORMAT_VERSION" ]]; then
        return 1
    fi

    if [[ "$cache_rel" == "$rel" && "$cache_sha" == "$src_sha" && "$cache_webp" == "$webp_flag" && "$webp_flag" == "1" ]]; then
        return 0
    fi

    return 1
}

# 更新缓存状态
update_cache_state() {
    local img="$1"
    local state_file="$2"
    local rel
    local src_sha
    local webp_path
    local webp_flag="0"

    rel="$(relative_to_project "$img")"
    src_sha="$(hash_file "$img")"
    webp_path="${img%.*}.webp"

    if [[ -f "$webp_path" ]]; then
        webp_flag="1"
    fi

    printf '%s|%s|%s|%s\n' "$CACHE_FORMAT_VERSION" "$rel" "$src_sha" "$webp_flag" > "$state_file"
}

# 检查是否需要重建 WebP
need_optimization() {
    local source_file="$1"
    local target_file="$2"

    if [[ ! -f "$target_file" ]]; then
        return 0
    fi

    if [[ "$source_file" -nt "$target_file" ]]; then
        return 0
    fi

    return 1
}

# 优化 JPEG 文件
optimize_jpeg() {
    local img="$1"
    local size
    local quality=85

    size="$(get_file_size "$img")"
    echo -e "${YELLOW}📷 优化 JPEG: $(basename "$img")${NC}"

    if [[ $size -gt 1048576 ]]; then
        quality=75
    elif [[ $size -lt 51200 ]]; then
        quality=90
    fi

    jpegoptim --max="$quality" --strip-all --preserve "$img" || true
}

# 优化 PNG 文件
optimize_png() {
    local img="$1"
    echo -e "${YELLOW}🖼️  优化 PNG: $(basename "$img")${NC}"
    optipng -quiet -preserve "$img" || true
}

# 转换为 WebP
convert_to_webp() {
    local img="$1"
    local webp_name="${img%.*}.webp"
    local size
    local quality=80

    if need_optimization "$img" "$webp_name"; then
        echo -e "${YELLOW}🔄 转换 WebP: $(basename "$img")${NC}"
        size="$(get_file_size "$img")"

        if [[ $size -gt 1048576 ]]; then
            quality=75
        elif [[ $size -lt 51200 ]]; then
            quality=85
        fi

        cwebp -q "$quality" "$img" -o "$webp_name" 2>/dev/null || true
    fi
}

# 处理单个图片
process_image() {
    local img="$1"
    local ext="${img##*.}"
    local ext_lower
    local state_file

    ext_lower="$(echo "$ext" | tr '[:upper:]' '[:lower:]')"
    state_file="$(state_file_for "$img")"

    case "$ext_lower" in
        jpg|jpeg|png)
            if is_cache_hit "$img" "$state_file"; then
                skipped_count=$((skipped_count + 1))
                if [[ "$SHOW_SKIPPED" == "1" ]]; then
                    echo -e "${BLUE}⏭️  跳过已处理: $(basename "$img")${NC}"
                fi
                return
            fi
            ;;
        *)
            echo -e "${YELLOW}⏭️  跳过不支持的格式: $(basename "$img")${NC}"
            return
            ;;
    esac

    case "$ext_lower" in
        jpg|jpeg)
            # 先优化原图，再生成 WebP，确保 WebP 反映最新原图内容
            optimize_jpeg "$img"
            convert_to_webp "$img"
            ;;
        png)
            optimize_png "$img"
            convert_to_webp "$img"
            ;;
    esac

    update_cache_state "$img" "$state_file"
    optimized_count=$((optimized_count + 1))
}

# 主处理流程
echo -e "${BLUE}🔍 扫描图片文件...${NC}"

# 查找图片文件
image_files=()
while IFS= read -r -d '' file; do
    image_files+=("$file")
done < <(find "$TARGET_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -print0)

total_files=${#image_files[@]}
echo -e "${BLUE}📊 发现 $total_files 张图片${NC}"

if [[ $total_files -eq 0 ]]; then
    echo -e "${YELLOW}⚠️  没有找到需要优化的图片${NC}"
    exit 0
fi

# 处理图片
processed=0
echo -e "${GREEN}🚀 开始处理图片...${NC}"

for img in "${image_files[@]}"; do
    process_image "$img"
    processed=$((processed + 1))

    if [[ $((processed % 10)) -eq 0 ]] || [[ $processed -eq $total_files ]]; then
        echo -e "${BLUE}📈 进度: $processed/$total_files${NC}"
    fi
done

# 统计结果
echo -e "${GREEN}🎉 图片优化完成!${NC}"
echo -e "${BLUE}📊 处理统计:${NC}"
echo -e "   • 总文件数: $total_files"
echo -e "   • 本次处理: $optimized_count"
echo -e "   • 命中缓存跳过: $skipped_count"

# 统计 WebP 文件
webp_count=$(find "$TARGET_DIR" -name "*.webp" 2>/dev/null | wc -l | tr -d ' ')
echo -e "   • WebP 文件: $webp_count"

echo -e "${BLUE}💾 日志文件: $LOG_FILE${NC}"
echo "$(date '+%Y-%m-%d %H:%M:%S') - 优化完成: total=$total_files processed=$optimized_count skipped=$skipped_count" >> "$LOG_FILE"

echo -e "${GREEN}✅ 优化完成!${NC}"
