# [Linux] Bash kill 使用方法: 終止進程

## Overview
`kill` 命令用於終止正在運行的進程。它可以根據進程的 ID (PID) 發送信號，通常用於停止或重啟應用程序。

## Usage
基本語法如下：
```
kill [options] [arguments]
```

## Common Options
- `-l`：列出所有可用的信號名稱。
- `-s SIGNAL`：指定要發送的信號，可以用信號名稱或數字表示。
- `-n`：根據信號編號發送信號。

## Common Examples
- 終止特定進程：
  ```bash
  kill 1234
  ```
  這裡 `1234` 是進程的 PID。

- 使用信號名稱終止進程：
  ```bash
  kill -s TERM 1234
  ```
  這會發送 `TERM` 信號給 PID 為 `1234` 的進程。

- 列出所有可用的信號：
  ```bash
  kill -l
  ```

- 強制終止進程：
  ```bash
  kill -9 1234
  ```
  使用 `-9` 參數可以強制終止進程，這是一個不會被捕獲的信號。

## Tips
- 確保在使用 `kill` 命令時確認進程的 PID，以避免終止錯誤的進程。
- 使用 `killall` 命令可以根據進程名稱終止所有相同名稱的進程，例如：
  ```bash
  killall firefox
  ```
- 在終止進程之前，考慮使用 `ps` 命令檢查進程狀態，以確保你終止的是正確的進程。