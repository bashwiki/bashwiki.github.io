# [Linux] Bash cp 使用法: 複製檔案和目錄

## Overview
`cp` 命令用於在 Linux 系統中複製檔案和目錄。它可以將一個或多個檔案從一個位置複製到另一個位置，並且可以選擇保留檔案的屬性。

## Usage
基本語法如下：
```bash
cp [選項] [來源] [目標]
```

## Common Options
- `-r`：遞迴複製目錄及其內容。
- `-i`：在覆蓋檔案之前提示用戶確認。
- `-u`：僅在來源檔案較新或目標檔案不存在時才複製。
- `-v`：顯示詳細的複製過程。

## Common Examples
1. 複製單個檔案：
   ```bash
   cp file1.txt file2.txt
   ```
   這會將 `file1.txt` 複製為 `file2.txt`。

2. 複製目錄及其內容：
   ```bash
   cp -r myfolder/ newfolder/
   ```
   這會將 `myfolder` 及其所有內容複製到 `newfolder`。

3. 在覆蓋檔案之前進行確認：
   ```bash
   cp -i file1.txt file2.txt
   ```
   如果 `file2.txt` 已存在，系統會提示用戶確認是否覆蓋。

4. 僅在來源檔案較新時複製：
   ```bash
   cp -u file1.txt file2.txt
   ```
   這會在 `file1.txt` 比 `file2.txt` 新或 `file2.txt` 不存在時進行複製。

## Tips
- 使用 `-v` 選項可以幫助你了解正在複製哪些檔案，特別是在處理大量檔案時。
- 在複製重要檔案時，考慮使用 `-i` 選項以避免意外覆蓋。
- 當複製目錄時，務必使用 `-r` 選項，否則命令將無法執行。