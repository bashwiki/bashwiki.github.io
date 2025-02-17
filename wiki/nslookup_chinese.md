# [Linux] Bash nslookup 用法: 查询域名的IP地址

## 概述
`nslookup` 是一个用于查询域名系统（DNS）记录的命令行工具。它可以帮助用户获取域名对应的IP地址，或者反向查询IP地址以获取域名信息。

## 用法
基本语法如下：
```
nslookup [options] [arguments]
```

## 常用选项
- `-type=TYPE`：指定查询的记录类型，如 A、AAAA、MX、CNAME 等。
- `-timeout=SECONDS`：设置查询超时时间，单位为秒。
- `-retry=NUMBER`：设置查询失败后的重试次数。
- `-debug`：显示详细的调试信息。

## 常见示例
1. 查询域名的IP地址：
   ```bash
   nslookup example.com
   ```

2. 查询特定类型的DNS记录（如MX记录）：
   ```bash
   nslookup -type=MX example.com
   ```

3. 使用特定的DNS服务器进行查询：
   ```bash
   nslookup example.com 8.8.8.8
   ```

4. 反向查询IP地址以获取域名：
   ```bash
   nslookup 93.184.216.34
   ```

## 提示
- 使用 `-debug` 选项可以帮助你更好地理解查询过程，特别是在遇到问题时。
- 如果你经常需要查询不同类型的DNS记录，可以考虑将常用命令写入脚本以提高效率。
- 确保你的网络连接正常，以避免因网络问题导致的查询失败。