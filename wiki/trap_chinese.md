# [리눅스] Bash trap 사용법

## 概述
`trap` 命令用于在 Bash 脚本中捕获信号和其他事件，并在这些事件发生时执行指定的命令。它的主要目的是允许开发者在脚本中处理异常情况，例如清理临时文件、保存状态或优雅地终止程序。通过使用 `trap`，开发者可以确保脚本在接收到特定信号时能够执行必要的清理操作。

## 用法
`trap` 命令的基本语法如下：

```bash
trap COMMAND SIGNAL
```

- `COMMAND`：在接收到指定信号时要执行的命令。可以是单个命令或命令列表。
- `SIGNAL`：要捕获的信号名称或编号。常见的信号包括：
  - `SIGINT`（中断，通常由 Ctrl+C 触发）
  - `SIGTERM`（终止信号）
  - `EXIT`（脚本结束时触发）

可以使用多个信号来捕获，例如：

```bash
trap 'echo "Script terminated"; exit' SIGINT SIGTERM
```

## 示例
以下是使用 `trap` 命令的两个实际示例：

### 示例 1：捕获中断信号
```bash
#!/bin/bash

trap 'echo "Caught SIGINT, exiting..."; exit' SIGINT

while true; do
  echo "Running... (Press Ctrl+C to stop)"
  sleep 1
done
```
在这个示例中，当用户按下 Ctrl+C 时，脚本会捕获 `SIGINT` 信号并输出一条消息，然后优雅地退出。

### 示例 2：清理临时文件
```bash
#!/bin/bash

tempfile=$(mktemp)

trap 'rm -f "$tempfile"; echo "Temporary file removed."' EXIT

echo "Creating temporary file: $tempfile"
# 模拟一些操作
sleep 5
echo "Done with operations."
```
在这个示例中，脚本创建了一个临时文件，并在脚本结束时（无论是正常结束还是由于信号中断）删除该文件。

## 小贴士
- 使用 `trap` 捕获 `EXIT` 信号可以确保在脚本结束时执行清理操作，无论是正常结束还是由于错误。
- 在 `trap` 中使用双引号包围命令，以确保变量能够正确展开。
- 避免在 `trap` 中使用复杂的命令，保持命令简单明了，以减少错误的可能性。
- 在调试脚本时，可以使用 `trap 'commands' DEBUG` 来在每个命令执行前执行特定的命令，这对于跟踪脚本的执行过程非常有用。

通过合理使用 `trap` 命令，开发者可以提高脚本的健壮性和可维护性。