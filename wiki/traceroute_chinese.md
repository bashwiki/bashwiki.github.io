# [Linux] Bash traceroute 用法: 路由跟踪命令

## 概述
`traceroute` 命令用于跟踪数据包在网络中从源主机到目标主机的路径。它能够显示经过的每一个路由器的 IP 地址以及响应时间，帮助用户分析网络连接的延迟和问题。

## 用法
基本语法如下：
```bash
traceroute [options] [arguments]
```

## 常用选项
- `-m <hops>`: 设置最大跳数，限制 traceroute 能够经过的路由器数量。
- `-n`: 直接使用 IP 地址而不进行域名解析，快速显示结果。
- `-p <port>`: 指定要使用的目标端口，默认是 33434。
- `-w <seconds>`: 设置等待每个响应的时间，默认是 5 秒。

## 常见示例
1. 跟踪到某个主机的路由：
   ```bash
   traceroute example.com
   ```

2. 使用 IP 地址而不解析域名：
   ```bash
   traceroute -n 8.8.8.8
   ```

3. 设置最大跳数为 10：
   ```bash
   traceroute -m 10 example.com
   ```

4. 指定目标端口为 80：
   ```bash
   traceroute -p 80 example.com
   ```

5. 设置响应等待时间为 2 秒：
   ```bash
   traceroute -w 2 example.com
   ```

## 提示
- 在进行网络故障排除时，使用 `-n` 选项可以加快结果显示速度。
- 如果网络连接不稳定，可以尝试增加等待时间以获得更准确的响应。
- 了解每个跳数的延迟情况，可以帮助定位网络瓶颈。