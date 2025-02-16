# [Linux] Bash systemctl 使用法: 管理系統服務

## Overview
`systemctl` 是一個用於管理 Linux 系統上系統服務的命令。它是 systemd 的一部分，允許用戶啟動、停止、重新啟動和查詢服務的狀態。

## Usage
基本語法如下：
```
systemctl [選項] [參數]
```

## Common Options
- `start`：啟動指定的服務。
- `stop`：停止指定的服務。
- `restart`：重新啟動指定的服務。
- `status`：顯示指定服務的當前狀態。
- `enable`：設置服務在開機時自動啟動。
- `disable`：禁止服務在開機時自動啟動。

## Common Examples
- 啟動服務：
  ```bash
  systemctl start nginx
  ```

- 停止服務：
  ```bash
  systemctl stop nginx
  ```

- 重新啟動服務：
  ```bash
  systemctl restart nginx
  ```

- 查詢服務狀態：
  ```bash
  systemctl status nginx
  ```

- 設置服務開機自動啟動：
  ```bash
  systemctl enable nginx
  ```

- 禁止服務開機自動啟動：
  ```bash
  systemctl disable nginx
  ```

## Tips
- 使用 `systemctl list-units --type=service` 可以查看所有服務的列表及其狀態。
- 在執行需要管理權限的命令時，記得使用 `sudo` 來獲取必要的權限。
- 定期檢查服務狀態，確保系統運行正常。