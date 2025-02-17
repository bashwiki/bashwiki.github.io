# [Linux] Bash systemctl 用法: 管理系统服务

## 概述
`systemctl` 是一个用于管理系统和服务管理器的命令行工具，主要用于启动、停止、重启和检查服务的状态。它是 `systemd` 的一部分，广泛应用于现代 Linux 发行版中。

## 用法
基本语法如下：
```bash
systemctl [options] [arguments]
```

## 常用选项
- `start`：启动指定的服务。
- `stop`：停止指定的服务。
- `restart`：重启指定的服务。
- `status`：查看指定服务的当前状态。
- `enable`：设置服务在系统启动时自动启动。
- `disable`：禁止服务在系统启动时自动启动。
- `list-units`：列出当前加载的单元（服务、套接字等）。

## 常见示例
1. 启动服务：
   ```bash
   systemctl start nginx
   ```

2. 停止服务：
   ```bash
   systemctl stop nginx
   ```

3. 重启服务：
   ```bash
   systemctl restart nginx
   ```

4. 查看服务状态：
   ```bash
   systemctl status nginx
   ```

5. 设置服务开机自启：
   ```bash
   systemctl enable nginx
   ```

6. 禁止服务开机自启：
   ```bash
   systemctl disable nginx
   ```

7. 列出所有加载的单元：
   ```bash
   systemctl list-units
   ```

## 提示
- 使用 `systemctl` 命令时，建议以 `sudo` 权限运行，以确保有足够的权限管理服务。
- 定期检查服务状态，以确保关键服务正常运行。
- 使用 `systemctl` 的 `--quiet` 选项可以减少输出信息，适合在脚本中使用。