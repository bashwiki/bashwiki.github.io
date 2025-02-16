# [Linux] Bash unxz 使用法: 解壓縮 .xz 檔案

## Overview
`unxz` 是一個用於解壓縮 `.xz` 格式檔案的命令行工具。它可以將壓縮的檔案還原為原始的未壓縮狀態，方便用戶存取和使用。

## Usage
基本語法如下：
```
unxz [選項] [檔案]
```

## Common Options
- `-k`：保留原始的壓縮檔案。
- `-f`：強制解壓縮，即使檔案已經存在。
- `-v`：顯示詳細的解壓縮過程。

## Common Examples
以下是一些常見的使用範例：

1. 解壓縮單個檔案：
   ```bash
   unxz example.xz
   ```

2. 解壓縮並保留原始檔案：
   ```bash
   unxz -k example.xz
   ```

3. 強制解壓縮已存在的檔案：
   ```bash
   unxz -f example.xz
   ```

4. 顯示解壓縮過程：
   ```bash
   unxz -v example.xz
   ```

## Tips
- 在使用 `unxz` 前，確保你有足夠的磁碟空間來存放解壓縮後的檔案。
- 如果你不確定檔案的格式，可以使用 `file` 命令來檢查檔案類型。
- 使用 `-k` 選項可以避免意外刪除原始檔案，特別是在處理重要檔案時。