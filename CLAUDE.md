# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Hugo-based static website for Martin Liu's blog, focused on SRE (Site Reliability Engineering), DevOps, and IT operations topics. The site is hosted on GitHub Pages and optimized for performance with image compression, caching, and modern web practices.

## Architecture and Structure

The repository follows a standard Hugo structure:
- `content/` - Blog posts and pages organized by date and categories
- `themes/` - Hugo theme (Stack theme by Jimmy)
- `static/` - Static assets like images and CSS
- `assets/` - Source files for CSS, JS, and other assets
- `config/` - Hugo configuration files
- `scripts/` - Optimization and build scripts

## Key Technologies

- **Hugo**: Static site generator (version 0.148.2)
- **Stack Theme**: Hugo theme by Jimmy
- **Cloudflare**: DNS, HTTPS, and Pages for hosting
- **GitHub Actions**: CI/CD for building and deploying
- **Image Optimization**: WebP conversion and compression using cwebp, optipng, jpegoptim

## Development Commands

### Build the site
```bash
hugo --minify --gc --enableGitInfo --cleanDestinationDir
```

### Serve locally for development
```bash
hugo server --bind 0.0.0.0 --baseURL http://localhost:1313 --buildDrafts --buildFuture --disableFastRender
```

### Run image optimization
```bash
./scripts/run-optimization.sh
```

### Run image optimization on specific directory
```bash
./scripts/optimize-images-simple.sh content/post
```

## Deployment

The site deploys automatically via GitHub Actions:
1. Push to any branch triggers a build and deploy to GitHub Pages
2. Manual deployment to production (Cloudflare) requires triggering the `CD - Push to PRD*CloudFlare` workflow with confirmation

## Performance Optimizations

The site includes several performance optimizations:
- WebP image conversion for modern browsers
- Gzip and Brotli compression
- CDN caching headers
- Image optimization with incremental processing
- Hugo's built-in minification and cache control

## Development Workflow

1. Make changes to content in `content/` or assets in `assets/`
2. Run `hugo server` to preview locally
3. Optimize images with `./scripts/run-optimization.sh` before committing
4. Commit and push to trigger automated build and deployment

## Key Files and Directories

- `config/_default/config.toml` - Main Hugo configuration
- `config/_default/params.toml` - Theme parameters and settings
- `scripts/run-optimization.sh` - Main image optimization script
- `.github/workflows/deploy-2-page.yml` - GitHub Actions workflow for deployment
- `Dockerfile` - Development container configuration