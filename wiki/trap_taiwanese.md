# [Linux] Bash trap 用法: 捕捉信號和執行清理動作

## Overview
`trap` 命令用於捕捉特定的信號並執行指定的命令。這在腳本中非常有用，特別是當你需要在腳本終止或中斷時進行清理工作。

## Usage
基本語法如下：
```bash
trap [options] [commands] [signals]
```

## Common Options
- `-l`: 列出所有可用的信號名稱。
- `-p`: 顯示當前的 trap 設定。
- `commands`: 在接收到指定信號時執行的命令。

## Common Examples
1. **捕捉 SIGINT 信號（Ctrl+C）**
   ```bash
   trap 'echo "Script interrupted"; exit' SIGINT
   while true; do
       echo "Running..."
       sleep 1
   done
   ```

2. **在腳本結束時清理臨時文件**
   ```bash
   trap 'rm -f /tmp/mytempfile' EXIT
   touch /tmp/mytempfile
   echo "Doing something..."
   ```

3. **捕捉多個信號**
   ```bash
   trap 'echo "Received SIGTERM"; exit' SIGTERM SIGQUIT
   while true; do
       echo "Waiting for signals..."
       sleep 2
   done
   ```

## Tips
- 使用 `trap` 來確保即使在異常情況下也能執行清理工作。
- 測試腳本時，可以使用 `trap -p` 來查看當前的 trap 設定。
- 將清理命令放在 `trap` 中，以避免重複代碼。