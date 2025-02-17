# [Linux] Bash dig 使用说明：查询DNS信息

## 概述
`dig`（Domain Information Groper）是一个用于查询DNS（域名系统）信息的命令行工具。它可以帮助用户获取域名的解析记录，包括A记录、MX记录、CNAME记录等。

## 用法
基本语法如下：
```
dig [选项] [参数]
```

## 常用选项
- `@server`：指定要查询的DNS服务器。
- `-t type`：指定查询的记录类型（例如：A、MX、CNAME等）。
- `+short`：以简短格式显示结果。
- `+trace`：追踪DNS解析过程。

## 常见示例
1. 查询某个域名的A记录：
   ```bash
   dig example.com
   ```

2. 查询特定DNS服务器的A记录：
   ```bash
   dig @8.8.8.8 example.com
   ```

3. 查询域名的MX记录：
   ```bash
   dig example.com -t MX
   ```

4. 使用简短格式查询CNAME记录：
   ```bash
   dig example.com -t CNAME +short
   ```

5. 追踪DNS解析过程：
   ```bash
   dig example.com +trace
   ```

## 提示
- 使用`+short`选项可以使输出结果更加简洁，便于快速查看。
- 如果你经常查询某个域名，可以考虑将其放入别名中，以便快速访问。
- 了解不同的记录类型可以帮助你更好地使用`dig`命令，确保获取所需的信息。