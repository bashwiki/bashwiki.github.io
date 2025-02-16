# [Linux] Bash unzip 用法: 解壓縮檔案

## Overview
`unzip` 命令用於解壓縮 ZIP 格式的檔案。它能夠將壓縮的檔案還原為原始檔案，方便用戶訪問和使用。

## Usage
基本語法如下：
```
unzip [選項] [檔案]
```

## Common Options
- `-d [目錄]`：指定解壓縮的目錄。
- `-l`：列出 ZIP 檔案中的內容，但不進行解壓縮。
- `-o`：自動覆蓋已存在的檔案而不提示。
- `-q`：靜默模式，減少輸出信息。

## Common Examples
1. 解壓縮檔案到當前目錄：
   ```bash
   unzip file.zip
   ```

2. 解壓縮檔案到指定目錄：
   ```bash
   unzip file.zip -d /path/to/directory
   ```

3. 列出 ZIP 檔案的內容：
   ```bash
   unzip -l file.zip
   ```

4. 自動覆蓋已存在的檔案：
   ```bash
   unzip -o file.zip
   ```

5. 靜默解壓縮檔案：
   ```bash
   unzip -q file.zip
   ```

## Tips
- 在解壓縮之前，使用 `unzip -l` 檢查檔案內容，以避免不必要的覆蓋。
- 使用 `-d` 選項時，確保目錄存在，否則命令將失敗。
- 如果檔案受密碼保護，使用 `unzip` 時會提示輸入密碼。