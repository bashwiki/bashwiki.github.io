# [Linux] Bash watch 用法: 監控命令輸出

## Overview
`watch` 命令用於定期執行指定的命令並顯示其輸出，這對於監控系統狀態或命令結果的變化非常有用。

## Usage
基本語法如下：
```
watch [options] [arguments]
```

## Common Options
- `-n <seconds>`: 設定每次執行命令的間隔時間（以秒為單位）。
- `-d`: 高亮顯示輸出中變化的部分。
- `-t`: 隱藏標題，僅顯示命令的輸出。
- `-x`: 允許執行包含引號的命令。

## Common Examples
1. 每 2 秒更新一次 `date` 命令的輸出：
   ```bash
   watch -n 2 date
   ```

2. 監控 `df -h` 命令以查看磁碟使用情況，並高亮顯示變化：
   ```bash
   watch -d df -h
   ```

3. 每 5 秒執行 `uptime` 命令，並隱藏標題：
   ```bash
   watch -t -n 5 uptime
   ```

4. 監控特定目錄的檔案變化：
   ```bash
   watch -d ls -l /path/to/directory
   ```

## Tips
- 使用 `-n` 參數來調整更新頻率，根據需要選擇合適的時間間隔。
- 利用 `-d` 參數可以快速識別輸出中的變化，特別是在監控系統性能時。
- 結合其他命令使用 `watch`，如 `grep` 或 `awk`，可以進一步過濾和格式化輸出。