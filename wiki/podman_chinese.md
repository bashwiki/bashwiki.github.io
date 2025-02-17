# [Linux] Bash podman 用法: 管理容器和镜像

## 概述
Podman 是一个无守护进程的容器管理工具，允许用户创建、运行和管理容器和容器镜像。与 Docker 类似，Podman 提供了一个简单的命令行界面，使得容器的使用变得更加方便。

## 用法
Podman 的基本语法如下：
```
podman [options] [arguments]
```

## 常用选项
- `run`：创建并运行一个新的容器。
- `pull`：从远程仓库下载容器镜像。
- `ps`：列出正在运行的容器。
- `images`：列出本地可用的镜像。
- `rm`：删除一个或多个容器。
- `rmi`：删除一个或多个镜像。

## 常见示例
1. **运行一个新的容器**
   ```bash
   podman run -d --name my_container nginx
   ```
   这个命令会在后台运行一个名为 `my_container` 的 Nginx 容器。

2. **查看正在运行的容器**
   ```bash
   podman ps
   ```
   该命令列出所有当前正在运行的容器。

3. **下载一个镜像**
   ```bash
   podman pull alpine
   ```
   这个命令从远程仓库下载 Alpine Linux 镜像。

4. **删除一个容器**
   ```bash
   podman rm my_container
   ```
   该命令会删除名为 `my_container` 的容器。

5. **列出本地镜像**
   ```bash
   podman images
   ```
   这个命令显示本地存储的所有镜像。

## 小贴士
- 使用 `-d` 选项可以让容器在后台运行，这样你可以继续使用命令行。
- 定期使用 `podman ps -a` 来查看所有容器，包括已停止的容器。
- 在删除容器或镜像之前，确保它们不再被使用，以避免意外数据丢失。