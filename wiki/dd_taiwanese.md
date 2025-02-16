# [Linux] Bash dd 使用法: 複製和轉換檔案

## Overview
`dd` 是一個用於複製和轉換檔案的命令行工具。它可以用來進行低層次的檔案操作，特別是在處理磁碟映像和備份時非常有用。

## Usage
基本語法如下：
```bash
dd [options] [arguments]
```

## Common Options
- `if=`: 指定輸入檔案（input file）。
- `of=`: 指定輸出檔案（output file）。
- `bs=`: 設定讀取和寫入的區塊大小（block size）。
- `count=`: 指定要複製的區塊數量。
- `status=`: 控制輸出狀態信息的詳細程度。

## Common Examples
1. **複製檔案**
   ```bash
   dd if=input.txt of=output.txt
   ```
   這個命令將 `input.txt` 複製到 `output.txt`。

2. **創建磁碟映像**
   ```bash
   dd if=/dev/sda of=/path/to/disk_image.img bs=4M
   ```
   這個命令將整個磁碟 `/dev/sda` 複製到一個磁碟映像檔案。

3. **從檔案中提取特定大小的資料**
   ```bash
   dd if=input.txt of=output.txt bs=1M count=5
   ```
   這個命令將 `input.txt` 的前 5MB 複製到 `output.txt`。

4. **將檔案轉換為大寫**
   ```bash
   dd if=input.txt of=output.txt conv=ucase
   ```
   這個命令將 `input.txt` 的內容轉換為大寫並輸出到 `output.txt`。

## Tips
- 使用 `status=progress` 來顯示進度信息，這對於長時間的操作特別有用。
- 在進行磁碟操作時，請小心使用 `dd`，因為錯誤的命令可能會導致資料損失。
- 在執行之前，建議先使用 `sync` 命令來確保所有資料都已寫入磁碟。