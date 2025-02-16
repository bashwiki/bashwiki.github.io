# [Linux] Bash podman 使用方式: 管理容器的工具

## Overview
Podman 是一個無需守護進程的容器管理工具，允許用戶創建、運行和管理容器。它的設計目的是提供與 Docker 相似的功能，但具有更高的安全性和靈活性。

## Usage
基本語法如下：
```bash
podman [options] [arguments]
```

## Common Options
- `run`: 創建並運行一個新的容器。
- `ps`: 列出當前運行的容器。
- `images`: 顯示本地可用的容器映像。
- `pull`: 從遠端倉庫下載容器映像。
- `rm`: 刪除一個或多個容器。

## Common Examples
- **運行一個新的容器**
  ```bash
  podman run -d nginx
  ```
  這會在後台運行一個 Nginx 容器。

- **列出運行中的容器**
  ```bash
  podman ps
  ```
  此命令會顯示所有當前運行的容器。

- **拉取一個映像**
  ```bash
  podman pull ubuntu
  ```
  這會從 Docker Hub 下載 Ubuntu 映像。

- **刪除一個容器**
  ```bash
  podman rm my_container
  ```
  此命令會刪除名為 `my_container` 的容器。

## Tips
- 使用 `podman --help` 獲取更多選項和用法說明。
- 為了提高安全性，考慮使用 Podman 的無根模式來運行容器。
- 定期清理不再使用的容器和映像，以節省磁碟空間。