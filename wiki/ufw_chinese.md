# [Linux] Bash ufw 使用方法: 管理防火墙规则

## 概述
`ufw`（Uncomplicated Firewall）是一个用于管理Linux系统防火墙的命令行工具。它旨在简化iptables的复杂性，使用户能够更轻松地配置防火墙规则。

## 用法
基本语法如下：
```
ufw [options] [arguments]
```

## 常用选项
- `enable`：启用防火墙。
- `disable`：禁用防火墙。
- `allow`：允许特定的流量。
- `deny`：拒绝特定的流量。
- `status`：查看防火墙的当前状态和规则。
- `reset`：重置防火墙规则到默认状态。

## 常见示例
1. 启用防火墙：
   ```bash
   ufw enable
   ```

2. 禁用防火墙：
   ```bash
   ufw disable
   ```

3. 允许SSH流量：
   ```bash
   ufw allow ssh
   ```

4. 允许特定端口（例如，80端口）：
   ```bash
   ufw allow 80
   ```

5. 拒绝特定端口（例如，23端口）：
   ```bash
   ufw deny 23
   ```

6. 查看防火墙状态：
   ```bash
   ufw status
   ```

7. 重置防火墙规则：
   ```bash
   ufw reset
   ```

## 小贴士
- 在启用防火墙之前，确保允许SSH流量，以免锁定自己。
- 定期检查防火墙状态，确保规则符合当前的安全需求。
- 使用`ufw status verbose`命令可以获取更详细的状态信息。