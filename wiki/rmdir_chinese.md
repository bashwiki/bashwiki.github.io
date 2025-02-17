# [Linux] Bash rmdir 用法: 删除空目录

## 概述
`rmdir` 命令用于删除空目录。如果目录中包含文件或其他目录，`rmdir` 将无法删除该目录。

## 用法
基本的命令语法如下：
```bash
rmdir [选项] [参数]
```

## 常用选项
- `-p`：递归删除目录，只有在父目录也为空时才会删除。
- `--ignore-fail-on-non-empty`：如果目录不为空，则忽略错误并继续执行。

## 常见示例
1. 删除一个空目录：
   ```bash
   rmdir my_empty_directory
   ```

2. 递归删除空目录及其父目录：
   ```bash
   rmdir -p my_empty_directory/parent_directory
   ```

3. 忽略非空目录的错误：
   ```bash
   rmdir --ignore-fail-on-non-empty my_non_empty_directory
   ```

## 提示
- 在使用 `rmdir` 前，确保目录确实为空，以避免错误。
- 可以使用 `ls` 命令检查目录内容：
  ```bash
  ls my_empty_directory
  ```
- 对于非空目录，考虑使用 `rm -r` 命令来删除目录及其内容。