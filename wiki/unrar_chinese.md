# [Linux] Bash unrar 用法: 解压RAR文件

## 概述
`unrar` 命令用于解压缩RAR格式的压缩文件。它是一个强大的工具，能够处理各种RAR文件，包括加密和分卷压缩的文件。

## 用法
基本语法如下：
```bash
unrar [options] [arguments]
```

## 常用选项
- `e`：将文件解压到当前目录，不保留目录结构。
- `x`：将文件解压到当前目录，保留目录结构。
- `l`：列出压缩文件中的内容。
- `t`：测试压缩文件的完整性。
- `v`：详细模式，显示解压过程中的详细信息。

## 常见示例
1. 解压缩RAR文件到当前目录：
   ```bash
   unrar x archive.rar
   ```

2. 解压缩RAR文件到指定目录：
   ```bash
   unrar x archive.rar /path/to/destination/
   ```

3. 列出RAR文件中的内容：
   ```bash
   unrar l archive.rar
   ```

4. 测试RAR文件的完整性：
   ```bash
   unrar t archive.rar
   ```

5. 解压缩RAR文件而不保留目录结构：
   ```bash
   unrar e archive.rar
   ```

## 小贴士
- 在处理大文件时，使用`-v`选项可以帮助你了解解压缩的进度。
- 如果RAR文件是加密的，`unrar`会提示你输入密码。
- 使用`unrar`时，确保你的系统已安装该工具，可以通过包管理器进行安装。