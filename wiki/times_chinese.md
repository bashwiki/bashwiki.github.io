# [Linux] Bash times 使用方法: 显示命令执行时间

## 概述
`times` 命令用于显示当前 shell 会话中各个命令的执行时间，包括用户时间、系统时间和总时间。这对于性能分析和优化脚本非常有用。

## 用法
基本语法如下：
```
times [options] [arguments]
```

## 常用选项
- `-p`：以 POSIX 格式输出时间。

## 常见示例
1. **查看当前 shell 会话的执行时间**
   ```bash
   times
   ```

2. **使用 `-p` 选项以 POSIX 格式输出**
   ```bash
   times -p
   ```

3. **在执行多个命令后查看时间**
   ```bash
   sleep 1
   ls
   times
   ```

4. **在脚本中使用 `times`**
   ```bash
   #!/bin/bash
   echo "开始执行"
   sleep 2
   echo "执行完成"
   times
   ```

## 提示
- 在长时间运行的脚本中，定期使用 `times` 可以帮助你监控性能。
- 结合其他命令使用，例如 `time` 命令，可以更详细地分析特定命令的执行时间。