# [Linux] Bash hostname 用法: 显示或设置主机名

## 概述
`hostname` 命令用于显示或设置计算机的主机名。主机名是网络中识别计算机的名称，通常用于网络通信和管理。

## 用法
基本语法如下：
```bash
hostname [options] [arguments]
```

## 常用选项
- `-a`：显示别名。
- `-d`：显示域名。
- `-f`：显示完全合格的域名（FQDN）。
- `-i`：显示主机的 IP 地址。
- `-s`：显示短主机名。

## 常见示例
1. 显示当前主机名：
   ```bash
   hostname
   ```

2. 显示完整的主机名：
   ```bash
   hostname -f
   ```

3. 显示主机的 IP 地址：
   ```bash
   hostname -i
   ```

4. 设置新的主机名：
   ```bash
   sudo hostname new-hostname
   ```

5. 显示主机的别名：
   ```bash
   hostname -a
   ```

## 提示
- 在更改主机名后，建议重启计算机以确保所有服务都能识别新的主机名。
- 使用 `hostnamectl` 命令可以更方便地管理主机名，特别是在使用 systemd 的系统中。
- 确保新的主机名符合网络命名规则，避免使用特殊字符。