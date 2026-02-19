# 图片压缩脚本说明

当前目录只保留与 CI 流程一致的图片压缩脚本。

## 保留脚本

- `optimize-images-simple.sh`
  - 核心压缩脚本：处理 JPG/JPEG/PNG，执行原图优化并生成 WebP。
  - 支持持久化记忆缓存（基于图片内容哈希），同一图片不会重复处理。

- `run-optimization.sh`
  - 入口脚本：按目录批量调用 `optimize-images-simple.sh`。
  - 默认处理目录：`static/images`、`assets/img`、`content`。

## 使用方法

```bash
# 运行批量优化
./scripts/run-optimization.sh

# 仅优化指定目录
./scripts/optimize-images-simple.sh content/post
```

## 依赖

在 macOS 上请先安装：

```bash
brew install webp optipng jpegoptim
```

## 说明

- CI 工作流中的图片优化说明与本地脚本保持一致（见 `.github/workflows/deploy-2-page.yml` 注释）。
- 已移除与 CI 无关或重复封装的脚本，避免维护负担与行为分叉。
- 记忆缓存目录为 `.image-cache/state/`，删除该目录可强制全量重跑。
