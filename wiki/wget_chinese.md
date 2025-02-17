# [Linux] Bash wget 用法: 下载文件的命令行工具

## 概述
`wget` 是一个用于从网络上下载文件的命令行工具。它支持 HTTP、HTTPS 和 FTP 协议，可以在不需要用户交互的情况下进行下载，非常适合批量下载和自动化任务。

## 用法
基本语法如下：
```
wget [选项] [参数]
```

## 常用选项
- `-O <文件名>`: 指定下载文件的名称。
- `-c`: 继续未完成的下载。
- `-q`: 安静模式，不显示下载进度。
- `--limit-rate=<速度>`: 限制下载速度。
- `-r`: 递归下载，下载整个网站。

## 常见示例
1. 下载一个文件：
   ```bash
   wget http://example.com/file.zip
   ```

2. 指定下载文件名：
   ```bash
   wget -O myfile.zip http://example.com/file.zip
   ```

3. 继续未完成的下载：
   ```bash
   wget -c http://example.com/largefile.zip
   ```

4. 限制下载速度为 200KB/s：
   ```bash
   wget --limit-rate=200k http://example.com/file.zip
   ```

5. 递归下载整个网站：
   ```bash
   wget -r http://example.com/
   ```

## 小贴士
- 使用 `-q` 选项可以在脚本中运行 wget 时减少输出，保持终端整洁。
- 在下载大文件时，使用 `-c` 选项可以避免重新下载已存在的部分。
- 结合 `--limit-rate` 选项，可以在网络带宽有限的情况下进行下载，避免影响其他网络活动。