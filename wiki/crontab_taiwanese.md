# [台灣] Bash crontab 使用法: 定時執行任務

## Overview
`crontab` 命令用於設定定時任務，讓使用者可以在指定的時間自動執行腳本或命令。這對於自動化系統維護或定期執行任務非常有用。

## Usage
基本語法如下：
```bash
crontab [options] [arguments]
```

## Common Options
- `-e`：編輯當前使用者的 crontab 文件。
- `-l`：列出當前使用者的 crontab 任務。
- `-r`：刪除當前使用者的 crontab 文件。
- `-i`：在刪除 crontab 時顯示提示。

## Common Examples
以下是一些常見的範例：

1. **編輯 crontab**
   ```bash
   crontab -e
   ```

2. **列出當前的 crontab 任務**
   ```bash
   crontab -l
   ```

3. **刪除 crontab**
   ```bash
   crontab -r
   ```

4. **設定每小時執行一次的任務**
   ```bash
   echo "0 * * * * /path/to/script.sh" | crontab -
   ```

5. **設定每天凌晨 1 點執行的任務**
   ```bash
   echo "0 1 * * * /path/to/backup.sh" | crontab -
   ```

## Tips
- 確保腳本具有執行權限，否則 crontab 將無法執行。
- 使用絕對路徑來指定腳本或命令，以避免路徑問題。
- 定期檢查 crontab 任務，確保它們正常運行。