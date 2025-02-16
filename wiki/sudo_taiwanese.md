# [Linux] Bash sudo 使用法: 提升權限執行命令

## Overview
`sudo` 是一個用於在 Unix 和 Linux 系統中以超級用戶（root）身份執行命令的工具。它允許授權的用戶在不需要切換到 root 帳戶的情況下，執行需要更高權限的操作。

## Usage
基本語法如下：
```
sudo [options] [arguments]
```

## Common Options
- `-u [user]`：指定以哪個用戶的身份執行命令，預設為 root。
- `-k`：使 sudo 忘記用戶的密碼，強制下次執行時重新輸入密碼。
- `-l`：列出當前用戶可以執行的命令。
- `-i`：以指定用戶的環境執行命令，類似於登入該用戶。

## Common Examples
1. 以 root 身份更新系統：
   ```bash
   sudo apt update
   ```

2. 安裝一個軟體包：
   ```bash
   sudo apt install package_name
   ```

3. 以其他用戶身份執行命令：
   ```bash
   sudo -u username command
   ```

4. 列出可執行的命令：
   ```bash
   sudo -l
   ```

5. 以 root 環境執行一個 shell：
   ```bash
   sudo -i
   ```

## Tips
- 使用 `sudo` 時，請確保你知道你正在執行的命令，以避免不小心更改系統設置。
- 定期檢查 `/etc/sudoers` 文件，確保只有授權用戶可以使用 `sudo`。
- 使用 `-k` 選項在不再需要權限時，及時清除 sudo 的密碼記錄。