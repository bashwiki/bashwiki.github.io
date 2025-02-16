# [Linux] Bash tee 使用法: 將輸出同時寫入檔案和標準輸出

## Overview
`tee` 命令用於將標準輸入的內容同時寫入檔案和標準輸出。這意味著你可以在終端中看到輸出的同時，將其保存到指定的檔案中。

## Usage
基本語法如下：
```bash
tee [options] [arguments]
```

## Common Options
- `-a`：以附加模式寫入檔案，而不是覆蓋。
- `-i`：忽略中斷信號。
- `--help`：顯示幫助信息。

## Common Examples
以下是一些常見的使用範例：

1. 將命令的輸出寫入檔案並顯示在終端：
   ```bash
   echo "Hello, World!" | tee output.txt
   ```

2. 將多個檔案的內容合併並寫入新檔案：
   ```bash
   cat file1.txt file2.txt | tee combined.txt
   ```

3. 使用附加模式將輸出追加到已存在的檔案：
   ```bash
   echo "Another line" | tee -a output.txt
   ```

4. 將錯誤輸出也寫入檔案：
   ```bash
   command 2>&1 | tee error_log.txt
   ```

## Tips
- 使用 `-a` 選項可以避免覆蓋檔案，這在日誌記錄時特別有用。
- 結合 `grep` 和 `tee` 可以在過濾輸出時同時保存結果：
  ```bash
  ps aux | grep bash | tee bash_processes.txt
  ```
- 如果你需要在腳本中使用 `tee`，可以考慮將其與其他管道命令結合，以提高效率。