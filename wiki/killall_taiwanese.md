# [Linux] Bash killall 使用法: 終止所有指定的程序

## Overview
`killall` 是一個用於終止系統中所有指定名稱的進程的命令。這個命令非常有用，當你需要快速終止多個相同名稱的進程時，無需逐一查找和終止。

## Usage
基本語法如下：
```
killall [選項] [進程名稱]
```

## Common Options
- `-u <用戶名>`: 只終止指定用戶擁有的進程。
- `-i`: 在終止進程之前顯示確認提示。
- `-q`: 在終止進程時不顯示任何錯誤消息。
- `-s <信號>`: 指定要發送的信號，預設為 `TERM` 信號。

## Common Examples
1. 終止所有名為 `firefox` 的進程：
   ```bash
   killall firefox
   ```

2. 終止所有名為 `python` 的進程，並顯示確認提示：
   ```bash
   killall -i python
   ```

3. 終止所有名為 `myapp` 的進程，並使用 `KILL` 信號：
   ```bash
   killall -s KILL myapp
   ```

4. 只終止用戶 `john` 擁有的所有 `ssh` 進程：
   ```bash
   killall -u john ssh
   ```

## Tips
- 使用 `-i` 選項可以避免意外終止重要進程，特別是在生產環境中。
- 在使用 `killall` 前，建議先使用 `pgrep` 命令確認進程名稱是否正確。
- 小心使用 `-s KILL`，因為這會強制終止進程，可能導致數據丟失。