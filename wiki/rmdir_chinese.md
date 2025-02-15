# [리눅스] Bash rmdir 사용법

## 概述
`rmdir` 是一个用于删除空目录的 Bash 命令。它的主要目的是帮助用户清理文件系统中的空目录，从而保持目录结构的整洁。请注意，`rmdir` 只能删除没有文件或子目录的目录。如果目录不为空，命令将会失败。

## 用法
基本语法如下：
```
rmdir [选项] 目录名
```

常用选项包括：
- `-p`：递归删除目录及其父目录（如果父目录也为空）。
- `--ignore-fail-on-non-empty`：忽略非空目录的错误，不会显示错误信息。

## 示例
以下是使用 `rmdir` 命令的几个实际示例：

1. 删除一个空目录：
   ```bash
   rmdir my_empty_directory
   ```

2. 递归删除空目录及其父目录：
   ```bash
   rmdir -p my_empty_directory/my_subdirectory
   ```

## 小贴士
- 在使用 `rmdir` 前，确保目录确实为空。可以使用 `ls` 命令检查目录内容。
- 如果需要删除非空目录，考虑使用 `rm -r` 命令，但要小心使用，以免误删重要文件。
- 使用 `rmdir` 时，最好在命令前加上 `echo` 进行测试，以确保要删除的目录是正确的：
  ```bash
  echo rmdir my_empty_directory
  ```
这样可以避免意外删除错误的目录。