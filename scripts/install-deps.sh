#!/bin/bash

# 📦 macOS 图片优化工具安装脚本
# 
# 这个脚本会安装所有必要的图片优化工具
# 适用于 macOS 系统，使用 Homebrew 包管理器

set -euo pipefail

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}📦 开始安装图片优化工具...${NC}"

# 检查是否安装了 Homebrew
check_homebrew() {
    if ! command -v brew &> /dev/null; then
        echo -e "${RED}❌ 未找到 Homebrew${NC}"
        echo -e "${YELLOW}请先安装 Homebrew: https://brew.sh/${NC}"
        echo -e "${BLUE}安装命令:${NC}"
        echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        exit 1
    else
        echo -e "${GREEN}✅ 找到 Homebrew${NC}"
    fi
}

# 安装工具函数
install_tool() {
    local tool=$1
    local package=${2:-$tool}
    
    if command -v $tool &> /dev/null; then
        echo -e "${GREEN}✅ $tool 已安装${NC}"
        return 0
    fi
    
    echo -e "${YELLOW}📥 正在安装 $package...${NC}"
    if brew install $package; then
        echo -e "${GREEN}✅ $package 安装成功${NC}"
    else
        echo -e "${RED}❌ $package 安装失败${NC}"
        return 1
    fi
}

# 更新 Homebrew
update_homebrew() {
    echo -e "${BLUE}🔄 更新 Homebrew...${NC}"
    brew update
}

# 主安装流程
main() {
    echo -e "${BLUE}🚀 开始安装流程...${NC}"
    echo ""
    
    # 检查 Homebrew
    check_homebrew
    
    # 更新 Homebrew
    update_homebrew
    
    echo ""
    echo -e "${BLUE}📋 安装清单:${NC}"
    echo "  • webp (WebP 格式处理)"
    echo "  • optipng (PNG 优化)"
    echo "  • jpegoptim (JPEG 优化)"
    echo "  • imagemagick (通用图片处理)"
    echo "  • gnu-parallel (并行处理，可选)"
    echo ""
    
    # 安装基本工具
    install_tool cwebp webp
    install_tool optipng
    install_tool jpegoptim
    install_tool magick imagemagick
    
    # 安装可选工具（用于并行处理）
    echo ""
    echo -e "${BLUE}🔧 安装可选工具...${NC}"
    install_tool parallel gnu-parallel || echo -e "${YELLOW}⚠️  gnu-parallel 安装失败，将使用系统默认的并行处理${NC}"
    
    echo ""
    echo -e "${GREEN}🎉 所有工具安装完成！${NC}"
    echo ""
    echo -e "${BLUE}📋 安装状态:${NC}"
    
    # 验证安装
    tools=("cwebp:WebP 编码器" "dwebp:WebP 解码器" "optipng:PNG 优化器" "jpegoptim:JPEG 优化器" "magick:ImageMagick")
    
    for tool_info in "${tools[@]}"; do
        IFS=':' read -r tool desc <<< "$tool_info"
        if command -v $tool &> /dev/null; then
            version=$(eval "${tool}" --version 2>/dev/null | head -1 || echo "已安装")
            echo -e "  ${GREEN}✅${NC} $desc: $version"
        else
            echo -e "  ${RED}❌${NC} $desc: 未安装"
        fi
    done
    
    echo ""
    echo -e "${BLUE}🚀 现在可以运行图片优化了:${NC}"
    echo "  ./scripts/run-optimization.sh"
    echo ""
    echo -e "${BLUE}💡 高级用法:${NC}"
    echo "  ./scripts/optimize-images.sh -h"
}

# 运行主函数
main "$@"
