# [Linux] Bash trap 用法: 捕获信号和清理资源

## 概述
`trap` 命令用于捕获和处理信号，允许用户在脚本中定义在接收到特定信号时要执行的命令。这对于在脚本中进行清理操作或处理意外中断非常有用。

## 用法
基本语法如下：
```bash
trap [options] [commands] [signals]
```

## 常用选项
- `-l`：列出所有可用的信号名称。
- `-p`：打印当前的 trap 设置。
- `signals`：可以指定一个或多个信号，例如 `SIGINT`、`SIGTERM` 等。

## 常见示例

1. **捕获 SIGINT 信号**
   ```bash
   trap 'echo "脚本被中断"; exit' SIGINT
   while true; do
       echo "运行中... (按 Ctrl+C 退出)"
       sleep 1
   done
   ```

2. **在退出时清理临时文件**
   ```bash
   trap 'rm -f /tmp/tempfile; echo "临时文件已删除"' EXIT
   touch /tmp/tempfile
   echo "创建了临时文件..."
   ```

3. **捕获多个信号**
   ```bash
   trap 'echo "接收到 SIGTERM"; exit' SIGTERM
   trap 'echo "接收到 SIGHUP"; exit' SIGHUP
   while true; do
       sleep 1
   done
   ```

## 小贴士
- 在使用 `trap` 时，确保在脚本的开始部分设置信号处理，这样可以确保在脚本运行期间能够捕获信号。
- 使用 `EXIT` 信号可以在脚本结束时执行清理操作，无论是正常结束还是由于信号中断。
- 通过 `trap -p` 可以查看当前的 trap 设置，便于调试和确认。

使用 `trap` 命令可以让你的 Bash 脚本更加健壮和灵活，能够有效处理各种信号和异常情况。