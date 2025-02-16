# [Linux] Bash fgrep 用法: 搜尋固定字串

## Overview
fgrep 是一個用於搜尋固定字串的命令，通常用於在檔案中快速找到特定的文字，而不會進行正則表達式的解析。這使得 fgrep 在處理大量資料時特別有效率。

## Usage
基本語法如下：
```
fgrep [選項] [參數]
```

## Common Options
- `-i`：忽略大小寫。
- `-v`：反向搜尋，顯示不包含指定字串的行。
- `-c`：計算包含指定字串的行數。
- `-n`：在輸出中顯示行號。
- `-r`：遞迴搜尋目錄中的檔案。

## Common Examples
1. 在檔案中搜尋固定字串：
   ```bash
   fgrep "hello" filename.txt
   ```

2. 忽略大小寫進行搜尋：
   ```bash
   fgrep -i "hello" filename.txt
   ```

3. 計算包含特定字串的行數：
   ```bash
   fgrep -c "hello" filename.txt
   ```

4. 顯示行號：
   ```bash
   fgrep -n "hello" filename.txt
   ```

5. 遞迴搜尋目錄中的所有檔案：
   ```bash
   fgrep -r "hello" /path/to/directory
   ```

## Tips
- 使用 `-i` 選項可以讓搜尋更靈活，尤其是在不確定字母大小寫的情況下。
- 結合 `-v` 和 `-c` 可以快速了解哪些行不包含特定字串，這在資料篩選時非常有用。
- 當處理大量檔案時，考慮使用 `-r` 來提高效率，避免手動一個一個檔案搜尋。