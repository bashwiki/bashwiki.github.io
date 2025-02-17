# [Linux] Bash ping 用法: 检测网络连通性

## Overview
`ping` 命令用于测试网络连接的可达性。它通过向目标主机发送 ICMP 回显请求，并等待接收回显响应，从而确定网络连接是否正常。

## Usage
基本语法如下：
```bash
ping [options] [arguments]
```

## Common Options
- `-c <count>`: 指定发送的请求数量。
- `-i <interval>`: 指定发送请求的时间间隔（以秒为单位）。
- `-s <size>`: 指定发送数据包的大小。
- `-t <ttl>`: 设置数据包的生存时间（TTL）。

## Common Examples
1. **基本使用**: 测试与 Google 的连接。
   ```bash
   ping google.com
   ```

2. **发送特定数量的请求**: 发送 4 个请求。
   ```bash
   ping -c 4 google.com
   ```

3. **设置请求间隔**: 每 2 秒发送一个请求。
   ```bash
   ping -i 2 google.com
   ```

4. **指定数据包大小**: 发送 100 字节的数据包。
   ```bash
   ping -s 100 google.com
   ```

5. **设置 TTL**: 设置数据包的生存时间为 64。
   ```bash
   ping -t 64 google.com
   ```

## Tips
- 使用 `-c` 选项可以避免 `ping` 命令无限运行，方便测试。
- 如果你只想查看响应时间，可以使用 `-q` 选项，简化输出。
- 在网络故障排查时，尝试 ping 不同的主机，以确定问题是局部的还是全局的。