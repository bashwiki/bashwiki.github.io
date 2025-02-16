# [Linux] Bash mkfs 使用法: 創建檔案系統

## Overview
`mkfs` 命令用於在磁碟或分割區上創建檔案系統。這是一個非常重要的工具，因為它為數據存儲提供了結構，使得操作系統能夠讀取和寫入數據。

## Usage
基本語法如下：
```
mkfs [選項] [參數]
```

## Common Options
- `-t`：指定檔案系統類型，例如 `ext4`、`vfat` 等。
- `-L`：為檔案系統指定標籤。
- `-n`：不執行實際的格式化，只顯示將要執行的命令。
- `-V`：顯示版本信息。

## Common Examples
1. 創建一個 `ext4` 檔案系統：
   ```bash
   mkfs -t ext4 /dev/sdX1
   ```

2. 創建一個 `vfat` 檔案系統並指定標籤：
   ```bash
   mkfs -t vfat -L MY_USB /dev/sdX1
   ```

3. 顯示將要執行的命令，不執行格式化：
   ```bash
   mkfs -n -t ext4 /dev/sdX1
   ```

4. 創建一個 `xfs` 檔案系統：
   ```bash
   mkfs -t xfs /dev/sdX1
   ```

## Tips
- 在執行 `mkfs` 之前，請確保備份所有重要數據，因為格式化將刪除所有現有數據。
- 使用 `-n` 選項可以在不執行格式化的情況下檢查命令是否正確。
- 確保選擇正確的磁碟或分割區，以避免意外格式化錯誤的設備。