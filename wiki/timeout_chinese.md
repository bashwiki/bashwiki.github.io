# [Linux] Bash timeout 用法: 限制命令执行时间

## 概述
`timeout` 命令用于限制其他命令的执行时间。当指定的时间到达时，`timeout` 会终止正在运行的命令。这在需要防止某些命令运行过长时间时非常有用。

## 用法
基本语法如下：
```bash
timeout [选项] [时间] [命令] [参数]
```

## 常用选项
- `-s, --signal`: 指定发送给命令的信号，默认为 `TERM`。
- `--preserve-status`: 在命令被终止时保留其退出状态。
- `-k, --kill-after`: 在超时后，等待指定时间再发送信号。

## 常见示例
1. **限制命令执行时间为 5 秒**：
   ```bash
   timeout 5s sleep 10
   ```
   这个命令会尝试让 `sleep` 命令执行 10 秒，但由于 `timeout` 限制，它只会执行 5 秒。

2. **使用自定义信号终止命令**：
   ```bash
   timeout -s SIGKILL 5s sleep 10
   ```
   这里，`sleep` 命令将在 5 秒后被强制终止，使用 `SIGKILL` 信号。

3. **保留命令的退出状态**：
   ```bash
   timeout --preserve-status 5s false
   echo $?
   ```
   这个命令会执行 `false`，即使在 5 秒后被终止，退出状态仍然会保留。

4. **在超时后延迟发送信号**：
   ```bash
   timeout -k 2s 5s sleep 10
   ```
   该命令会在 5 秒后发送终止信号，但如果 `sleep` 仍在运行，它会在额外的 2 秒后强制终止。

## 提示
- 使用 `timeout` 时，确保选择合适的时间单位（如 `s`、`m`、`h`）。
- 在脚本中使用 `--preserve-status` 选项可以帮助你更好地处理命令的退出状态。
- 对于长时间运行的命令，考虑使用 `-k` 选项，以便在需要时强制终止。