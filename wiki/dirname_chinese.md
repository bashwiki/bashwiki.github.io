# [리눅스] Bash dirname 사용법

## 概述
`dirname` 是一个用于处理文件路径的 Bash 命令。它的主要功能是从给定的文件路径中提取目录部分，返回路径中最后一个斜杠（/）之前的部分。这对于在脚本中处理文件路径时非常有用，尤其是在需要分离文件名和目录时。

## 用法
基本语法如下：
```bash
dirname [路径]
```
### 常用选项
- `-z`：如果路径为空，则返回空字符串。
- `--help`：显示帮助信息并退出。
- `--version`：显示版本信息并退出。

## 示例
以下是两个使用 `dirname` 命令的实际示例：

### 示例 1：提取目录路径
```bash
$ dirname /home/user/documents/file.txt
/home/user/documents
```
在这个例子中，`dirname` 提取了文件 `file.txt` 的目录路径。

### 示例 2：处理相对路径
```bash
$ dirname ./projects/my_project/main.py
./projects/my_project
```
在这个例子中，`dirname` 从相对路径中提取了目录部分。

## 提示
- 使用 `dirname` 时，确保提供有效的路径，以避免意外的空输出。
- 可以将 `dirname` 与其他命令结合使用，例如 `basename`，以便在脚本中更灵活地处理文件路径。
- 在处理多个路径时，可以使用循环来逐个处理每个路径，确保脚本的可读性和可维护性。