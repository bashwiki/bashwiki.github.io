# [Linux] Bash timeout 用法: 限制命令執行時間

## Overview
`timeout` 命令用來限制其他命令的執行時間。如果指定的時間到達，`timeout` 會自動終止該命令，這對於防止某些命令無限期運行非常有用。

## Usage
基本語法如下：

```bash
timeout [options] [duration] [command] [arguments]
```

## Common Options
- `-k, --kill-after=DURATION`：在超過指定的時間後，強制終止命令。
- `-s, --signal=SIGNAL`：指定要發送的信號，預設為 `TERM`。
- `--preserve-status`：保留被終止命令的退出狀態。

## Common Examples
以下是一些實用的範例：

1. 限制命令執行時間為 5 秒：

   ```bash
   timeout 5s sleep 10
   ```

   這個命令會執行 `sleep 10`，但因為 `timeout` 限制在 5 秒內，命令會在 5 秒後被終止。

2. 使用 `-k` 選項強制終止命令：

   ```bash
   timeout -k 2s 5s sleep 10
   ```

   在這個例子中，`sleep 10` 會在 5 秒後被終止，然後在 2 秒後強制終止。

3. 指定信號來終止命令：

   ```bash
   timeout -s SIGKILL 5s sleep 10
   ```

   這會在 5 秒後使用 `SIGKILL` 信號終止 `sleep 10` 命令。

## Tips
- 使用 `timeout` 時，確保選擇合適的時間限制，以避免不必要的中斷。
- 當使用 `-k` 選項時，考慮到命令的清理工作，選擇合適的強制終止時間。
- 測試命令時，可以先使用較短的時間限制，以確保其行為符合預期。