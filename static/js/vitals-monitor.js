// Web Vitals 监控脚本
(function() {
    // 只在生产环境启用监控
    if (location.hostname !== 'martinliu.cn') return;

    // 延迟加载 Web Vitals 库
    function loadWebVitals() {
        const script = document.createElement('script');
        script.src = 'https://unpkg.com/web-vitals@3/dist/web-vitals.js';
        script.onload = initWebVitals;
        document.head.appendChild(script);
    }

    function initWebVitals() {
        function sendToGoogleAnalytics({name, delta, value, id}) {
            gtag('event', name, {
                event_category: 'Web Vitals',
                event_label: id,
                value: Math.round(name === 'CLS' ? delta * 1000 : delta),
                non_interaction: true,
            });
        }

        function sendToCustomAnalytics({name, delta, value, id}) {
            // 发送到自定义分析服务
            fetch('/api/analytics/vitals', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    metric: name,
                    value: value,
                    delta: delta,
                    id: id,
                    url: location.href,
                    timestamp: Date.now()
                })
            }).catch(console.error);
        }

        // 监控所有核心指标
        webVitals.getCLS(sendToGoogleAnalytics);
        webVitals.getFID(sendToGoogleAnalytics);
        webVitals.getFCP(sendToGoogleAnalytics);
        webVitals.getLCP(sendToGoogleAnalytics);
        webVitals.getTTFB(sendToGoogleAnalytics);

        // 发送到自定义分析（可选）
        webVitals.getCLS(sendToCustomAnalytics);
        webVitals.getFID(sendToCustomAnalytics);
        webVitals.getFCP(sendToCustomAnalytics);
        webVitals.getLCP(sendToCustomAnalytics);
        webVitals.getTTFB(sendToCustomAnalytics);
    }

    // 页面完全加载后再加载监控脚本
    if (document.readyState === 'complete') {
        setTimeout(loadWebVitals, 1000);
    } else {
        window.addEventListener('load', () => {
            setTimeout(loadWebVitals, 1000);
        });
    }

    // 错误监控
    window.addEventListener('error', function(e) {
        gtag('event', 'exception', {
            description: e.error ? e.error.toString() : e.message,
            fatal: false,
            source: e.filename,
            lineno: e.lineno,
            colno: e.colno
        });
    });

    // 未处理的 Promise 拒绝
    window.addEventListener('unhandledrejection', function(e) {
        gtag('event', 'exception', {
            description: 'Unhandled Promise Rejection: ' + e.reason,
            fatal: false
        });
    });
})();
