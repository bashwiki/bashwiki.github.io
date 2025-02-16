# [Linux] Bash unrar 使用方法: 解壓縮RAR檔案

## Overview
`unrar` 是一個用於解壓縮 RAR 檔案的命令行工具。它可以讓使用者輕鬆地提取 RAR 檔案中的內容。

## Usage
基本語法如下：
```bash
unrar [options] [arguments]
```

## Common Options
- `x`：解壓縮檔案到當前目錄。
- `e`：解壓縮檔案到當前目錄，但不保留目錄結構。
- `l`：列出 RAR 檔案中的內容。
- `t`：測試 RAR 檔案的完整性。
- `v`：顯示詳細的解壓縮過程。

## Common Examples
1. 解壓縮 RAR 檔案到當前目錄：
   ```bash
   unrar x archive.rar
   ```

2. 解壓縮 RAR 檔案到指定目錄：
   ```bash
   unrar x archive.rar /path/to/destination/
   ```

3. 列出 RAR 檔案中的內容：
   ```bash
   unrar l archive.rar
   ```

4. 測試 RAR 檔案的完整性：
   ```bash
   unrar t archive.rar
   ```

5. 解壓縮檔案而不保留目錄結構：
   ```bash
   unrar e archive.rar
   ```

## Tips
- 確保你已安裝 `unrar` 工具，否則命令將無法執行。
- 使用 `l` 選項來檢查檔案內容，這樣可以避免解壓縮不必要的檔案。
- 當解壓縮大型 RAR 檔案時，建議使用 `t` 選項先測試檔案的完整性，以確保沒有損壞。