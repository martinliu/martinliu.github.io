// 性能优化的 JavaScript
(function() {
    'use strict';

    // 图片懒加载
    function lazyLoadImages() {
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.classList.remove('lazyload');
                            img.classList.add('lazyloaded');
                            observer.unobserve(img);
                        }
                    }
                });
            }, { rootMargin: '50px 0px' });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        } else {
            // 备用方案
            document.querySelectorAll('img[data-src]').forEach(img => {
                img.src = img.dataset.src;
            });
        }
    }

    // 防抖函数
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // 页面滚动性能优化
    let ticking = false;
    function updateScrollElements() {
        // 滚动相关的 DOM 操作
        const scrolled = window.pageYOffset;
        const rate = scrolled * -0.5;
        
        // 只有在必要时才操作 DOM
        if (Math.abs(rate) > 1) {
            document.body.style.setProperty('--scroll-offset', `${rate}px`);
        }
        
        ticking = false;
    }

    function requestScrollUpdate() {
        if (!ticking) {
            requestAnimationFrame(updateScrollElements);
            ticking = true;
        }
    }

    // Web Vitals 监控
    function sendToAnalytics(metric) {
        if (typeof gtag !== 'undefined') {
            gtag('event', metric.name, {
                event_category: 'Web Vitals',
                value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value),
                event_label: metric.id,
                non_interaction: true,
            });
        }
    }

    // 初始化
    function init() {
        // DOM 加载完成后初始化
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
            return;
        }

        // 启用图片懒加载
        lazyLoadImages();

        // 绑定滚动事件（防抖）
        window.addEventListener('scroll', requestScrollUpdate, { passive: true });

        // 监控 Web Vitals
        if ('web-vitals' in window) {
            getCLS(sendToAnalytics);
            getFID(sendToAnalytics);
            getFCP(sendToAnalytics);
            getLCP(sendToAnalytics);
            getTTFB(sendToAnalytics);
        }

        // 预加载重要页面
        const importantLinks = document.querySelectorAll('a[href^="/post/"], a[href^="/page/"]');
        if ('IntersectionObserver' in window) {
            const linkObserver = new IntersectionObserver(entries => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const link = entry.target;
                        const linkEl = document.createElement('link');
                        linkEl.rel = 'prefetch';
                        linkEl.href = link.href;
                        document.head.appendChild(linkEl);
                        linkObserver.unobserve(link);
                    }
                });
            });

            importantLinks.forEach(link => linkObserver.observe(link));
        }
    }

    // 启动
    init();

    // Service Worker 注册
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js')
                .then(registration => {
                    console.log('SW registered: ', registration);
                })
                .catch(registrationError => {
                    console.log('SW registration failed: ', registrationError);
                });
        });
    }
})();
