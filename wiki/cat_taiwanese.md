# [Linux] Bash cat 使用法: 顯示或合併檔案內容

## Overview
`cat` 命令是用來顯示檔案內容、合併檔案或創建新檔案的工具。它的名稱來自於 "concatenate" 的縮寫，主要功能是將檔案的內容串接起來。

## Usage
基本語法如下：
```bash
cat [選項] [檔案]
```

## Common Options
- `-n`：為每一行編號。
- `-b`：為非空行編號。
- `-E`：在每行的結尾顯示 `$` 符號。
- `-s`：壓縮連續的空行為一行。

## Common Examples
1. 顯示檔案內容：
   ```bash
   cat filename.txt
   ```

2. 合併多個檔案並顯示：
   ```bash
   cat file1.txt file2.txt
   ```

3. 將檔案內容輸出到新檔案：
   ```bash
   cat file1.txt > newfile.txt
   ```

4. 使用選項編號每一行：
   ```bash
   cat -n filename.txt
   ```

5. 壓縮空行：
   ```bash
   cat -s filename.txt
   ```

## Tips
- 使用 `cat` 時，若檔案非常大，建議搭配 `less` 或 `more` 命令，以便於瀏覽。
- 當合併檔案時，確保檔案的順序正確，因為 `cat` 會依照提供的順序顯示內容。
- 使用 `>>` 來追加內容到檔案，而不是覆蓋：
   ```bash
   cat file1.txt >> existingfile.txt
   ```