# [台灣] Bash nohup 使用方法: 讓程序在登出後繼續運行

## Overview
`nohup` 是一個用於在登出後仍然保持程序運行的命令。它可以防止程序因為終端關閉而被終止，特別適合於長時間運行的任務。

## Usage
基本語法如下：
```
nohup [options] [arguments]
```

## Common Options
- `&`：將命令放在背景運行。
- `-h`：顯示幫助信息。
- `-p`：指定要運行的進程的 PID。

## Common Examples
1. 在背景運行一個腳本並將輸出重定向到 `output.log`：
   ```bash
   nohup ./my_script.sh > output.log 2>&1 &
   ```

2. 在登出後運行一個長時間的數據處理命令：
   ```bash
   nohup python data_processing.py &
   ```

3. 使用 `nohup` 來運行一個網頁伺服器：
   ```bash
   nohup python -m http.server 8000 &
   ```

## Tips
- 使用 `&` 將命令放在背景運行，可以讓你繼續使用終端。
- 確保將輸出重定向到文件，以便後續查看。
- 檢查 `nohup.out` 文件以獲取程序的標準輸出和錯誤信息，這是 `nohup` 的默認輸出文件。