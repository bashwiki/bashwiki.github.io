# [台灣] Bash 7z 用法: 壓縮與解壓縮檔案

## Overview
7z 是一個強大的檔案壓縮和解壓縮工具，支援多種檔案格式。它能夠有效地減少檔案大小，並且提供高效的壓縮比。

## Usage
基本語法如下：
```
7z [options] [arguments]
```

## Common Options
- `a`: 添加檔案到壓縮檔案中。
- `x`: 解壓縮檔案。
- `t`: 指定檔案格式。
- `l`: 列出壓縮檔案中的檔案。
- `d`: 刪除壓縮檔案中的檔案。

## Common Examples
- 壓縮檔案：
  ```bash
  7z a archive.7z file1.txt file2.txt
  ```
- 解壓縮檔案：
  ```bash
  7z x archive.7z
  ```
- 列出壓縮檔案內容：
  ```bash
  7z l archive.7z
  ```
- 刪除壓縮檔案中的特定檔案：
  ```bash
  7z d archive.7z file1.txt
  ```

## Tips
- 使用 `-p` 選項來設置密碼，以保護壓縮檔案。
- 在壓縮大量檔案時，可以考慮使用 `-mx` 選項來調整壓縮等級，以獲得最佳性能。
- 定期檢查壓縮檔案的完整性，使用 `t` 選項來測試檔案是否損壞。