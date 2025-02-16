# [台灣] Bash test 使用法: 測試條件表達式

## Overview
`test` 命令用來評估條件表達式，並根據結果返回真或假。這在腳本中非常有用，特別是用於控制流程的判斷。

## Usage
基本語法如下：
```
test [options] [arguments]
```

## Common Options
- `-e FILE`：檢查檔案是否存在。
- `-d DIRECTORY`：檢查目錄是否存在。
- `-f FILE`：檢查檔案是否為普通檔案。
- `-z STRING`：檢查字串是否為空。
- `-n STRING`：檢查字串是否為非空。

## Common Examples
以下是一些常見的使用範例：

1. 檢查檔案是否存在：
   ```bash
   test -e myfile.txt && echo "檔案存在"
   ```

2. 檢查目錄是否存在：
   ```bash
   test -d mydirectory && echo "目錄存在"
   ```

3. 檢查檔案是否為普通檔案：
   ```bash
   test -f myfile.txt && echo "這是一個普通檔案"
   ```

4. 檢查字串是否為空：
   ```bash
   mystring=""
   test -z "$mystring" && echo "字串是空的"
   ```

5. 檢查字串是否為非空：
   ```bash
   mystring="Hello"
   test -n "$mystring" && echo "字串是非空的"
   ```

## Tips
- 使用 `[` 和 `]` 來代替 `test`，例如 `[` `-e myfile.txt` `]`，這在 Bash 中是等效的。
- 在使用條件判斷時，建議使用雙括號 `[[ ]]`，這樣可以避免某些字串處理的問題。
- 確保在使用變數時加上引號，以防止空字串或特殊字元造成的錯誤。