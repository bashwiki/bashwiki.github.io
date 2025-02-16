# [Linux] Bash mknod 使用法: 創建特殊檔案

## Overview
`mknod` 命令用於創建特殊檔案，包括字符檔案和區塊檔案。這些檔案通常用於設備管理，允許用戶與硬體設備進行互動。

## Usage
基本語法如下：
```
mknod [選項] [檔案名稱] [類型] [主設備號] [次設備號]
```

## Common Options
- `-m, --mode`: 設定檔案的權限模式。
- `-Z, --context`: 設定 SELinux 上下文。
- `-h, --help`: 顯示幫助信息。

## Common Examples
1. 創建一個字符檔案：
   ```bash
   mknod /dev/mychar c 100 0
   ```
   這將創建一個名為 `mychar` 的字符檔案，主設備號為 100，次設備號為 0。

2. 創建一個區塊檔案：
   ```bash
   mknod /dev/myblock b 200 0
   ```
   這將創建一個名為 `myblock` 的區塊檔案，主設備號為 200，次設備號為 0。

3. 設定檔案權限：
   ```bash
   mknod -m 660 /dev/mydevice c 300 0
   ```
   這將創建一個字符檔案 `mydevice`，並設置權限為 660。

## Tips
- 確保你有足夠的權限來創建特殊檔案，通常需要 root 權限。
- 使用 `ls -l /dev` 查看已創建的特殊檔案及其屬性。
- 在創建設備檔案之前，確認主設備號和次設備號的正確性，以避免系統錯誤。