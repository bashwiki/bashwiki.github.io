# [Linux] Bash rar 用法: 压缩和解压缩文件

## 概述
`rar` 命令用于创建和管理 RAR 格式的压缩文件。它可以有效地压缩文件和目录，节省存储空间，并提供数据完整性检查。

## 用法
基本语法如下：
```bash
rar [options] [arguments]
```

## 常用选项
- `a`：添加文件到压缩包。
- `x`：从压缩包中提取文件。
- `t`：测试压缩包的完整性。
- `v`：显示详细信息。
- `r`：递归添加目录中的文件。

## 常见示例
1. 创建一个新的 RAR 压缩包：
   ```bash
   rar a myarchive.rar /path/to/files/*
   ```

2. 解压缩 RAR 文件：
   ```bash
   rar x myarchive.rar
   ```

3. 测试 RAR 文件的完整性：
   ```bash
   rar t myarchive.rar
   ```

4. 递归添加目录中的所有文件到压缩包：
   ```bash
   rar a myarchive.rar /path/to/directory/*
   ```

5. 显示压缩过程的详细信息：
   ```bash
   rar a -v myarchive.rar /path/to/files/*
   ```

## 提示
- 在压缩大文件时，可以使用 `-m5` 选项来提高压缩比，但会增加处理时间。
- 定期测试你的 RAR 文件，以确保数据的完整性。
- 使用 `-p` 选项可以为压缩包设置密码，增加安全性。