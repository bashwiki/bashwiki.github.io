# [台灣] Bash cron 使用法: 定時執行任務

## Overview
`cron` 是一個用於在 Unix 和類 Unix 系統上定期執行任務的工具。使用者可以設定任務在特定的時間或時間間隔自動執行，這對於自動化日常任務非常有用。

## Usage
基本語法如下：
```
cron [options] [arguments]
```

## Common Options
- `-l`：列出當前用戶的所有 cron 任務。
- `-e`：編輯當前用戶的 cron 任務。
- `-r`：刪除當前用戶的所有 cron 任務。

## Common Examples
以下是一些常見的 `cron` 使用範例：

1. 每天早上 7 點執行一個備份腳本：
   ```bash
   0 7 * * * /path/to/backup.sh
   ```

2. 每小時執行一次系統更新：
   ```bash
   0 * * * * sudo apt update && sudo apt upgrade -y
   ```

3. 每週一中午 12 點發送報告：
   ```bash
   0 12 * * 1 /path/to/send_report.sh
   ```

## Tips
- 確保你的腳本具有執行權限，否則 `cron` 將無法執行它。
- 使用完整的路徑來指定命令和腳本，以避免因環境變數不同而導致的錯誤。
- 定期檢查 `cron` 日誌，以確保任務正常執行，並及時排除故障。