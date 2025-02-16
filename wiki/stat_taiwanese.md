# [Linux] Bash stat 使用法: 檔案狀態顯示

## Overview
`stat` 命令用於顯示檔案或檔案系統的詳細狀態資訊，包括檔案大小、權限、擁有者、修改時間等。

## Usage
基本語法如下：
```bash
stat [選項] [檔案]
```

## Common Options
- `-c`：自定義輸出格式。
- `-f`：顯示檔案系統的狀態。
- `--help`：顯示幫助信息。
- `--version`：顯示版本信息。

## Common Examples
1. 顯示檔案的狀態：
   ```bash
   stat filename.txt
   ```

2. 自定義輸出格式：
   ```bash
   stat -c '%s %n' filename.txt
   ```

3. 顯示檔案系統的狀態：
   ```bash
   stat -f /
   ```

4. 顯示多個檔案的狀態：
   ```bash
   stat file1.txt file2.txt
   ```

## Tips
- 使用 `-c` 選項可以自定義輸出格式，方便提取特定資訊。
- 當需要檢查多個檔案的狀態時，可以一次性列出檔案名稱，減少重複操作。
- 結合其他命令使用，例如 `grep`，可以過濾出特定的狀態信息。