# [台灣] Bash umask 用法: 設定檔案權限的預設值

## Overview
`umask` 命令用於設定新創建檔案和目錄的預設權限掩碼。這個命令可以幫助用戶控制檔案和目錄的可訪問性，確保只有授權的用戶能夠訪問或修改它們。

## Usage
基本語法如下：
```
umask [options] [arguments]
```

## Common Options
- `-S`：以符號形式顯示當前的 umask 值。
- `-p`：顯示當前的 umask 值，並且不改變它。

## Common Examples
1. **查看當前 umask 值**
   ```bash
   umask
   ```

2. **設定 umask 值為 022**
   ```bash
   umask 022
   ```
   這將使新創建的檔案擁有 644 的權限，目錄擁有 755 的權限。

3. **以符號形式顯示當前 umask 值**
   ```bash
   umask -S
   ```

4. **設定 umask 值為 007**
   ```bash
   umask 007
   ```
   這將使新創建的檔案和目錄的權限為 770，允許同組用戶訪問。

## Tips
- 在設定 umask 值時，請根據您的需求選擇合適的權限，以避免不必要的安全風險。
- 可以將 umask 設定添加到您的 shell 配置檔（如 `.bashrc` 或 `.bash_profile`）中，以便每次登錄時自動應用。
- 測試不同的 umask 值，了解其對檔案和目錄權限的影響，這樣可以更好地管理系統的安全性。