#!/bin/bash
# 图片批量优化脚本

echo "开始优化静态资源图片..."

# 创建WebP版本的图片
find /Users/martinliu/code/martinliu.github.io/static/img -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" | while read img; do
    webp_name="${img%.*}.webp"
    if [ ! -f "$webp_name" ]; then
        echo "转换: $img -> $webp_name"
        # 如果有 cwebp 工具，取消注释以下行
        # cwebp -q 85 "$img" -o "$webp_name"
    fi
done

# 优化PNG图片
find /Users/martinliu/code/martinliu.github.io/static/img -name "*.png" | while read img; do
    echo "压缩PNG: $img"
    # 如果有 optipng 工具，取消注释以下行
    # optipng -o2 "$img"
done

# 优化JPEG图片
find /Users/martinliu/code/martinliu.github.io/static/img -name "*.jpg" -o -name "*.jpeg" | while read img; do
    echo "压缩JPEG: $img"
    # 如果有 jpegoptim 工具，取消注释以下行  
    # jpegoptim --size=85% "$img"
done

echo "图片优化完成!"
echo ""
echo "建议安装以下工具来启用图片优化:"
echo "brew install webp optipng jpegoptim"
