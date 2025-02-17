# [Linux] Bash inotifywait 使用方法: 监控文件系统事件

## 概述
`inotifywait` 是一个用于监控 Linux 文件系统事件的命令行工具。它可以实时监测文件或目录的变化，如文件的创建、删除、修改等，并在发生这些事件时输出相应的信息。

## 用法
基本语法如下：
```bash
inotifywait [options] [arguments]
```

## 常用选项
- `-m`：持续监控，直到手动停止。
- `-r`：递归监控指定目录及其子目录。
- `-e`：指定要监控的事件类型，例如 `modify`、`create`、`delete` 等。
- `--format`：自定义输出格式。

## 常见示例
1. 监控当前目录的文件创建和删除事件：
   ```bash
   inotifywait -m -e create -e delete .
   ```

2. 递归监控 `/var/log` 目录的所有修改事件：
   ```bash
   inotifywait -m -r -e modify /var/log
   ```

3. 监控特定文件的修改事件并自定义输出格式：
   ```bash
   inotifywait -m --format '%w%f %e' -e modify /path/to/file.txt
   ```

4. 监控多个事件（创建、修改、删除）：
   ```bash
   inotifywait -m -e create -e modify -e delete /path/to/directory
   ```

## 小贴士
- 使用 `-m` 选项可以让 `inotifywait` 持续运行，适合需要长时间监控的场景。
- 结合其他命令使用，例如通过管道将输出传递给脚本进行自动化处理。
- 注意系统对 inotify 监控的限制，过多的监控可能会导致性能问题。可以通过调整 `/proc/sys/fs/inotify/max_user_watches` 来增加监控数量。