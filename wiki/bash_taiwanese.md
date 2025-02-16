# [台灣] Bash bash 用法: 執行命令的解釋

## Overview
Bash 是一種 Unix Shell，主要用於執行命令和腳本。它提供了一個命令行介面，讓使用者可以與作業系統互動，執行各種操作。

## Usage
基本語法如下：
```bash
bash [options] [arguments]
```

## Common Options
- `-c`: 從字串執行命令。
- `-i`: 進入互動模式。
- `-l`: 啟動一個登入的 shell。
- `-s`: 從標準輸入讀取命令。

## Common Examples
1. 執行一個簡單的命令：
   ```bash
   bash -c "echo Hello, World!"
   ```

2. 進入互動模式：
   ```bash
   bash -i
   ```

3. 從檔案執行命令：
   ```bash
   bash script.sh
   ```

4. 從標準輸入執行命令：
   ```bash
   echo "echo Hello from stdin" | bash -s
   ```

## Tips
- 使用 `bash -i` 可以進行即時命令測試，方便調試。
- 確保腳本檔案有執行權限，使用 `chmod +x script.sh` 來設置。
- 使用 `bash -l` 來模擬登入環境，這對於測試環境變數非常有用。