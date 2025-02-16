# [台灣] Bash pkill 用法: 終止進程的命令

## Overview
`pkill` 命令用於根據進程名稱終止正在運行的進程。這個命令非常有用，當你知道進程的名稱但不知道其進程ID時，可以輕鬆地終止該進程。

## Usage
基本語法如下：
```bash
pkill [選項] [參數]
```

## Common Options
- `-f`：根據完整的命令行來匹配進程。
- `-n`：終止最新啟動的進程。
- `-o`：終止最早啟動的進程。
- `-signal`：發送指定的信號（預設為 TERM）。
- `-u`：根據用戶來匹配進程。

## Common Examples
1. 終止所有名為 `firefox` 的進程：
   ```bash
   pkill firefox
   ```

2. 終止所有名為 `python` 的進程，並發送 `SIGKILL` 信號：
   ```bash
   pkill -9 python
   ```

3. 根據完整命令行終止進程，假設命令行包含 `my_script.py`：
   ```bash
   pkill -f my_script.py
   ```

4. 終止最新啟動的 `java` 進程：
   ```bash
   pkill -n java
   ```

5. 根據用戶終止所有 `nginx` 進程：
   ```bash
   pkill -u www-data nginx
   ```

## Tips
- 在使用 `pkill` 前，可以使用 `pgrep` 命令來確認將要終止的進程，這樣可以避免意外終止錯誤的進程。
- 使用 `-n` 和 `-o` 選項時，請確保你清楚你要終止的是最新或最早的進程，以免影響系統運行。
- 在生產環境中，謹慎使用 `pkill`，特別是當你使用 `-9` 信號時，因為它會強制終止進程，可能導致數據丟失。