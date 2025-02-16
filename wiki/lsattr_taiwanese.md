# [台灣] Bash lsattr 用法: 查詢檔案屬性

## Overview
`lsattr` 是一個用於顯示檔案或目錄的屬性命令。它可以幫助使用者了解檔案的安全性和可修改性，特別是在 Linux 系統中。

## Usage
基本語法如下：
```bash
lsattr [options] [arguments]
```

## Common Options
- `-a`：顯示所有檔案，包括以點開頭的隱藏檔案。
- `-d`：顯示目錄的屬性，而不是其內容。
- `-R`：遞迴顯示目錄及其子目錄的檔案屬性。

## Common Examples
1. 顯示當前目錄下所有檔案的屬性：
   ```bash
   lsattr
   ```

2. 顯示包括隱藏檔案的屬性：
   ```bash
   lsattr -a
   ```

3. 顯示特定檔案的屬性，例如 `example.txt`：
   ```bash
   lsattr example.txt
   ```

4. 遞迴顯示某個目錄及其子目錄的檔案屬性，例如 `my_folder`：
   ```bash
   lsattr -R my_folder
   ```

## Tips
- 使用 `lsattr` 可以幫助您識別哪些檔案具有特殊屬性，如不可刪除或不可修改。
- 結合 `lsattr` 與 `grep` 可以快速查找特定屬性的檔案，例如：
  ```bash
  lsattr | grep '^i'
  ```
- 定期檢查檔案屬性可以增強系統的安全性，特別是在多用戶環境中。