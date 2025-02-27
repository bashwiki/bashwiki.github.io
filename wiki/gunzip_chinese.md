# [Linux] Bash gunzip 使用方法: 解压缩 gzip 文件

## 概述
`gunzip` 命令用于解压缩以 `.gz` 为扩展名的文件。它是 GNU zip (gzip) 的一部分，广泛用于压缩和解压缩文件，以节省存储空间和加快传输速度。

## 用法
基本语法如下：
```
gunzip [选项] [参数]
```

## 常用选项
- `-c`：将解压缩的内容输出到标准输出，而不是直接修改文件。
- `-f`：强制解压缩，即使目标文件已存在。
- `-k`：保留原始的压缩文件，解压缩后不会删除它。
- `-v`：显示详细的解压缩过程，包括文件名和压缩比。

## 常见示例
1. 解压缩单个文件：
   ```bash
   gunzip file.gz
   ```

2. 解压缩多个文件：
   ```bash
   gunzip file1.gz file2.gz
   ```

3. 将解压缩的内容输出到标准输出：
   ```bash
   gunzip -c file.gz > output.txt
   ```

4. 强制解压缩已存在的文件：
   ```bash
   gunzip -f existing_file.gz
   ```

5. 保留原始压缩文件：
   ```bash
   gunzip -k file.gz
   ```

## 提示
- 在解压缩前，确保你有足够的磁盘空间来存放解压后的文件。
- 使用 `-v` 选项可以帮助你了解解压缩过程，尤其是在处理多个文件时。
- 如果你不确定文件是否为 gzip 格式，可以使用 `file` 命令检查文件类型。