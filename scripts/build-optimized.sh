#!/bin/bash
# Hugo 构建优化脚本

set -e

echo "🚀 开始构建优化流程..."

# 1. 清理旧的构建文件
echo "🧹 清理旧文件..."
rm -rf public
rm -rf resources/_gen

# 2. 安装依赖工具（如果没有安装）
if ! command -v hugo &> /dev/null; then
    echo "❌ Hugo 未安装"
    exit 1
fi

# 3. 设置环境变量
export HUGO_ENV=production
export NODE_ENV=production

# 4. 构建网站
echo "🔨 构建网站..."
hugo --minify --enableGitInfo --cleanDestinationDir

# 5. 优化图片（如果工具可用）
if command -v find &> /dev/null; then
    echo "🖼️  检查图片优化..."
    
    # 转换为 WebP（如果 cwebp 可用）
    if command -v cwebp &> /dev/null; then
        echo "转换图片为 WebP 格式..."
        find public -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" | while read img; do
            webp_name="${img%.*}.webp"
            if [ ! -f "$webp_name" ]; then
                cwebp -q 85 "$img" -o "$webp_name"
                echo "转换: $img -> $webp_name"
            fi
        done
    fi
    
    # 压缩 PNG（如果 optipng 可用）
    if command -v optipng &> /dev/null; then
        echo "压缩 PNG 图片..."
        find public -name "*.png" -exec optipng -o2 {} \;
    fi
    
    # 压缩 JPEG（如果 jpegoptim 可用）
    if command -v jpegoptim &> /dev/null; then
        echo "压缩 JPEG 图片..."
        find public -name "*.jpg" -o -name "*.jpeg" -exec jpegoptim --size=85% {} \;
    fi
fi

# 6. 生成 Gzip 文件
if command -v gzip &> /dev/null; then
    echo "🗜️  生成 Gzip 压缩文件..."
    find public -type f \( -name "*.html" -o -name "*.css" -o -name "*.js" -o -name "*.xml" -o -name "*.json" \) | while read file; do
        gzip -9 -c "$file" > "$file.gz"
        echo "压缩: $file"
    done
fi

# 7. 生成 Brotli 文件（如果可用）
if command -v brotli &> /dev/null; then
    echo "🗜️  生成 Brotli 压缩文件..."
    find public -type f \( -name "*.html" -o -name "*.css" -o -name "*.js" -o -name "*.xml" -o -name "*.json" \) | while read file; do
        brotli -9 -c "$file" > "$file.br"
        echo "Brotli 压缩: $file"
    done
fi

#!/bin/bash
# Hugo 本地构建优化脚本

set -e

# 检查是否为本地开发环境
LOCAL_DEV=${LOCAL_DEV:-true}
SKIP_OPTIMIZATION=${SKIP_OPTIMIZATION:-false}

echo "🚀 开始构建优化流程..."
echo "环境: $([ "$LOCAL_DEV" = "true" ] && echo "本地开发" || echo "生产构建")"

# 1. 清理旧的构建文件
echo "🧹 清理旧文件..."
rm -rf public
rm -rf resources/_gen

# 2. 检查 Hugo 安装
if ! command -v hugo &> /dev/null; then
    echo "❌ Hugo 未安装"
    echo "💡 请运行: brew install hugo"
    exit 1
fi

# 3. 设置环境变量
if [ "$LOCAL_DEV" = "true" ]; then
    export HUGO_ENV=development
    export NODE_ENV=development
    echo "🔧 本地开发模式 - 跳过部分优化"
else
    export HUGO_ENV=production
    export NODE_ENV=production
    echo "🚀 生产构建模式 - 启用全部优化"
fi

# 4. 构建网站
echo "🔨 构建网站..."
if [ "$LOCAL_DEV" = "true" ]; then
    # 本地开发：快速构建，启用草稿
    hugo --buildDrafts --buildFuture --enableGitInfo
else
    # 生产构建：完整优化
    hugo --minify --gc --enableGitInfo --cleanDestinationDir
fi

# 5. 图片优化（仅在生产模式或明确要求时）
if [ "$LOCAL_DEV" != "true" ] || [ "$SKIP_OPTIMIZATION" != "true" ]; then
    echo "🖼️  图片优化..."
    
    # 检查优化工具
    tools_available=true
    
    if ! command -v cwebp &> /dev/null; then
        echo "⚠️  cwebp 未安装 (brew install webp)"
        tools_available=false
    fi
    
    if ! command -v optipng &> /dev/null; then
        echo "⚠️  optipng 未安装 (brew install optipng)"
        tools_available=false
    fi
    
    if ! command -v jpegoptim &> /dev/null; then
        echo "⚠️  jpegoptim 未安装 (brew install jpegoptim)"
        tools_available=false
    fi
    
    if [ "$tools_available" = "true" ]; then
        # 转换为 WebP
        echo "转换图片为 WebP 格式..."
        find public -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" | while read img; do
            webp_name="${img%.*}.webp"
            if [ ! -f "$webp_name" ]; then
                cwebp -q 85 "$img" -o "$webp_name" 2>/dev/null || true
                echo "✅ 转换: $img"
            fi
        done
        
        # 压缩 PNG
        echo "压缩 PNG 图片..."
        find public -name "*.png" -exec optipng -o2 {} \; 2>/dev/null || true
        
        # 压缩 JPEG
        echo "压缩 JPEG 图片..."
        find public -name "*.jpg" -o -name "*.jpeg" -exec jpegoptim --size=85% {} \; 2>/dev/null || true
    else
        echo "🔧 安装图片优化工具："
        echo "   brew install webp optipng jpegoptim"
    fi
fi

# 6. 压缩文件生成（仅生产模式）
if [ "$LOCAL_DEV" != "true" ]; then
    # 生成 Gzip 文件
    if command -v gzip &> /dev/null; then
        echo "🗜️  生成 Gzip 压缩文件..."
        find public -type f \( -name "*.html" -o -name "*.css" -o -name "*.js" -o -name "*.xml" -o -name "*.json" \) | while read file; do
            gzip -9 -c "$file" > "$file.gz"
        done
    fi
    
    # 生成 Brotli 文件
    if command -v brotli &> /dev/null; then
        echo "🗜️  生成 Brotli 压缩文件..."
        find public -type f \( -name "*.html" -o -name "*.css" -o -name "*.js" -o -name "*.xml" -o -name "*.json" \) | while read file; do
            brotli -9 -c "$file" > "$file.br"
        done
    fi
fi

# 7. 检查构建结果
echo "📊 构建统计..."
total_files=$(find public -type f | wc -l)
total_size=$(du -sh public | cut -f1)
echo "总文件数: $total_files"
echo "总大小: $total_size"

# 8. 验证关键文件
echo "✅ 验证关键文件..."
critical_files=("public/index.html" "public/sitemap.xml")
for file in "${critical_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file 存在"
    else
        echo "❌ $file 缺失"
    fi
done

# 9. 性能检查
if [ "$LOCAL_DEV" != "true" ]; then
    echo "🔍 性能检查..."
    
    # 检查大文件
    echo "大于 1MB 的文件:"
    find public -type f -size +1M -exec ls -lh {} \; 2>/dev/null | head -5 || echo "无"
    
    # 检查未优化的大型资源
    echo "较大的 JS/CSS 文件:"
    find public -name "*.js" -o -name "*.css" | xargs du -h 2>/dev/null | sort -hr | head -5 || echo "无"
fi

echo "🎉 构建完成！"

# 10. 启动本地服务器（可选）
if [ "$1" = "--serve" ]; then
    echo "🌐 启动本地服务器..."
    
    # 检查端口
    PORT=${2:-8080}
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
        echo "⚠️  端口 $PORT 已被占用，尝试 $((PORT+1))"
        PORT=$((PORT+1))
    fi
    
    echo "🌍 服务器地址: http://localhost:$PORT"
    echo "按 Ctrl+C 停止服务器"
    
    cd public && python3 -m http.server $PORT
fi

# 10. 可选：运行本地服务器进行测试
if [ "$1" = "--serve" ]; then
    echo "🌐 启动本地服务器..."
    cd public && python3 -m http.server 8080
fi
