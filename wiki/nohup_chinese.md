# [Linux] Bash nohup 用法: 使进程在退出终端后继续运行

## 概述
`nohup` 命令用于在用户退出终端后继续运行指定的命令。它可以防止进程因终端关闭而被终止，常用于长时间运行的任务。

## 用法
基本语法如下：
```bash
nohup [选项] [命令] [参数] &
```

## 常用选项
- `&`：将命令放入后台执行。
- `-h`：显示帮助信息。
- `-p`：用于指定进程的 PID。

## 常见示例
1. 在后台运行一个脚本，并将输出重定向到 `output.log` 文件：
   ```bash
   nohup ./long_running_script.sh > output.log &
   ```

2. 运行一个 Python 脚本并忽略终端关闭：
   ```bash
   nohup python3 my_script.py &
   ```

3. 使用 `nohup` 运行一个命令并查看输出：
   ```bash
   nohup ls -l > list_output.txt &
   ```

## 提示
- 确保在命令末尾加上 `&`，以便将其放入后台运行。
- 输出重定向是一个好习惯，可以帮助你查看程序的运行结果。
- 使用 `jobs` 命令可以查看当前后台运行的任务。