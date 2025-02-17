# [Linux] Bash cron 使用: 定时任务调度

## 概述
`cron` 是一个用于在 Unix 和类 Unix 系统上定期执行任务的工具。它允许用户设置计划任务，以便在特定的时间间隔内自动运行指定的命令或脚本。

## 用法
基本的 `cron` 语法如下：

```bash
cron [options] [arguments]
```

## 常用选项
- `-l`：列出当前用户的所有定时任务。
- `-e`：编辑当前用户的定时任务。
- `-r`：删除当前用户的所有定时任务。

## 常见示例
以下是一些常见的 `cron` 使用示例：

1. **每小时执行一个脚本**
   ```bash
   0 * * * * /path/to/script.sh
   ```

2. **每天凌晨 2 点执行备份**
   ```bash
   0 2 * * * /usr/bin/backup.sh
   ```

3. **每周一执行清理任务**
   ```bash
   0 0 * * 1 /usr/local/bin/cleanup.sh
   ```

4. **每分钟检查服务状态**
   ```bash
   * * * * * /usr/bin/check_service.sh
   ```

## 小贴士
- 确保脚本具有可执行权限，可以使用 `chmod +x /path/to/script.sh` 来设置。
- 使用绝对路径来指定脚本或命令，以避免路径问题。
- 定期检查 `cron` 日志，以确保任务按预期执行，通常日志位于 `/var/log/cron`。