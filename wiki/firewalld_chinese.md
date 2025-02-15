# [리눅스] Bash firewalld 사용법

## 概述
`firewalld` 是一个动态管理防火墙的工具，主要用于在 Linux 系统上配置和管理网络流量的访问控制。它支持区域和服务的概念，使得用户可以根据不同的网络环境灵活地设置防火墙规则。`firewalld` 提供了一个简单的命令行界面和图形用户界面，方便用户进行防火墙配置。

## 用法
基本语法如下：
```bash
firewalld [OPTIONS]
```

常用选项包括：
- `--zone=<zone>`：指定要操作的区域。
- `--add-service=<service>`：在指定区域中添加服务。
- `--remove-service=<service>`：在指定区域中移除服务。
- `--add-port=<port>/<protocol>`：在指定区域中添加端口。
- `--remove-port=<port>/<protocol>`：在指定区域中移除端口。
- `--set-target=<target>`：设置区域的目标（如：ACCEPT, DROP等）。

## 示例
1. **添加服务到公共区域**
   ```bash
   firewall-cmd --zone=public --add-service=http --permanent
   ```
   这个命令将 HTTP 服务添加到公共区域，并使更改永久生效。

2. **查看当前区域的配置**
   ```bash
   firewall-cmd --get-active-zones
   ```
   该命令将列出当前活动的区域及其相关配置。

## 提示
- 使用 `--permanent` 选项时，请确保在重新加载防火墙之前，您已完成所有更改。可以使用 `firewall-cmd --reload` 命令来应用更改。
- 定期检查防火墙规则，以确保没有不必要的开放端口或服务，增强系统安全性。
- 使用 `firewall-cmd --list-all` 命令查看当前区域的所有配置，帮助您了解现有的防火墙设置。