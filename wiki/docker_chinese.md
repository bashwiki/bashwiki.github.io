# [Linux] Bash docker 使用: 管理容器和镜像

## 概述
Docker 是一个开源平台，用于自动化应用程序的部署、扩展和管理。它通过容器技术将应用程序及其依赖打包在一起，确保在任何环境中都能一致运行。

## 用法
基本语法如下：
```bash
docker [options] [arguments]
```

## 常用选项
- `run`: 创建并启动一个新的容器。
- `ps`: 列出当前运行的容器。
- `images`: 列出本地可用的镜像。
- `pull`: 从 Docker Hub 或其他注册中心下载镜像。
- `build`: 从 Dockerfile 构建镜像。

## 常见示例
1. **运行一个新的容器**
   ```bash
   docker run hello-world
   ```
   这个命令会下载并运行一个简单的 hello-world 镜像，验证 Docker 是否安装正确。

2. **列出当前运行的容器**
   ```bash
   docker ps
   ```
   该命令显示所有正在运行的容器及其状态。

3. **列出所有镜像**
   ```bash
   docker images
   ```
   这个命令列出本地存储的所有 Docker 镜像。

4. **从 Docker Hub 下载镜像**
   ```bash
   docker pull nginx
   ```
   该命令从 Docker Hub 下载 Nginx 镜像。

5. **构建镜像**
   ```bash
   docker build -t my-image:latest .
   ```
   这个命令根据当前目录下的 Dockerfile 构建一个名为 my-image 的镜像。

## 提示
- 使用 `docker-compose` 来管理多容器应用程序，可以简化配置和启动过程。
- 定期清理未使用的镜像和容器，使用 `docker system prune` 命令。
- 在生产环境中，确保容器的安全性，定期更新镜像和依赖。