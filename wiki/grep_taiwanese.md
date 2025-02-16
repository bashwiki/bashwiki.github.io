# [台灣] Bash grep 用法: 搜尋文本中的模式

## Overview
`grep` 是一個強大的命令行工具，用於在文本中搜尋特定的模式或字串。它可以從檔案或標準輸入中過濾出符合條件的行，並顯示出來。

## Usage
基本語法如下：
```
grep [選項] [參數]
```

## Common Options
- `-i`: 忽略大小寫。
- `-v`: 顯示不符合模式的行。
- `-r`: 遞迴搜尋目錄中的檔案。
- `-n`: 顯示行號。
- `-l`: 只顯示包含匹配模式的檔案名稱。

## Common Examples
1. **基本搜尋**
   ```bash
   grep "hello" file.txt
   ```
   這會在 `file.txt` 中搜尋包含 "hello" 的行。

2. **忽略大小寫**
   ```bash
   grep -i "hello" file.txt
   ```
   這會搜尋 "hello"、"Hello"、"HELLO" 等不區分大小寫的匹配。

3. **遞迴搜尋**
   ```bash
   grep -r "hello" /path/to/directory
   ```
   這會在指定目錄及其子目錄中搜尋 "hello"。

4. **顯示行號**
   ```bash
   grep -n "hello" file.txt
   ```
   這會在搜尋結果中顯示匹配行的行號。

5. **顯示不匹配的行**
   ```bash
   grep -v "hello" file.txt
   ```
   這會顯示不包含 "hello" 的所有行。

## Tips
- 使用 `-r` 選項時，注意搜尋的目錄大小，避免搜尋過多不必要的檔案。
- 結合管道使用 `grep` 可以進行更複雜的文本處理，例如：
  ```bash
  cat file.txt | grep "hello"
  ```
- 對於大型檔案，考慮使用 `-m` 選項限制輸出行數，以提高效率。