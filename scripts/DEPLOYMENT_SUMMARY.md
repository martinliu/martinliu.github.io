# 图片压缩脚本精简说明

## 目标

对 `scripts/` 中的图片处理脚本做收敛，只保留与当前 CI 语境一致的压缩流程，去除重复/无关脚本。

## 当前保留脚本

- `scripts/optimize-images-simple.sh`
  - 核心图片压缩脚本（JPG/JPEG/PNG 优化 + WebP 生成）。
  - 内置持久化记忆缓存（`.image-cache/state/`），仅处理新增或内容变更图片。
- `scripts/run-optimization.sh`
  - 批量入口脚本，按既定目录调用核心脚本。

## 已移除脚本

- `scripts/install-deps.sh`
  - 与 CI 无直接关系，且功能可由环境预装工具替代。
- `scripts/replace_images_with_webp.py`
  - 属于 Markdown 引用替换，不是图片压缩链路。
- `scripts/batch_webp_replace.py`
  - 对 `replace_images_with_webp.py` 的重复封装。

## 与 CI 的关系

GitHub Actions（`.github/workflows/deploy-2-page.yml`）中保留了本地压缩流程说明：

- 本地执行 `./scripts/run-optimization.sh`
- 核心脚本为 `./scripts/optimize-images-simple.sh`

## 本地运行

```bash
# 全量入口
./scripts/run-optimization.sh

# 指定目录
./scripts/optimize-images-simple.sh content/post
```

## 依赖

```bash
brew install webp optipng jpegoptim
```

## 缓存控制

- 默认会复用 `.image-cache/state/` 中的状态文件，减少重复处理。
- 如果需要强制全量重跑，可删除缓存目录：

```bash
rm -rf .image-cache/state
```
