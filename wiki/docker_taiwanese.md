# [台灣] Bash docker 用法: 管理容器和映像檔

## Overview
Docker 是一個開源平台，讓開發者可以自動化應用程式的部署、擴展和管理。它使用容器技術來打包應用程式及其依賴項，確保在任何環境中都能一致運行。

## Usage
基本的命令語法如下：
```bash
docker [options] [arguments]
```

## Common Options
- `run`: 創建並啟動一個新的容器。
- `ps`: 列出當前正在運行的容器。
- `images`: 列出本地的所有映像檔。
- `rm`: 刪除一個或多個容器。
- `rmi`: 刪除一個或多個映像檔。

## Common Examples
- 啟動一個新的容器並運行一個交互式的 bash：
  ```bash
  docker run -it ubuntu bash
  ```
  
- 查看當前運行的容器：
  ```bash
  docker ps
  ```

- 列出所有本地映像檔：
  ```bash
  docker images
  ```

- 刪除一個已停止的容器：
  ```bash
  docker rm <container_id>
  ```

- 刪除一個映像檔：
  ```bash
  docker rmi <image_id>
  ```

## Tips
- 使用 `docker-compose` 來管理多個容器的應用程式，這樣可以簡化配置和啟動過程。
- 定期清理未使用的容器和映像檔，以釋放磁碟空間。
- 在開發過程中，使用 `--rm` 選項來自動刪除容器，避免堆積不必要的容器。