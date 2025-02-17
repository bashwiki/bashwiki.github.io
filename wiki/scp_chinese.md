# [Linux] Bash scp 使用方法: 远程文件复制

## 概述
`scp`（Secure Copy Protocol）命令用于在本地和远程主机之间安全地复制文件或目录。它基于SSH协议，确保数据在传输过程中的安全性。

## 用法
基本语法如下：
```bash
scp [options] [source] [destination]
```

## 常用选项
- `-r`：递归复制整个目录。
- `-P`：指定远程主机的端口（注意是大写的P）。
- `-i`：指定用于身份验证的私钥文件。
- `-v`：显示详细的操作过程，便于调试。

## 常见示例
1. 从本地复制文件到远程主机：
   ```bash
   scp /path/to/local/file username@remote_host:/path/to/remote/directory
   ```

2. 从远程主机复制文件到本地：
   ```bash
   scp username@remote_host:/path/to/remote/file /path/to/local/directory
   ```

3. 递归复制整个目录到远程主机：
   ```bash
   scp -r /path/to/local/directory username@remote_host:/path/to/remote/directory
   ```

4. 使用指定端口复制文件：
   ```bash
   scp -P 2222 /path/to/local/file username@remote_host:/path/to/remote/directory
   ```

## 提示
- 使用`-v`选项可以帮助您调试连接问题。
- 确保SSH服务在远程主机上运行，并且您有适当的访问权限。
- 对于大文件传输，考虑使用`-C`选项启用压缩，以提高传输速度。