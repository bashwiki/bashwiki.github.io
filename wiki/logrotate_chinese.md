# [Linux] Bash logrotate 用法: 管理日志文件的轮换

## 概述
logrotate 是一个用于管理系统日志文件的工具，它可以自动轮换、压缩和删除旧的日志文件，以帮助节省磁盘空间并保持系统的整洁。

## 用法
基本语法如下：
```bash
logrotate [options] [arguments]
```

## 常用选项
- `-f`：强制执行轮换，即使日志文件未达到轮换条件。
- `-s`：指定状态文件的位置，状态文件用于记录上次轮换的状态。
- `-v`：在执行时显示详细信息，便于调试。
- `-d`：以调试模式运行，不实际执行轮换，只显示将要执行的操作。

## 常见示例
1. **使用默认配置文件进行日志轮换**
   ```bash
   logrotate /etc/logrotate.conf
   ```

2. **强制轮换指定的日志文件**
   ```bash
   logrotate -f /etc/logrotate.d/myapp
   ```

3. **查看将要执行的操作而不实际执行**
   ```bash
   logrotate -d /etc/logrotate.conf
   ```

4. **指定状态文件进行轮换**
   ```bash
   logrotate -s /var/lib/logrotate.status /etc/logrotate.conf
   ```

## 小贴士
- 定期检查日志文件的大小，确保 logrotate 配置合理，以免占用过多磁盘空间。
- 在进行重要的日志轮换操作前，备份日志文件以防数据丢失。
- 使用 `-v` 选项可以帮助你了解 logrotate 的执行情况，便于排查问题。