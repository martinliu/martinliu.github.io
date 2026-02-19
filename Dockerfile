FROM golang:1.22-bookworm

ARG HUGO_VERSION=0.148.2

ENV DEBIAN_FRONTEND=noninteractive
ENV HUGO_CACHEDIR=/workspace/.hugo_cache

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    webp \
    jpegoptim \
    optipng \
    && rm -rf /var/lib/apt/lists/*

RUN arch="$(dpkg --print-architecture)" \
    && case "$arch" in \
        amd64)  hugo_arch="amd64" ;; \
        arm64)  hugo_arch="arm64" ;; \
        *) echo "Unsupported architecture: $arch" && exit 1 ;; \
    esac \
    && curl -fsSL -o /tmp/hugo.deb \
      "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-${hugo_arch}.deb" \
    && apt-get update \
    && apt-get install -y --no-install-recommends /tmp/hugo.deb \
    && rm -f /tmp/hugo.deb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

EXPOSE 1313

CMD ["hugo", "server", "--bind", "0.0.0.0", "--baseURL", "http://localhost:1313", "--buildDrafts", "--buildFuture", "--disableFastRender"]
