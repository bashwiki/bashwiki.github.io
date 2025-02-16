# [Linux] Bash ip 使用說明: 查詢和管理網路介面

## Overview
`ip` 命令是一個用於查詢和管理 Linux 系統中的網路介面的工具。它可以用來顯示網路設定、添加或刪除路由、以及管理網路設備等。

## Usage
基本語法如下：
```
ip [options] [arguments]
```

## Common Options
- `link`：顯示或管理網路介面。
- `addr`：顯示或管理 IP 地址。
- `route`：顯示或管理路由表。
- `neigh`：顯示或管理 ARP 表。
- `tunnel`：管理隧道介面。

## Common Examples
1. 顯示所有網路介面的狀態：
   ```bash
   ip link show
   ```

2. 顯示所有 IP 地址：
   ```bash
   ip addr show
   ```

3. 添加一個新的 IP 地址到指定的網路介面：
   ```bash
   ip addr add 192.168.1.100/24 dev eth0
   ```

4. 刪除指定的 IP 地址：
   ```bash
   ip addr del 192.168.1.100/24 dev eth0
   ```

5. 顯示路由表：
   ```bash
   ip route show
   ```

6. 添加一條新的路由：
   ```bash
   ip route add 10.0.0.0/8 via 192.168.1.1
   ```

## Tips
- 使用 `ip -h` 可以查看所有可用的選項和用法。
- 在進行網路設定時，建議先備份當前的配置，以防出現問題。
- 對於臨時的網路設定，`ip` 命令非常方便，但重啟後可能會失效，建議在系統啟動時自動配置。