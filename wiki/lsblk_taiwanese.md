# [Linux] Bash lsblk 使用方法: 列出區塊設備

## Overview
`lsblk` 是一個用於列出系統中所有區塊設備的命令，包括硬碟、分割區和其他儲存裝置。它顯示這些設備的層級結構和相關資訊，幫助使用者了解系統的儲存配置。

## Usage
基本語法如下：
```bash
lsblk [options] [arguments]
```

## Common Options
- `-a`：顯示所有設備，包括空的設備。
- `-f`：顯示文件系統類型和標籤。
- `-l`：以列表形式顯示設備，而不是樹狀結構。
- `-o`：自訂輸出欄位，可以選擇顯示的資訊。
- `-p`：顯示完整的設備路徑。

## Common Examples
1. 列出所有區塊設備：
   ```bash
   lsblk
   ```

2. 顯示所有設備，包括空的設備：
   ```bash
   lsblk -a
   ```

3. 顯示設備的文件系統類型和標籤：
   ```bash
   lsblk -f
   ```

4. 以列表形式顯示設備：
   ```bash
   lsblk -l
   ```

5. 自訂輸出顯示設備名稱和大小：
   ```bash
   lsblk -o NAME,SIZE
   ```

## Tips
- 使用 `lsblk -f` 可以快速查看每個設備的文件系統類型，這對於管理磁碟非常有幫助。
- 結合 `grep` 使用可以過濾出特定設備，例如：
  ```bash
  lsblk | grep sda
  ```
- 定期檢查區塊設備的狀態有助於預防資料遺失或系統故障。