# [Linux] Bash inotifywait 使用法: 監控檔案系統事件

## Overview
`inotifywait` 是一個用於監控檔案系統事件的命令行工具。它可以即時監測指定目錄或檔案的變化，並在發生特定事件時輸出通知，這對於自動化任務或監控系統狀態非常有用。

## Usage
基本語法如下：
```bash
inotifywait [options] [arguments]
```

## Common Options
- `-m`：持續監控，直到手動停止。
- `-r`：遞迴監控子目錄。
- `-e`：指定要監控的事件類型，例如 `modify`、`create`、`delete` 等。
- `--format`：自定義輸出格式。

## Common Examples
1. 監控目錄中的檔案變化：
   ```bash
   inotifywait -m /path/to/directory
   ```

2. 監控特定事件（如檔案創建）：
   ```bash
   inotifywait -m -e create /path/to/directory
   ```

3. 遞迴監控子目錄中的所有變化：
   ```bash
   inotifywait -m -r /path/to/directory
   ```

4. 自定義輸出格式：
   ```bash
   inotifywait -m --format '%w%f %e' -e modify /path/to/file
   ```

## Tips
- 使用 `-m` 選項可以讓你持續監控，適合用於長時間運行的監控任務。
- 結合其他命令（如 `grep` 或 `awk`）可以進一步處理 `inotifywait` 的輸出。
- 在腳本中使用 `inotifywait` 時，可以考慮使用 `&` 將其放在背景運行，這樣可以同時執行其他任務。