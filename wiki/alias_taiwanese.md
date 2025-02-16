# [Linux] Bash alias 用法: 簡化命令輸入

## Overview
`alias` 命令用於創建命令的別名，讓使用者能夠用更簡單的方式執行常用的命令。透過這個命令，使用者可以自定義簡短的命令來替代較長或複雜的命令。

## Usage
基本語法如下：
```bash
alias [options] [arguments]
```

## Common Options
- `-p`：顯示所有當前的別名。
- `--help`：顯示幫助信息。

## Common Examples
以下是一些實用的別名示例：

1. 創建一個簡單的別名來更新系統：
   ```bash
   alias update='sudo apt update && sudo apt upgrade'
   ```

2. 創建一個別名來快速進入常用目錄：
   ```bash
   alias docs='cd ~/Documents'
   ```

3. 創建一個別名來顯示當前目錄的詳細列表：
   ```bash
   alias ll='ls -la'
   ```

4. 創建一個別名來清除終端屏幕：
   ```bash
   alias cls='clear'
   ```

## Tips
- 使用 `alias` 時，建議在 `.bashrc` 或 `.bash_profile` 文件中添加別名，以便每次啟動終端時自動加載。
- 選擇簡短且易於記憶的別名，這樣可以提高工作效率。
- 使用 `unalias [alias_name]` 來刪除不再需要的別名。