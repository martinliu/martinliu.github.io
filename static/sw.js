// Service Worker - 缓存优化策略
const CACHE_NAME = 'martinliu-blog-v2';
const DYNAMIC_CACHE = 'martinliu-dynamic-v2';

// 需要缓存的静态资源
const STATIC_ASSETS = [
    '/',
    '/scss/style.min.css',
    '/js/main.min.js',
    '/js/performance.js',
    '/img/avatar.png',
    '/favicon.ico'
];

// 安装事件 - 预缓存关键资源
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('预缓存静态资源');
                return cache.addAll(STATIC_ASSETS);
            })
            .then(() => self.skipWaiting())
    );
});

// 激活事件 - 清理旧缓存
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME && cacheName !== DYNAMIC_CACHE) {
                        console.log('删除旧缓存:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// 请求拦截 - 缓存策略
self.addEventListener('fetch', event => {
    const { request } = event;
    const url = new URL(request.url);

    // 只处理同源请求
    if (url.origin !== location.origin) {
        return;
    }

    // HTML 请求 - 网络优先策略
    if (request.headers.get('accept').includes('text/html')) {
        event.respondWith(
            fetch(request)
                .then(response => {
                    // 缓存HTML页面（排除管理页面）
                    if (response.status === 200 && !url.pathname.includes('/admin/')) {
                        const responseClone = response.clone();
                        caches.open(DYNAMIC_CACHE).then(cache => {
                            cache.put(request, responseClone);
                        });
                    }
                    return response;
                })
                .catch(() => {
                    // 网络失败时从缓存返回
                    return caches.match(request)
                        .then(cachedResponse => {
                            if (cachedResponse) {
                                return cachedResponse;
                            }
                            // 返回离线页面
                            return caches.match('/offline.html');
                        });
                })
        );
        return;
    }

    // 静态资源 - 缓存优先策略
    if (request.url.match(/\.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2)$/)) {
        event.respondWith(
            caches.match(request)
                .then(cachedResponse => {
                    if (cachedResponse) {
                        // 后台更新缓存
                        fetch(request).then(response => {
                            if (response.status === 200) {
                                const responseClone = response.clone();
                                caches.open(CACHE_NAME).then(cache => {
                                    cache.put(request, responseClone);
                                });
                            }
                        }).catch(() => {});
                        
                        return cachedResponse;
                    }
                    
                    // 缓存中没有，从网络获取
                    return fetch(request).then(response => {
                        if (response.status === 200) {
                            const responseClone = response.clone();
                            caches.open(CACHE_NAME).then(cache => {
                                cache.put(request, responseClone);
                            });
                        }
                        return response;
                    });
                })
        );
        return;
    }

    // API 请求 - 网络优先，短时间缓存
    if (url.pathname.startsWith('/api/')) {
        event.respondWith(
            fetch(request)
                .then(response => {
                    if (response.status === 200) {
                        const responseClone = response.clone();
                        caches.open(DYNAMIC_CACHE).then(cache => {
                            // API 缓存5分钟
                            const headers = new Headers(responseClone.headers);
                            headers.append('sw-cache-timestamp', Date.now().toString());
                            const cachedResponse = new Response(responseClone.body, {
                                status: responseClone.status,
                                statusText: responseClone.statusText,
                                headers: headers
                            });
                            cache.put(request, cachedResponse);
                        });
                    }
                    return response;
                })
                .catch(() => {
                    return caches.match(request).then(cachedResponse => {
                        if (cachedResponse) {
                            const cacheTime = cachedResponse.headers.get('sw-cache-timestamp');
                            if (cacheTime && (Date.now() - parseInt(cacheTime)) < 300000) { // 5分钟内
                                return cachedResponse;
                            }
                        }
                        throw new Error('No cached response available');
                    });
                })
        );
        return;
    }
});

// 后台同步
self.addEventListener('sync', event => {
    if (event.tag === 'background-sync') {
        event.waitUntil(doBackgroundSync());
    }
});

function doBackgroundSync() {
    // 后台同步逻辑，如离线时收集的分析数据
    return Promise.resolve();
}
