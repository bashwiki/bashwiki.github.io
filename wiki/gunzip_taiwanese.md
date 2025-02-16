# [台灣] Bash gunzip 使用法: 解壓縮.gz 檔案

## Overview
`gunzip` 是一個用於解壓縮 `.gz` 格式檔案的命令。它可以將壓縮的檔案還原為原始的未壓縮狀態，方便用戶存取和使用檔案內容。

## Usage
基本語法如下：
```
gunzip [選項] [檔案]
```

## Common Options
- `-c`: 將解壓縮的內容輸出到標準輸出，而不改變原始檔案。
- `-f`: 強制解壓縮，即使檔案已經存在。
- `-k`: 保留原始的壓縮檔案。
- `-v`: 顯示解壓縮過程中的詳細資訊。

## Common Examples
以下是一些常見的 `gunzip` 使用範例：

1. 解壓縮單一檔案：
   ```bash
   gunzip example.gz
   ```

2. 解壓縮並保留原始檔案：
   ```bash
   gunzip -k example.gz
   ```

3. 將解壓縮的內容輸出到標準輸出：
   ```bash
   gunzip -c example.gz > output.txt
   ```

4. 強制解壓縮已存在的檔案：
   ```bash
   gunzip -f example.gz
   ```

5. 顯示解壓縮過程的詳細資訊：
   ```bash
   gunzip -v example.gz
   ```

## Tips
- 在解壓縮大型檔案時，使用 `-v` 選項可以幫助你了解進度。
- 如果你需要保留原始檔案，記得使用 `-k` 選項。
- 當處理多個檔案時，可以一次性解壓縮多個 `.gz` 檔案，例如：
  ```bash
  gunzip file1.gz file2.gz file3.gz
  ```