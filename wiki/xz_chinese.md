# [Linux] Bash xz 使用方法: 压缩和解压缩文件

## 概述
`xz` 命令用于在 Linux 系统中压缩和解压缩文件。它使用 LZMA 算法，能够提供高效的压缩比率，适合处理大型文件。

## 用法
基本语法如下：
```bash
xz [options] [arguments]
```

## 常用选项
- `-d` 或 `--decompress`：解压缩文件。
- `-k` 或 `--keep`：在压缩时保留原始文件。
- `-f` 或 `--force`：强制覆盖已存在的文件。
- `-z` 或 `--compress`：压缩文件（默认操作）。
- `-9`：使用最高压缩级别。

## 常见示例
1. 压缩文件：
   ```bash
   xz file.txt
   ```
   这将创建一个名为 `file.txt.xz` 的压缩文件，并删除原始的 `file.txt`。

2. 解压缩文件：
   ```bash
   xz -d file.txt.xz
   ```
   这将解压缩 `file.txt.xz`，恢复为 `file.txt`。

3. 保留原始文件：
   ```bash
   xz -k file.txt
   ```
   这将压缩 `file.txt`，同时保留原始文件。

4. 强制压缩：
   ```bash
   xz -f file.txt
   ```
   如果 `file.txt.xz` 已存在，这将覆盖它。

5. 使用最高压缩级别：
   ```bash
   xz -9 file.txt
   ```
   这将以最高压缩级别压缩文件。

## 小贴士
- 在处理非常大的文件时，考虑使用 `-k` 选项以保留原始文件，避免数据丢失。
- 结合 `tar` 命令使用，可以更方便地压缩和打包多个文件：
  ```bash
  tar -cJf archive.tar.xz folder/
  ```
- 使用 `-v` 选项可以在压缩过程中显示详细信息，方便监控进度。