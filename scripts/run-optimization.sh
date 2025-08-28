#!/bin/bash

# 🚀 简化的图片优化运行脚本
# 
# 这个脚本提供了一个简单的接口来运行图片优化
# 适合日常使用，使用合理的默认设置

set -euo pipefail

# 获取脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# 颜色输出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🖼️  开始图片优化...${NC}"
echo -e "${YELLOW}项目目录: ${PROJECT_DIR}${NC}"

# 检查必要工具是否安装
check_tools() {
    local missing_tools=()
    
    for tool in webp optipng jpegoptim magick; do
        if ! command -v $tool &> /dev/null; then
            missing_tools+=($tool)
        fi
    done
    
    if [ ${#missing_tools[@]} -ne 0 ]; then
        echo -e "${YELLOW}⚠️  缺少以下工具: ${missing_tools[*]}${NC}"
        echo -e "${BLUE}正在安装缺少的工具...${NC}"
        
        # 运行安装脚本
        if [ -f "${SCRIPT_DIR}/install-deps.sh" ]; then
            "${SCRIPT_DIR}/install-deps.sh"
        else
            echo -e "${YELLOW}请手动安装: brew install webp optipng jpegoptim imagemagick${NC}"
            exit 1
        fi
    fi
}

# 检查工具
check_tools

# 运行优化脚本
echo -e "${GREEN}🚀 开始优化图片...${NC}"

# 优化不同目录的图片
directories=("static/images" "assets/img" "content")

for dir in "${directories[@]}"; do
    if [[ -d "${PROJECT_DIR}/${dir}" ]]; then
        echo -e "${BLUE}📁 优化目录: ${dir}${NC}"
        "${SCRIPT_DIR}/optimize-images-simple.sh" "${PROJECT_DIR}/${dir}"
    else
        echo -e "${YELLOW}⏭️  跳过不存在的目录: ${dir}${NC}"
    fi
done

echo -e "${GREEN}✅ 图片优化完成！${NC}"
echo ""
echo -e "${BLUE}📊 查看详细日志:${NC}"
echo -e "   tail -f ${PROJECT_DIR}/.image-cache/optimization.log"
echo ""
echo -e "${BLUE}💡 提示:${NC}"
echo -e "   • 首次运行可能需要较长时间"
echo -e "   • 后续运行会自动跳过已优化的文件"
echo -e "   • 建议在添加新图片后运行此脚本"
