# [Linux] Bash ps 使用法: 查看目前運行的程序

## Overview
`ps` 命令用於顯示當前系統中運行的進程。它提供了進程的快照，讓用戶能夠查看哪些程序正在運行及其相關信息。

## Usage
基本語法如下：
```
ps [options] [arguments]
```

## Common Options
- `-e` 或 `-A`: 顯示所有進程。
- `-f`: 顯示完整格式，包括進程的父進程ID。
- `-u [user]`: 顯示指定用戶的進程。
- `-l`: 顯示長格式的信息。
- `-aux`: 顯示所有進程，包括其他用戶的進程。

## Common Examples
1. 顯示所有進程：
   ```bash
   ps -e
   ```

2. 顯示當前用戶的進程：
   ```bash
   ps -u $USER
   ```

3. 顯示完整格式的進程信息：
   ```bash
   ps -f
   ```

4. 顯示所有進程及其詳細信息：
   ```bash
   ps aux
   ```

5. 顯示特定用戶的進程：
   ```bash
   ps -u username
   ```

## Tips
- 使用 `ps aux` 可以獲得最全面的進程信息，適合進行系統監控。
- 結合 `grep` 命令可以過濾特定進程，例如：
  ```bash
  ps aux | grep firefox
  ```
- 定期檢查運行的進程有助於維持系統性能，避免不必要的資源消耗。