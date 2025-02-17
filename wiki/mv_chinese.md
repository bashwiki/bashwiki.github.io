# [Linux] Bash mv 用法: 移动或重命名文件和目录

## 概述
`mv` 命令用于在 Linux 和 Unix 系统中移动文件和目录，或者重命名它们。该命令是文件管理中非常常用的工具。

## 用法
基本语法如下：
```bash
mv [选项] [源] [目标]
```

## 常用选项
- `-i`：在覆盖文件之前提示确认。
- `-u`：仅在源文件比目标文件新时才移动。
- `-v`：显示详细的操作过程。
- `-n`：不覆盖已存在的文件。

## 常见示例
1. 移动文件到另一个目录：
   ```bash
   mv file.txt /path/to/destination/
   ```

2. 重命名文件：
   ```bash
   mv oldname.txt newname.txt
   ```

3. 移动并重命名文件：
   ```bash
   mv file.txt /path/to/destination/newname.txt
   ```

4. 使用 `-i` 选项提示确认：
   ```bash
   mv -i file.txt /path/to/destination/
   ```

5. 使用 `-v` 选项显示详细信息：
   ```bash
   mv -v file.txt /path/to/destination/
   ```

## 小贴士
- 在移动或重命名重要文件时，使用 `-i` 选项可以防止意外覆盖。
- 使用 `-v` 选项可以帮助你跟踪操作过程，特别是在处理多个文件时。
- 在移动大量文件时，考虑使用 `-u` 选项，以避免不必要的文件覆盖。