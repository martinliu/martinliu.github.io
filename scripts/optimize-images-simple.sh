#!/bin/bash

# 🖼️ 简化版图片优化脚本 (macOS 兼容)
# 
# 功能：
# - 基本图片优化
# - WebP 转换
# - 增量处理
#
# 使用方法：
# ./scripts/optimize-images-simple.sh [目标目录]

set -euo pipefail

# 配置变量
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
TARGET_DIR="${1:-public}"
CACHE_DIR="${PROJECT_DIR}/.image-cache"
LOG_FILE="${CACHE_DIR}/optimization.log"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 初始化
echo -e "${BLUE}🚀 简化版图片优化脚本启动${NC}"
echo -e "${BLUE}📁 目标目录: ${TARGET_DIR}${NC}"

# 检查目标目录
if [[ ! -d "$TARGET_DIR" ]]; then
    echo -e "${RED}❌ 错误: 目标目录 '${TARGET_DIR}' 不存在${NC}"
    exit 1
fi

# 创建缓存目录
mkdir -p "$CACHE_DIR"

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
        stat -f%z "$file" 2>/dev/null || echo 0
    else
        echo 0
    fi
}

# 检查是否需要优化
need_optimization() {
    local source_file="$1"
    local target_file="$2"
    
    # 如果目标文件不存在，需要优化
    if [[ ! -f "$target_file" ]]; then
        return 0
    fi
    
    # 如果源文件比目标文件新，需要优化
    if [[ "$source_file" -nt "$target_file" ]]; then
        return 0
    fi
    
    # 不需要优化
    return 1
}

# 优化 JPEG 文件
optimize_jpeg() {
    local img="$1"
    local size=$(get_file_size "$img")
    
    echo -e "${YELLOW}📷 优化 JPEG: $(basename "$img")${NC}"
    
    # 根据文件大小设置质量
    local quality=85
    if [[ $size -gt 1048576 ]]; then  # > 1MB
        quality=75
    elif [[ $size -lt 51200 ]]; then  # < 50KB
        quality=90
    fi
    
    jpegoptim --max=$quality --strip-all --preserve "$img" || true
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
    
    if need_optimization "$img" "$webp_name"; then
        echo -e "${YELLOW}🔄 转换 WebP: $(basename "$img")${NC}"
        local size=$(get_file_size "$img")
        local quality=80
        
        # 根据文件大小调整质量
        if [[ $size -gt 1048576 ]]; then  # > 1MB
            quality=75
        elif [[ $size -lt 51200 ]]; then  # < 50KB
            quality=85
        fi
        
        cwebp -q $quality "$img" -o "$webp_name" 2>/dev/null || true
    fi
}

# 处理单个图片
process_image() {
    local img="$1"
    local ext="${img##*.}"
    local ext_lower=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
    
    case "$ext_lower" in
        jpg|jpeg)
            convert_to_webp "$img"
            optimize_jpeg "$img"
            ;;
        png)
            convert_to_webp "$img"
            optimize_png "$img"
            ;;
        *)
            echo -e "${YELLOW}⏭️  跳过不支持的格式: $(basename "$img")${NC}"
            ;;
    esac
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
    
    # 显示进度
    if [[ $((processed % 10)) -eq 0 ]] || [[ $processed -eq $total_files ]]; then
        echo -e "${BLUE}📈 进度: $processed/$total_files${NC}"
    fi
done

# 统计结果
echo -e "${GREEN}🎉 图片优化完成!${NC}"
echo -e "${BLUE}📊 处理统计:${NC}"
echo -e "   • 总文件数: $total_files"

# 统计 WebP 文件
webp_count=$(find "$TARGET_DIR" -name "*.webp" 2>/dev/null | wc -l | tr -d ' ')
echo -e "   • WebP 文件: $webp_count"

echo -e "${BLUE}💾 日志文件: $LOG_FILE${NC}"
echo "$(date '+%Y-%m-%d %H:%M:%S') - 优化完成: $total_files 文件" >> "$LOG_FILE"

echo -e "${GREEN}✅ 优化完成!${NC}"
