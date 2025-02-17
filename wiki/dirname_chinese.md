# [Linux] Bash dirname 用法: 获取路径的目录部分

## 概述
`dirname` 命令用于提取给定路径的目录部分。它返回指定文件路径中去掉文件名后的部分，通常用于脚本和命令行操作中，以便处理文件路径。

## 用法
基本语法如下：
```
dirname [options] [arguments]
```

## 常用选项
- `-z`：在输出中使用空字符串代替空路径。
- `--help`：显示帮助信息。
- `--version`：显示版本信息。

## 常见示例
以下是一些常见的 `dirname` 使用示例：

1. 获取单个文件路径的目录部分：
   ```bash
   dirname /home/user/documents/file.txt
   ```
   输出：
   ```
   /home/user/documents
   ```

2. 处理相对路径：
   ```bash
   dirname ./folder/file.txt
   ```
   输出：
   ```
   ./folder
   ```

3. 从多个路径中提取目录部分：
   ```bash
   dirname /var/log/syslog /etc/hosts
   ```
   输出：
   ```
   /var/log
   /etc
   ```

4. 结合其他命令使用：
   ```bash
   dirname $(which bash)
   ```
   输出：
   ```
   /usr/bin
   ```

## 提示
- 使用 `dirname` 时，可以与其他命令结合使用，以便动态获取文件路径。
- 注意处理相对路径和绝对路径的区别，确保得到预期的结果。
- 在脚本中使用 `dirname` 时，可以将其输出赋值给变量，以便后续操作。