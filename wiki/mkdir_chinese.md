# [Linux] Bash mkdir 用法: 创建目录

## 概述
`mkdir` 命令用于在文件系统中创建新目录。这个命令非常简单且常用，是管理文件和目录结构的基础工具之一。

## 用法
基本语法如下：
```
mkdir [选项] [参数]
```

## 常用选项
- `-p`：递归创建目录，如果父目录不存在，则一并创建。
- `-v`：在创建目录时显示详细信息。
- `-m`：设置新目录的权限模式。

## 常见示例
1. 创建单个目录：
   ```bash
   mkdir my_directory
   ```

2. 创建多个目录：
   ```bash
   mkdir dir1 dir2 dir3
   ```

3. 递归创建目录：
   ```bash
   mkdir -p parent_dir/child_dir
   ```

4. 创建目录并显示详细信息：
   ```bash
   mkdir -v new_directory
   ```

5. 创建目录并设置权限：
   ```bash
   mkdir -m 755 my_secure_directory
   ```

## 提示
- 使用 `-p` 选项可以避免因父目录不存在而导致的错误。
- 在创建多个目录时，可以一次性指定多个目录名，节省时间。
- 记得根据需要设置目录权限，以确保安全性和可访问性。