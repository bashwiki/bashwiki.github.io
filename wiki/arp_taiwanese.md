# [台灣] Bash arp 使用方式: 查看和管理ARP緩存

## Overview
`arp` 命令用於顯示和管理系統的ARP（地址解析協議）緩存。ARP緩存存儲了IP地址與其對應的物理地址（MAC地址）之間的映射，這對於網絡通信至關重要。

## Usage
基本語法如下：
```
arp [options] [arguments]
```

## Common Options
- `-a`：顯示所有ARP條目。
- `-d`：刪除指定的ARP條目。
- `-s`：手動添加一個ARP條目。
- `-n`：以數字格式顯示地址，避免進行DNS查詢。

## Common Examples
以下是一些常見的使用範例：

1. 顯示所有ARP緩存條目：
   ```bash
   arp -a
   ```

2. 刪除特定的ARP條目：
   ```bash
   arp -d 192.168.1.1
   ```

3. 手動添加一個ARP條目：
   ```bash
   arp -s 192.168.1.10 00:1A:2B:3C:4D:5E
   ```

4. 以數字格式顯示ARP條目：
   ```bash
   arp -n
   ```

## Tips
- 定期檢查ARP緩存可以幫助識別潛在的網絡問題。
- 在添加ARP條目時，確保MAC地址的格式正確。
- 使用 `arp -a` 來快速查看所有連接設備的IP和MAC地址，這對於網絡管理非常有幫助。