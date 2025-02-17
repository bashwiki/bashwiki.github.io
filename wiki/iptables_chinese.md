# [Linux] Bash iptables 使用指南: 管理网络流量

## 概述
`iptables` 是一个用于配置 Linux 内核防火墙的命令行工具。它允许用户设置规则来控制网络流量的进出，提供了强大的网络安全功能。

## 用法
基本语法如下：
```bash
iptables [options] [arguments]
```

## 常用选项
- `-A`：在链的末尾添加规则。
- `-D`：删除指定的规则。
- `-I`：在链的开头插入规则。
- `-L`：列出当前的规则。
- `-F`：清空指定链的所有规则。
- `-P`：设置默认策略。

## 常见示例
1. **列出所有规则**
   ```bash
   iptables -L
   ```

2. **允许特定端口的入站流量（例如，允许 HTTP 流量）**
   ```bash
   iptables -A INPUT -p tcp --dport 80 -j ACCEPT
   ```

3. **拒绝特定 IP 地址的入站流量**
   ```bash
   iptables -A INPUT -s 192.168.1.100 -j DROP
   ```

4. **清空所有规则**
   ```bash
   iptables -F
   ```

5. **设置默认策略为拒绝所有入站流量**
   ```bash
   iptables -P INPUT DROP
   ```

## 提示
- 在修改规则之前，建议备份当前的 iptables 配置，以便在需要时恢复。
- 使用 `iptables-save` 和 `iptables-restore` 命令可以方便地保存和恢复规则。
- 定期检查和更新防火墙规则，以确保网络安全。