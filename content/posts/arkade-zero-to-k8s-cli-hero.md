---
date: 2020-08-03T00:42:14+08:00
title: "Arkade Zero to K8s Cli Hero"
subtitle: ""
description: ""
categories: "DevOps"
tags: ["DevOps"]
keywords: ["DevOps"]
bigimg: [{src: "/images/abstract-1.jpg", desc: "DevOps"}]
draft: true
---

github.com/alexellis/arkade/

安装 arkade

```bash
# Note: you can also run without `sudo` and move the binary yourself
curl -sLS https://dl.get-arkade.dev | sudo sh

arkade --help
ark --help  # a handy alias

# Windows users with Git Bash
curl -sLS https://dl.get-arkade.dev | sh
```

```sh
➜ ~ curl -sLS https://dl.get-arkade.dev | sudo sh
Downloading package https://github.com/alexellis/arkade/releases/download/0.5.1/arkade-darwin as /tmp/arkade-darwin
Download complete.

Running with sufficient permissions to attempt to move arkade to /usr/local/bin
New version of arkade installed to /usr/local/bin
Creating alias 'ark' for 'arkade'.
            _             _      
  __ _ _ __| | ____ _  __| | ___ 
 / _` | '__| |/ / _` |/ _` |/ _ \
| (_| | |  |   < (_| | (_| |  __/
 \__,_|_|  |_|\_\__,_|\__,_|\___|

Get Kubernetes apps the easy way

Version: 0.5.1
Git Commit: 3c3970eafdca83570d5b1b85902a4957f9dfba16
```

## arkade get

arkade get kubectl

arkade get kind

kind create cluster

## arkade install 

arkade install kubernetes-dashboard

安装和访问 dashboard

arkade install ingress-nginx --help

