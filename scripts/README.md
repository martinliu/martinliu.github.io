# 图片优化和引用替换脚本

这个目录包含了用于优化网站图片的本地脚本，替代了原来在GitHub Actions中耗时的在线优化过程。

## 脚本文件

### 图片优化脚本
- `optimize-images-simple.sh` - 主要的图片优化脚本，支持多线程和增量处理
- `run-optimization.sh` - 简化的运行脚本，适合日常使用
- `install-deps.sh` - 安装必要的优化工具

### 图片引用替换脚本
- `replace_images_with_webp.py` - **新增**：自动替换 Markdown 文件中的图片引用为 WebP 格式

## 完整的图片优化工作流

1. **首次使用，安装依赖工具**：
```bash
./scripts/install-deps.sh
```

2. **运行图片优化**：
```bash
./scripts/run-optimization.sh
```

3. **替换 Markdown 文件中的图片引用为 WebP 格式**：
```bash
# 预览单个文件的更改
python3 scripts/replace_images_with_webp.py content/post/article.md -p -v

# 批量处理整个目录（递归）
python3 scripts/replace_images_with_webp.py content/post -r -f

# 处理所有内容（谨慎使用）
python3 scripts/replace_images_with_webp.py content -r -p
```

## 脚本功能详解

### 🔄 replace_images_with_webp.py（WebP 引用替换工具）

**功能：**
- 自动检测 Markdown 文件中的图片引用（JPG、JPEG、PNG）
- 检查对应的 WebP 文件是否存在
- 自动替换为 WebP 格式引用
- 支持单个文件或批量处理
- 提供预览和确认模式

**支持的引用格式：**
- Markdown 图片语法：`![alt text](image.jpg)`
- Front Matter 图片字段：`image: filename.png`

**使用选项：**
- `-p, --preview` - 只预览更改，不实际执行
- `-r, --recursive` - 递归处理目录下的所有 Markdown 文件
- `-f, --force` - 强制替换，不提示确认
- `-v, --verbose` - 显示详细输出

**使用示例：**
```bash
# 预览单个文件的替换
python3 scripts/replace_images_with_webp.py content/post/article.md -p -v

# 强制批量处理目录
python3 scripts/replace_images_with_webp.py content/post -r -f

# 递归预览所有内容
python3 scripts/replace_images_with_webp.py content -r -p
```

### optimize-images-simple.sh

- **多线程处理**：利用所有CPU核心并行处理图片
- **增量处理**：只处理新增或修改的图片文件
- **多格式支持**：
  - JPG/JPEG 优化（使用 jpegoptim）
  - PNG 优化（使用 optipng）
  - WebP 转换（使用 cwebp）
- **压缩统计**：显示优化前后的文件大小对比
- **macOS 优化**：针对 macOS 系统进行了兼容性优化

### 使用方法

```bash
# 基本用法 - 优化常见图片目录
./scripts/run-optimization.sh

# 优化特定目录
./scripts/optimize-images-simple.sh /path/to/images

# 安装依赖工具
./scripts/install-deps.sh
```

## 性能优化

脚本针对macOS进行了优化：

1. **智能线程分配**：自动检测CPU核心数
2. **内存管理**：避免同时处理过多大文件
3. **增量处理**：跳过已优化的文件
4. **缓存机制**：记录处理状态，避免重复工作

## 系统要求

- macOS 10.14 或更高版本
- Homebrew 包管理器
- 至少 2GB 可用磁盘空间（用于临时文件）

## 安装的工具

- `jpegoptim` - JPEG图片优化
- `optipng` - PNG图片优化  
- `webp` - WebP格式转换
- `parallel` - GNU并行处理工具

## 使用示例

```bash
# 优化所有图片（推荐日常使用）
./scripts/run-optimization.sh

# 优化特定目录
./scripts/optimize-images-simple.sh content/post/2024

# 安装依赖工具
./scripts/install-deps.sh
```

## 注意事项

1. **备份重要图片**：首次使用建议加上 `-b` 参数保留备份
2. **磁盘空间**：确保有足够空间存储优化后的文件
3. **处理时间**：大量图片的首次优化可能需要较长时间
4. **质量设置**：根据需要调整JPEG和WebP的质量参数

## 故障排除

### 常见问题

1. **权限错误**：确保脚本有执行权限
```bash
chmod +x scripts/*.sh
```

2. **工具未安装**：运行安装脚本
```bash
./scripts/install-deps.sh
```

3. **内存不足**：减少并行线程数
```bash
./scripts/optimize-images.sh -j 2
```

### 日志文件

脚本会在 `/tmp` 目录创建日志文件：
- `image-optimization.log` - 详细处理日志
- `optimization-stats.txt` - 优化统计信息

## 与CI/CD集成

这个脚本设计为本地使用，建议在以下情况运行：

1. 添加新图片后
2. 发布前的最终优化
3. 定期维护（如每周一次）

优化后的图片会自动被Git追踪，无需在CI/CD中重复处理。
