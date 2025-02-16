# [Linux] Bash su 使用方式: 切換使用者

## Overview
`su` 命令用於在 Linux 系統中切換使用者。當你需要以不同的使用者身份執行命令時，這個命令非常有用，特別是當你需要以 root 使用者的權限執行某些操作時。

## Usage
基本語法如下：

```bash
su [options] [username]
```

如果不指定使用者名稱，預設會切換到 root 使用者。

## Common Options
- `-l` 或 `--login`: 以登入方式切換使用者，這會加載該使用者的環境變數。
- `-c`: 執行指定的命令，然後退出。
- `-s`: 指定要使用的 shell。

## Common Examples
1. 切換到 root 使用者：
   ```bash
   su
   ```

2. 切換到指定的使用者（例如 user1）：
   ```bash
   su user1
   ```

3. 以登入方式切換到 user1：
   ```bash
   su -l user1
   ```

4. 執行一個命令（例如 `ls`）並返回：
   ```bash
   su -c "ls" user1
   ```

5. 使用指定的 shell 切換到 user1：
   ```bash
   su -s /bin/bash user1
   ```

## Tips
- 使用 `su -` 而不是 `su` 可以確保你獲得完整的環境設置。
- 當需要執行單個命令時，使用 `-c` 參數可以避免完全切換使用者。
- 確保你有權限使用 `su` 命令，通常需要知道目標使用者的密碼。