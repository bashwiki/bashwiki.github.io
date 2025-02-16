# [台灣] Bash ufw 使用方法: 管理防火牆規則

## Overview
`ufw`（Uncomplicated Firewall）是一個用於管理 Linux 系統防火牆的工具，旨在簡化 iptables 的使用。它提供了一個簡單的命令行界面，讓用戶能夠輕鬆設置和管理防火牆規則，以提高系統的安全性。

## Usage
基本語法如下：
```
ufw [options] [arguments]
```

## Common Options
- `enable`：啟用防火牆。
- `disable`：禁用防火牆。
- `allow`：允許特定的連接。
- `deny`：拒絕特定的連接。
- `status`：顯示防火牆的當前狀態和規則。
- `reset`：重置防火牆到預設狀態。

## Common Examples
- 啟用防火牆：
  ```bash
  sudo ufw enable
  ```

- 禁用防火牆：
  ```bash
  sudo ufw disable
  ```

- 允許 SSH 連接：
  ```bash
  sudo ufw allow ssh
  ```

- 允許特定端口（例如 80 端口）：
  ```bash
  sudo ufw allow 80
  ```

- 拒絕特定端口（例如 23 端口）：
  ```bash
  sudo ufw deny 23
  ```

- 查看防火牆狀態：
  ```bash
  sudo ufw status
  ```

- 重置防火牆：
  ```bash
  sudo ufw reset
  ```

## Tips
- 在啟用防火牆之前，確保已允許必要的服務（如 SSH），以免鎖定自己。
- 定期檢查防火牆狀態，確保規則符合當前需求。
- 使用 `ufw status verbose` 可以獲得更詳細的狀態信息。