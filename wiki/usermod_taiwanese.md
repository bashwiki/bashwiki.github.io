# [Linux] Bash usermod 使用法: 用於修改用戶帳號的屬性

## Overview
`usermod` 命令用於修改現有用戶帳號的屬性。這包括更改用戶的群組、主目錄、登錄名稱等。這個命令通常需要管理員權限來執行。

## Usage
基本語法如下：
```
usermod [選項] [用戶名]
```

## Common Options
- `-aG`：將用戶添加到指定的附加群組中，而不會移除其現有的群組。
- `-d`：指定用戶的新主目錄。
- `-l`：更改用戶的登錄名稱。
- `-g`：指定用戶的主要群組。
- `-s`：指定用戶的登錄殼（shell）。

## Common Examples
- 將用戶 `john` 添加到 `sudo` 群組：
  ```bash
  sudo usermod -aG sudo john
  ```

- 更改用戶 `mary` 的主目錄為 `/home/mary_new`：
  ```bash
  sudo usermod -d /home/mary_new mary
  ```

- 更改用戶 `alice` 的登錄名稱為 `alice_new`：
  ```bash
  sudo usermod -l alice_new alice
  ```

- 將用戶 `bob` 的主要群組更改為 `developers`：
  ```bash
  sudo usermod -g developers bob
  ```

- 更改用戶 `charlie` 的登錄殼為 `/bin/zsh`：
  ```bash
  sudo usermod -s /bin/zsh charlie
  ```

## Tips
- 在使用 `usermod` 命令時，務必小心，因為不當的更改可能會導致用戶無法登錄。
- 使用 `-aG` 選項時，確保在添加用戶到新群組時不會移除其現有的群組。
- 在更改用戶屬性後，建議檢查用戶的設置是否正確，以確保系統的正常運行。