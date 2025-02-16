# [Linux] Bash find 使用法: 尋找檔案名稱

## Overview
`find` 命令用於在目錄樹中搜尋符合特定條件的檔案和目錄。它可以根據名稱、大小、修改時間等多種條件進行搜尋，並且可以執行指定的操作。

## Usage
基本語法如下：
```
find [選項] [參數]
```

## Common Options
- `-name <pattern>`: 根據檔案名稱模式搜尋。
- `-type <type>`: 根據檔案類型搜尋，例如 `f` 代表檔案，`d` 代表目錄。
- `-size <n>`: 根據檔案大小搜尋，`n` 可以是數字加上單位（如 `k`、`M`、`G`）。
- `-mtime <n>`: 根據檔案的修改時間搜尋，`n` 可以是正數或負數。
- `-exec <command> {} \;`: 對找到的每個檔案執行指定的命令。

## Common Examples
1. 根據名稱搜尋檔案：
   ```bash
   find /path/to/search -name "example.txt"
   ```

2. 搜尋所有的目錄：
   ```bash
   find /path/to/search -type d
   ```

3. 搜尋大於 10MB 的檔案：
   ```bash
   find /path/to/search -size +10M
   ```

4. 搜尋最近 7 天內修改過的檔案：
   ```bash
   find /path/to/search -mtime -7
   ```

5. 對找到的檔案執行命令，例如刪除：
   ```bash
   find /path/to/search -name "*.tmp" -exec rm {} \;
   ```

## Tips
- 使用 `-iname` 來進行不區分大小寫的名稱搜尋。
- 結合 `-print` 選項可以顯示找到的檔案。
- 在使用 `-exec` 時，確保命令結尾有 `\;`，以避免語法錯誤。