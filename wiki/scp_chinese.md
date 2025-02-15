# [리눅스] Bash scp 사용법

## 概述
`scp`（Secure Copy Protocol）是一个用于在本地和远程主机之间安全地复制文件和目录的命令。它基于SSH（Secure Shell）协议，确保数据在传输过程中得到加密，提供了安全性和隐私保护。`scp` 适用于在网络中传输文件，尤其是在需要安全传输的场合。

## 用法
`scp` 的基本语法如下：

```bash
scp [选项] [源文件] [目标]
```

### 常见选项
- `-r`：递归复制整个目录。
- `-P`：指定远程主机的端口号（注意是大写的 P）。
- `-i`：指定用于身份验证的私钥文件。
- `-v`：启用详细模式，输出调试信息。
- `-q`：安静模式，不显示进度条。

## 示例
### 示例 1：从本地复制文件到远程主机
```bash
scp /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
```
在这个示例中，`file.txt` 文件将被复制到远程主机的指定目录中。

### 示例 2：从远程主机复制文件到本地
```bash
scp user@remote_host:/path/to/remote/file.txt /path/to/local/directory/
```
这个命令将从远程主机复制 `file.txt` 文件到本地指定目录中。

### 示例 3：递归复制整个目录
```bash
scp -r /path/to/local/directory user@remote_host:/path/to/remote/
```
使用 `-r` 选项可以递归地复制整个目录。

## 提示
- 使用 `-P` 选项时，请确保使用大写字母，因为小写的 `-p` 是用于保留文件的修改时间和访问时间。
- 在频繁使用 `scp` 的情况下，可以设置 SSH 密钥，以避免每次都输入密码。
- 在大文件传输时，使用 `-v` 选项可以帮助你监控传输进度，便于排查问题。
- 确保目标路径存在，否则 `scp` 将返回错误。

通过掌握 `scp` 命令，您可以轻松地在本地和远程系统之间安全地传输文件。