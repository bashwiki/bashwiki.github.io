# [Linux] Bash tune2fs 使用法: 調整 ext2/ext3/ext4 檔案系統的參數

## Overview
`tune2fs` 是一個用於調整 ext2、ext3 和 ext4 檔案系統參數的命令。它允許使用者修改檔案系統的各種屬性，例如檔案系統的標籤、檔案系統檢查的頻率等。

## Usage
基本語法如下：
```bash
tune2fs [選項] [參數]
```

## Common Options
- `-L <label>`: 設定檔案系統的標籤。
- `-c <max-mount-count>`: 設定檔案系統在檢查之前可以掛載的最大次數。
- `-i <interval>`: 設定檔案系統檢查的時間間隔。
- `-O <feature>`: 啟用特定的檔案系統功能。
- `-E <extended-option>`: 設定擴展選項。

## Common Examples
1. 設定檔案系統標籤：
   ```bash
   tune2fs -L mylabel /dev/sda1
   ```

2. 設定最大掛載次數為 20：
   ```bash
   tune2fs -c 20 /dev/sda1
   ```

3. 設定檔案系統檢查的時間間隔為 30 天：
   ```bash
   tune2fs -i 30d /dev/sda1
   ```

4. 啟用檔案系統的某個功能（例如，ext_attr）：
   ```bash
   tune2fs -O ext_attr /dev/sda1
   ```

## Tips
- 在執行 `tune2fs` 命令之前，建議先備份重要資料，以防不測。
- 使用 `-l` 選項可以列印檔案系統的當前參數，這樣可以幫助你了解目前的設定。
- 確保在未掛載檔案系統的情況下使用 `tune2fs` 進行調整，以避免資料損壞。