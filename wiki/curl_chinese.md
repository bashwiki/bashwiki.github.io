# [Linux] Bash curl 使用方法: 发送和接收数据的命令行工具

## 概述
curl 是一个用于在命令行中发送和接收数据的工具，支持多种协议，包括 HTTP、HTTPS、FTP 等。它常用于测试 API、下载文件以及进行网络请求。

## 用法
curl 的基本语法如下：

```bash
curl [options] [arguments]
```

## 常用选项
- `-X`：指定请求方法（如 GET、POST）。
- `-d`：发送数据，通常用于 POST 请求。
- `-H`：添加自定义请求头。
- `-o`：将输出保存到文件。
- `-I`：仅获取响应头。

## 常见示例
1. **发送 GET 请求**
   ```bash
   curl https://api.example.com/data
   ```

2. **发送 POST 请求并附带数据**
   ```bash
   curl -X POST -d "name=John&age=30" https://api.example.com/user
   ```

3. **添加自定义请求头**
   ```bash
   curl -H "Authorization: Bearer TOKEN" https://api.example.com/protected
   ```

4. **将响应保存到文件**
   ```bash
   curl -o response.json https://api.example.com/data
   ```

5. **获取响应头**
   ```bash
   curl -I https://api.example.com
   ```

## 小贴士
- 使用 `-v` 选项可以查看详细的请求和响应信息，帮助调试。
- 对于需要身份验证的请求，可以使用 `-u username:password` 来传递凭据。
- 结合 `-o` 和 `-L` 选项可以处理重定向并保存最终目标的内容。