# [Linux] Bash users 使用法: 列出系統使用者

## Overview
`users` 命令用於顯示當前登入系統的所有使用者名稱。這個命令非常簡單，主要用於快速查看哪些使用者正在使用系統。

## Usage
基本語法如下：
```bash
users [options]
```

## Common Options
- `-u`：顯示使用者的登入時間。
- `-r`：顯示目前登入的使用者數量。

## Common Examples
以下是一些常見的使用範例：

1. 顯示當前登入的所有使用者：
   ```bash
   users
   ```

2. 顯示當前登入的使用者及其登入時間：
   ```bash
   users -u
   ```

3. 顯示目前登入的使用者數量：
   ```bash
   users -r
   ```

## Tips
- 使用 `who` 命令可以獲得更詳細的使用者資訊，包括使用者的登入時間和來源。
- 若要定期監控系統使用者，可以將 `users` 命令與其他命令結合使用，例如 `watch`，以每幾秒更新一次顯示：
  ```bash
  watch users
  ```