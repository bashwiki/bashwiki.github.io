# [Linux] Bash arp 用法: 显示和修改ARP缓存

## 概述
`arp` 命令用于显示和修改系统的地址解析协议（ARP）缓存。ARP缓存存储了IP地址与物理地址（MAC地址）之间的映射，帮助网络设备在局域网中进行通信。

## 用法
基本语法如下：
```
arp [选项] [参数]
```

## 常用选项
- `-a`：显示所有ARP条目。
- `-d <hostname>`：删除指定主机的ARP条目。
- `-s <hostname> <hw_addr>`：手动添加一个ARP条目。
- `-n`：以数字形式显示地址，而不进行名称解析。

## 常见示例
1. 显示当前ARP缓存：
   ```bash
   arp -a
   ```

2. 删除特定主机的ARP条目：
   ```bash
   arp -d 192.168.1.1
   ```

3. 添加一个新的ARP条目：
   ```bash
   arp -s 192.168.1.10 00:1A:2B:3C:4D:5E
   ```

4. 以数字形式显示ARP条目：
   ```bash
   arp -n
   ```

## 提示
- 定期检查ARP缓存可以帮助识别网络中的潜在问题。
- 在添加静态ARP条目时，请确保IP地址和MAC地址的正确性，以避免网络冲突。
- 使用 `arp -a` 命令可以快速查看网络中所有活动设备的IP和MAC地址。