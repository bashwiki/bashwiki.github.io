# [Linux] Bash shutdown 用法: 关闭系统

## 概述
`shutdown` 命令用于安全地关闭或重启计算机。它允许用户指定关闭的时间和方式，确保系统在关闭前完成所有正在进行的任务。

## 用法
基本语法如下：
```
shutdown [options] [time] [message]
```

## 常用选项
- `-h`：关闭系统。
- `-r`：重启系统。
- `-c`：取消一个已计划的关闭。
- `+m`：在指定的分钟后关闭，例如 `+5` 表示5分钟后关闭。
- `hh:mm`：在指定的小时和分钟关闭，例如 `23:00` 表示晚上11点关闭。

## 常见示例
1. **立即关闭系统**：
   ```bash
   shutdown -h now
   ```

2. **在5分钟后重启系统**：
   ```bash
   shutdown -r +5
   ```

3. **在晚上11点关闭系统**：
   ```bash
   shutdown -h 23:00
   ```

4. **取消一个已计划的关闭**：
   ```bash
   shutdown -c
   ```

5. **发送关闭通知**：
   ```bash
   shutdown -h +1 "系统将在1分钟后关闭，请保存您的工作。"
   ```

## 提示
- 在使用 `shutdown` 命令前，请确保您有足够的权限，通常需要超级用户权限。
- 使用 `-h` 选项时，确保所有重要任务已完成，以避免数据丢失。
- 在计划关闭时，提前通知其他用户，以减少对他们工作的影响。