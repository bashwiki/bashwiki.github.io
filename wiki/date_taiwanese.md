# [臺灣] Bash date 使用法: 取得和格式化日期與時間

## Overview
`date` 命令用於顯示和格式化當前的日期和時間。它可以根據用戶的需求，顯示不同格式的日期和時間，並且還可以用來設置系統的日期和時間。

## Usage
基本語法如下：
```
date [options] [arguments]
```

## Common Options
- `+FORMAT`：自定義輸出格式。例如，`+%Y-%m-%d` 會顯示為 "2023-10-01"。
- `-u`：顯示協調世界時間（UTC）。
- `-d STRING`：顯示指定日期的時間。例如，`-d "next Friday"` 會顯示下個星期五的日期。
- `-s STRING`：設置系統的日期和時間。

## Common Examples
1. 顯示當前日期和時間：
   ```bash
   date
   ```

2. 顯示自定義格式的日期：
   ```bash
   date "+%Y-%m-%d %H:%M:%S"
   ```

3. 顯示協調世界時間：
   ```bash
   date -u
   ```

4. 顯示下個星期五的日期：
   ```bash
   date -d "next Friday"
   ```

5. 設置系統日期和時間（需要管理員權限）：
   ```bash
   sudo date -s "2023-10-01 12:00:00"
   ```

## Tips
- 使用 `date` 命令時，建議先使用 `date` 命令確認當前時間，然後再進行設置，以避免錯誤。
- 可以將常用的日期格式保存到別名中，方便快速使用。例如：
  ```bash
  alias today='date "+%Y-%m-%d"'
  ```
- 在腳本中使用 `date` 時，確保使用正確的格式，以便於日誌記錄和時間戳的生成。