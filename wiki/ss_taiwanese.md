# [Linux] Bash ss 使用法: 檢查網路連線狀態

## Overview
`ss` 是一個用於顯示網路連線的工具，能夠提供有關 TCP、UDP 和 UNIX 域套接字的詳細資訊。它是一個比 `netstat` 更快、更有效的替代品，適合用來監控系統的網路狀態。

## Usage
基本語法如下：
```bash
ss [options] [arguments]
```

## Common Options
- `-t`: 顯示 TCP 連線。
- `-u`: 顯示 UDP 連線。
- `-l`: 顯示正在監聽的套接字。
- `-p`: 顯示使用該連線的進程信息。
- `-n`: 以數字形式顯示地址和端口號，而非解析為名稱。

## Common Examples
1. 顯示所有 TCP 連線：
   ```bash
   ss -t
   ```

2. 顯示所有 UDP 連線：
   ```bash
   ss -u
   ```

3. 顯示所有正在監聽的套接字：
   ```bash
   ss -l
   ```

4. 顯示所有連線及其進程信息：
   ```bash
   ss -t -p
   ```

5. 以數字形式顯示所有連線：
   ```bash
   ss -n
   ```

## Tips
- 使用 `ss -t -l` 可以快速檢查哪些 TCP 端口正在監聽。
- 結合 `grep` 使用可以過濾特定的連線，例如：
  ```bash
  ss -t | grep 80
  ```
- 定期檢查連線狀態有助於發現潛在的安全問題或性能瓶頸。