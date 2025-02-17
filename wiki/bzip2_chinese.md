# [Linux] Bash bzip2 使用方法: 压缩和解压缩文件

## 概述
bzip2 是一个用于文件压缩和解压缩的命令行工具，能够有效地减少文件的大小，常用于备份和传输数据。

## 用法
bzip2 的基本语法如下：
```bash
bzip2 [选项] [参数]
```

## 常用选项
- `-d` 或 `--decompress`：解压缩文件。
- `-k` 或 `--keep`：在压缩或解压缩时保留原始文件。
- `-f` 或 `--force`：强制覆盖已存在的文件。
- `-v` 或 `--verbose`：显示详细的压缩过程信息。
- `-z` 或 `--compress`：压缩文件（默认操作）。

## 常见示例
1. **压缩文件**
   ```bash
   bzip2 example.txt
   ```
   这将创建一个名为 `example.txt.bz2` 的压缩文件，并删除原始的 `example.txt` 文件。

2. **解压缩文件**
   ```bash
   bzip2 -d example.txt.bz2
   ```
   这将解压缩 `example.txt.bz2` 文件，恢复为 `example.txt`。

3. **保留原始文件**
   ```bash
   bzip2 -k example.txt
   ```
   这将压缩 `example.txt`，并保留原始文件不变。

4. **强制覆盖已存在的文件**
   ```bash
   bzip2 -f example.txt
   ```
   如果 `example.txt.bz2` 已存在，将会被覆盖。

5. **显示详细信息**
   ```bash
   bzip2 -v example.txt
   ```
   这将显示压缩过程中的详细信息。

## 提示
- 使用 `-k` 选项可以避免意外删除原始文件，特别是在测试压缩效果时。
- 对于大文件，考虑使用 `-f` 选项以确保不会因文件已存在而导致压缩失败。
- 在处理多个文件时，可以使用通配符，例如 `bzip2 *.txt` 来压缩所有文本文件。