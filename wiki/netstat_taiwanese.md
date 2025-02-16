# [台灣] Bash netstat 使用法: 檢查網路連線狀態

## Overview
`netstat` 是一個用於顯示網路連線、路由表、介面統計和網路協定等資訊的命令。它對於監控和排除網路問題非常有用。

## Usage
基本的語法如下：
```bash
netstat [options] [arguments]
```

## Common Options
- `-a`: 顯示所有連線和監聽的端口。
- `-t`: 顯示 TCP 連線。
- `-u`: 顯示 UDP 連線。
- `-n`: 以數字格式顯示地址和端口號，而不是解析為名稱。
- `-l`: 只顯示監聽的端口。
- `-p`: 顯示每個連線的進程 ID 和名稱。

## Common Examples
- 顯示所有網路連線：
  ```bash
  netstat -a
  ```

- 顯示所有 TCP 連線：
  ```bash
  netstat -t
  ```

- 顯示所有 UDP 連線：
  ```bash
  netstat -u
  ```

- 顯示監聽的端口：
  ```bash
  netstat -l
  ```

- 顯示連線的進程 ID 和名稱：
  ```bash
  netstat -p
  ```

- 結合多個選項顯示所有 TCP 連線及其進程：
  ```bash
  netstat -t -p
  ```

## Tips
- 使用 `-n` 選項可以加快顯示速度，特別是在網路名稱解析較慢的情況下。
- 定期檢查網路連線狀態可以幫助及早發現潛在的問題。
- 結合其他命令（如 `grep`）可以更有效地過濾和查找特定的連線資訊。