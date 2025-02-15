# [리눅스] Bash systemctl 사용법

## 概述
`systemctl` 是一个用于控制系统和服务管理器的命令行工具，主要用于管理 Linux 系统中的 systemd 服务。它可以启动、停止、重启和检查服务的状态，以及管理系统的运行级别和目标。`systemctl` 是现代 Linux 发行版中管理服务的标准工具。

## 用法
基本语法如下：
```bash
systemctl [选项] [命令] [服务名]
```
常用选项包括：
- `start`：启动指定的服务。
- `stop`：停止指定的服务。
- `restart`：重启指定的服务。
- `status`：查看指定服务的当前状态。
- `enable`：设置服务在系统启动时自动启动。
- `disable`：禁止服务在系统启动时自动启动。
- `list-units`：列出所有已加载的单元（服务、套接字等）。

## 示例
1. 启动服务：
   ```bash
   systemctl start nginx
   ```
   这个命令将启动 Nginx 服务。

2. 检查服务状态：
   ```bash
   systemctl status nginx
   ```
   这个命令将显示 Nginx 服务的当前状态，包括是否正在运行、最近的日志等信息。

## 提示
- 使用 `systemctl` 时，建议以 root 用户或使用 `sudo` 权限执行命令，以确保有足够的权限管理服务。
- 定期检查服务的状态可以帮助及时发现和解决问题，使用 `systemctl status [服务名]` 是一个好习惯。
- 可以使用 `systemctl list-units --type=service` 来查看所有正在运行的服务，帮助您更好地管理系统资源。