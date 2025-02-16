# [Linux] Bash gzip 使用方法: 壓縮和解壓縮檔案

## Overview
`gzip` 是一個用於壓縮和解壓縮檔案的命令行工具。它使用 Lempel-Ziv 算法來減少檔案的大小，特別適合文本檔案。壓縮後的檔案通常以 `.gz` 為副檔名。

## Usage
基本語法如下：
```
gzip [options] [arguments]
```

## Common Options
- `-d` 或 `--decompress`: 解壓縮檔案。
- `-k` 或 `--keep`: 在壓縮時保留原始檔案。
- `-v` 或 `--verbose`: 顯示詳細的壓縮過程。
- `-r` 或 `--recursive`: 遞迴壓縮目錄中的所有檔案。

## Common Examples
1. 壓縮檔案：
   ```bash
   gzip myfile.txt
   ```
   這會將 `myfile.txt` 壓縮為 `myfile.txt.gz`。

2. 解壓縮檔案：
   ```bash
   gzip -d myfile.txt.gz
   ```
   這會將 `myfile.txt.gz` 解壓縮回 `myfile.txt`。

3. 保留原始檔案：
   ```bash
   gzip -k myfile.txt
   ```
   這會壓縮 `myfile.txt`，但原始檔案仍然會保留。

4. 遞迴壓縮目錄：
   ```bash
   gzip -r mydirectory/
   ```
   這會壓縮 `mydirectory` 目錄中的所有檔案。

5. 顯示詳細資訊：
   ```bash
   gzip -v myfile.txt
   ```
   這會在壓縮時顯示詳細的進度資訊。

## Tips
- 在壓縮大量檔案時，考慮使用 `-r` 選項來簡化操作。
- 使用 `-k` 選項可以避免意外刪除原始檔案。
- 定期檢查壓縮檔案的完整性，特別是在長期存儲時。