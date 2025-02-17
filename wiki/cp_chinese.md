# [Linux] Bash cp 使用方法: 复制文件和目录

## 概述
`cp` 命令用于在 Linux 系统中复制文件和目录。它可以将源文件或目录复制到目标位置，支持多种选项以满足不同的需求。

## 用法
基本语法如下：
```
cp [选项] [源文件或目录] [目标文件或目录]
```

## 常用选项
- `-r`：递归复制目录及其内容。
- `-i`：在覆盖文件之前提示确认。
- `-u`：仅在源文件比目标文件新时复制。
- `-v`：显示详细的复制过程。
- `-a`：归档模式，复制文件并保持其属性。

## 常见示例
1. 复制单个文件：
   ```bash
   cp file.txt /path/to/destination/
   ```

2. 复制多个文件到目标目录：
   ```bash
   cp file1.txt file2.txt /path/to/destination/
   ```

3. 递归复制目录：
   ```bash
   cp -r /path/to/source_directory /path/to/destination_directory/
   ```

4. 使用提示确认覆盖文件：
   ```bash
   cp -i file.txt /path/to/destination/
   ```

5. 显示详细的复制过程：
   ```bash
   cp -v file.txt /path/to/destination/
   ```

## 提示
- 在使用 `cp` 命令时，确保目标路径存在，避免出现错误。
- 使用 `-i` 选项可以避免意外覆盖重要文件。
- 对于大量文件的复制，考虑使用 `-u` 选项以提高效率，避免不必要的复制。