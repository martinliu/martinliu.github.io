# AGENTS.md

This file defines repository-specific rules for coding agents working in this project.

## 1) Project Snapshot

- Type: Hugo static site (`hugo-theme-stack` module).
- Primary content: Markdown posts/pages under `content/`.
- Theme/layout customization: `layouts/`, `assets/`, `static/assets/`.
- Static files and images: `static/`.
- Build output: `public/` (generated artifacts).
- CI/CD: GitHub Actions builds/deploys to `gh-pages`; production Cloudflare deploy is manually triggered.

## 2) Source Of Truth And Boundaries

- Treat `content/`, `layouts/`, `assets/`, `config/`, `scripts/`, and `docs/` as editable source.
- Treat `public/` as generated output. Do not mass-edit generated files manually unless explicitly requested.
- Do not change deployment workflow intent in `.github/workflows/` unless the task is explicitly deployment-related.
- Keep changes minimal and task-focused. Avoid repository-wide formatting churn.

## 3) Preferred Commands

- Local preview: `hugo server`
- Production-like local build: `hugo --minify --gc --enableGitInfo --cleanDestinationDir --logLevel info`
- Image optimization (local): `./scripts/run-optimization.sh`
- Optimize one directory only: `./scripts/optimize-images-simple.sh <dir>`

## 4) Working Rules For Agents

- Before editing, inspect current file context and existing style.
- For content edits, preserve front matter fields and language-specific files (`index.zh-cn.md`, `index.en.md`).
- Keep permalink/slug/date semantics unchanged unless asked.
- For template/CSS/JS edits, prefer targeted partial/component changes over broad rewrites.
- Keep performance-sensitive behavior aligned with current optimization direction.
- For scripts/docs, ensure examples match actual repo commands and paths.
- Avoid introducing new toolchain requirements unless necessary.

## 5) Validation Checklist (Minimum)

Run the smallest applicable checks for the task:

- Content-only changes: run `hugo --minify --gc --enableGitInfo --cleanDestinationDir --logLevel info`.
- Template/config/script changes: run the same production-like build command above.
- If image-processing logic changed: run relevant script in preview/dry-run mode first when possible.

If a command cannot run in the current environment, state it explicitly in the final report.

## 6) Commit/PR Expectations

- Keep each change set cohesive and reversible.
- Provide what changed, why it changed, and what was validated.
- Include file-level references in summaries (path + line when useful).

## 7) High-Risk Areas

- Large binary/image directories in `static/` and `content/post/**/`.
- Deployment workflows in `.github/workflows/`.
- Generated output in `public/`.

Avoid broad or destructive operations in these areas unless explicitly requested.
