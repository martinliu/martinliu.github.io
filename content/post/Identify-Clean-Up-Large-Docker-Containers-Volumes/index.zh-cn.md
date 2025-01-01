---
title: "如何寻找占用空间最大的容器，并删除它所使用的卷，释放占用的空间？"
date: 2024-11-13T22:44:45+08:00
description:  一个报错的容器可能会耗尽服务器的所有可用磁盘空间，导致其他所有容器都无法正常工作。
slug: identify-clean-up-large-docker-containers-volumes
image: 91625BFA-9860-451D-B947-558D4B63D207.jpg
categories:
    - DevOps
tags:
    - docker
comments: true
toc: true

---

在 Docker 环境中，容器和卷的空间占用可能会随着时间的推移而增长，导致磁盘空间不足。本文将介绍如何寻找占用空间最大的容器，并删除它们使用的卷，以释放磁盘空间。

在 Azure 的环境中，我使用了 Portainer 来管理这个服务器上的所有容器。Portainer 在发生某种未知的故障后，在一段时间中产生了大量的错误日志，导致它所占用的数据卷空间暴涨，以至于沾满了所有可用磁盘空间，最后整个服务器上的所有其他容器都不工作了。

下面是解决这个运维故障的过程中的一些笔记，希望对读者有所帮助。

## 1. 查找占用空间最大的容器

### **查看容器日志文件的大小**

容器的日志文件通常会占用大量磁盘空间。可以通过以下命令查找 Docker 容器日志文件的大小：

```bash
find /var/lib/docker/containers/ -type f -name "*.log" -exec du -h {} + | sort -hr | head -n 10
```

该命令会列出所有容器日志文件的大小，并按从大到小排序。你可以通过查看输出结果，找出占用空间最大的容器日志文件。

### **查看容器的挂载数据大小**

除了日志文件，容器的挂载数据（例如文件系统层）也可能占用大量空间。要查看某个容器的挂载数据大小，可以使用以下命令：

```bash
docker ps -a --size
```

该命令将列出所有容器及其占用的磁盘空间。通过 `SIZE` 列，你可以查看每个容器的磁盘使用情况，并根据需要找出占用空间最大的容器。

## 2. 停止并删除容器

找到占用空间大的容器后，下一步是停止并删除它。

### **停止容器**

首先，停止正在运行的容器：

```bash
docker stop <container-id_or_name>
```

### **删除容器**

容器停止后，可以通过以下命令删除容器：

```bash
docker rm <container-id_or_name>
```

## 3. 删除容器使用的卷

容器删除后，挂载的卷可能依然存在并占用磁盘空间。要删除容器使用的卷，请按照以下步骤操作：

### **查看容器使用的卷**

你可以使用以下命令查看容器使用的卷：

```bash
docker inspect <container-id_or_name> | grep Mounts -A 10
```

这将输出容器的挂载信息，包括挂载的卷。你可以根据输出的信息找出容器使用的卷。

### **删除卷**

如果确定不再需要该卷，可以删除它：

```bash
docker volume rm <volume-name>
```

如果不确定卷是否仍然被其他容器使用，可以先列出所有卷并检查未使用的卷：

```bash
docker volume ls
```

### **删除所有未使用的卷**

如果你想删除所有没有挂载到容器的卷，可以使用以下命令：

```bash
docker volume prune
```

该命令将删除所有未挂载的卷，释放磁盘空间。

## 4. 释放卷占用的空间

如果某个卷占用了大量空间（例如 `portainer_data` 卷占用了 54G 空间），可以先检查卷的内容，并根据需要删除不必要的数据。

### **检查卷的内容**

可以进入卷的 `_data` 目录查看它的内容：

```bash
ls -l /var/lib/docker/volumes/portainer_data/_data
```

### **删除卷中的数据**

如果确认不再需要卷中的数据，可以删除这些数据：

```bash
rm -rf /var/lib/docker/volumes/portainer_data/_data/*
```

这将删除卷中的所有数据。

### **删除卷**

数据删除后，可以删除整个卷：

```bash
docker volume rm portainer_data
```

如果你不再需要该卷，删除它将释放空间。

## 5. 自动清理 Docker 系统资源

为了避免未来容器和卷占用过多磁盘空间，可以定期清理 Docker 的未使用资源。你可以使用 `docker system prune` 命令来删除所有未使用的容器、镜像、网络和卷。

### **清理所有未使用的资源**

```bash
docker system prune -a --volumes
```

- `-a` 参数表示删除所有未使用的镜像。
- `--volumes` 参数表示删除所有未挂载的卷。

此命令会清理 Docker 系统中的所有不再使用的资源，释放磁盘空间。

## 6. 检查释放后的空间

完成清理操作后，可以通过以下命令检查卷是否已经释放空间：

```bash
du -sh /var/lib/docker/volumes/portainer_data
```

如果卷中的数据已被删除，空间占用应当会显著减少。

## 总结

1. **查找占用空间大的容器：**
   - 查看容器日志文件和挂载数据的大小。
2. **停止并删除容器：**
   - 使用 `docker stop` 和 `docker rm` 停止并删除容器。
3. **删除容器使用的卷：**
   - 使用 `docker volume rm` 删除不再需要的卷。
   - 使用 `docker volume prune` 清理未使用的卷。
4. **释放卷占用的空间：**
   - 删除卷中的数据，或者删除整个卷。
5. **定期清理 Docker 系统资源：**
   - 使用 `docker system prune -a --volumes` 清理所有未使用的资源。

通过这些操作，你可以有效地管理 Docker 容器和卷，确保磁盘空间不会被占用过多，保持系统的清洁和高效。

## 参考

- [Docker Documentation](https://docs.docker.com/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)