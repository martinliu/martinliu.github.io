# Contributing

This repository is a Hugo-based blog/site. This guide applies to both human contributors and coding agents.

## Scope

- Source content: `content/`
- Theme/layout overrides: `layouts/`, `assets/`, `static/assets/`
- Site config: `config/_default/`
- Utilities: `scripts/`
- Generated output: `public/` (do not manually edit unless explicitly requested)

## Prerequisites

- Hugo Extended (CI uses `0.148.2`)
- Go toolchain (module/theme dependency resolution)
- Optional for image optimization on macOS: Homebrew + `webp`, `optipng`, `jpegoptim`

## Local Development

- Start local server: `hugo server`
- Production-like local build: `hugo --minify --gc --enableGitInfo --cleanDestinationDir --logLevel info`
- Docker local server build: `docker build -t martin-blog-dev .`
- Docker local server run: `docker run --rm -it -p 1313:1313 -v "$PWD:/workspace" martin-blog-dev`

## Image Workflow (Optional But Recommended)

- Run optimization: `./scripts/run-optimization.sh`
- Optimize a specific directory: `./scripts/optimize-images-simple.sh content/post`

## Change Guidelines

- Keep edits minimal and task-scoped.
- Preserve front matter integrity for markdown content.
- Avoid large-scale binary churn unless required by the task.
- Do not change CI/deployment semantics unless explicitly requested.

## Validation

Run at least:

- `hugo --minify --gc --enableGitInfo --cleanDestinationDir --logLevel info`

For image/script changes, run the relevant script in preview mode first when available.

## Pull Request Expectations

Each PR should include:

- What changed.
- Why it changed.
- How it was validated (commands and outcomes).
- Any known risks or follow-up items.

Prefer small, reviewable PRs over large mixed changes.
