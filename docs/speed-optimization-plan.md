# 🚀 网站加速紧急优化计划

## 📊 当前性能基线
- **FCP**: 3.0s → 目标 <1.8s
- **LCP**: 8.1s → 目标 <2.5s ⚠️ **最高优先级**
- **Speed Index**: 4.6s → 目标 <3.4s

## 🎯 立即实施方案（本次提交）

### ✅ 已完成的优化
1. **LCP 元素优化**
   - 创建专用 Hero 图片组件 (`hero-image.html`)
   - 移除首屏图片的懒加载
   - 添加 `fetchpriority="high"` 和预加载
   - 支持 AVIF/WebP/JPEG 三格式

2. **Critical CSS 内联**
   - 首屏关键样式内联到 HTML
   - 减少渲染阻塞
   - 优化字体加载策略

3. **增强图片优化**
   - GitHub Actions 增加 AVIF 格式生成
   - 更激进的压缩策略
   - 降低压缩阈值（50KB）

4. **缓存策略优化**
   - 创建 `_headers` 文件
   - 静态资源长期缓存
   - HTML 短期缓存 + stale-while-revalidate

5. **资源预加载**
   - 关键域名预连接
   - 首屏图片预加载
   - 字体预加载

## 🔄 下一步实施计划

### 第1天 - 立即实施
- [ ] 在主题模板中应用新的 Hero 图片组件
- [ ] 在 `<head>` 中包含 Critical CSS
- [ ] 添加资源预加载组件
- [ ] 测试 GitHub Actions 图片优化

### 第2-3天 - 模板优化
- [ ] 识别并优化主页的 LCP 元素
- [ ] 确保首屏图片使用 `hero-image.html` 组件
- [ ] 非首屏图片使用优化后的 `responsive-image.html`
- [ ] 添加 `fetchpriority="high"` 到 LCP 元素

### 第4-5天 - 资源优化
- [ ] 审查并移除非关键的第三方脚本
- [ ] 实施字体优化（自托管 + font-display: swap）
- [ ] 优化 CSS 加载（Critical CSS + 延迟加载非关键CSS）

## 🧪 测试验证

### 性能测试
```bash
# 本地测试
hugo server

# Lighthouse 测试
lighthouse https://martinliu.cn --output html --output-path ./report.html

# PageSpeed Insights
# https://pagespeed.web.dev/
```

### 预期效果
- **FCP**: 3.0s → ~1.5s (50% 提升)
- **LCP**: 8.1s → ~2.0s (75% 提升) 🎯
- **Speed Index**: 4.6s → ~2.8s (40% 提升)

## 🔧 具体使用方法

### 1. Hero 图片（首屏）
```html
<!-- 首页 Hero 区域 -->
{{ partial "components/hero-image.html" (dict 
  "src" "images/hero.jpg" 
  "alt" "网站主页横幅" 
  "width" 1200 
  "height" 630
) }}
```

### 2. 普通图片（非首屏）
```html
<!-- 内容区域图片 -->
{{ partial "components/responsive-image.html" (dict 
  "src" "images/content.jpg" 
  "alt" "内容图片" 
  "width" 800 
  "height" 600
  "lazy" true
) }}
```

### 3. 在 head 中包含优化组件
```html
<head>
  <!-- Critical CSS -->
  {{ partial "head/critical-css.html" . }}
  
  <!-- 资源预加载 -->
  {{ partial "head/preload.html" . }}
  
  <!-- 其他 head 内容 -->
</head>
```

## 📈 监控和验证

### 自动化监控
- GitHub Actions 构建时的性能统计
- CloudFlare Analytics
- 定期 Lighthouse 报告

### 手动验证检查清单
- [ ] 首屏图片是否立即加载（无懒加载）
- [ ] AVIF/WebP 格式是否正确生成
- [ ] 缓存头是否正确设置
- [ ] Critical CSS 是否内联
- [ ] LCP 元素是否 <2.5s

## 🚨 关键注意事项

1. **LCP 元素识别**
   - 使用 Chrome DevTools 的 Performance 面板
   - 确认最大内容绘制元素
   - 确保该元素使用 `hero-image.html` 组件

2. **图片格式支持检查**
   - 确认 Hugo 版本支持 AVIF（需要 Hugo Extended）
   - 验证浏览器对 AVIF 的支持率

3. **缓存验证**
   - 检查 CloudFlare 缓存设置
   - 验证 `_headers` 文件是否生效

现在立即提交这些优化，然后部署测试！🚀
