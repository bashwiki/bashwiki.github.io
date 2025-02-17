# [Linux] Bash firewalld 用法: 管理防火墙规则

## 概述
firewalld 是一个动态管理防火墙的工具，允许用户通过命令行或图形界面来配置和管理网络流量的访问控制。它支持区域和服务的概念，使得防火墙规则的管理更加灵活和易于使用。

## 用法
基本语法如下：
```
firewalld [options] [arguments]
```

## 常用选项
- `--zone=<zone>`: 指定要操作的区域。
- `--add-service=<service>`: 向指定区域添加服务。
- `--remove-service=<service>`: 从指定区域移除服务。
- `--add-port=<port>/<protocol>`: 向指定区域添加端口。
- `--remove-port=<port>/<protocol>`: 从指定区域移除端口。
- `--list-all`: 列出当前区域的所有规则和设置。

## 常见示例
1. **添加服务到公共区域**
   ```bash
   firewall-cmd --zone=public --add-service=http --permanent
   ```

2. **移除服务**
   ```bash
   firewall-cmd --zone=public --remove-service=http --permanent
   ```

3. **添加端口**
   ```bash
   firewall-cmd --zone=public --add-port=8080/tcp --permanent
   ```

4. **移除端口**
   ```bash
   firewall-cmd --zone=public --remove-port=8080/tcp --permanent
   ```

5. **重新加载防火墙规则**
   ```bash
   firewall-cmd --reload
   ```

6. **列出所有区域的规则**
   ```bash
   firewall-cmd --list-all
   ```

## 小贴士
- 在进行任何更改之前，建议使用 `--list-all` 命令查看当前配置，以避免意外更改。
- 使用 `--permanent` 选项可以确保更改在防火墙重启后仍然有效。
- 定期检查和更新防火墙规则，以确保网络安全性。