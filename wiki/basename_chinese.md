# [리눅스] Bash basename 사용법

## 概述
`basename` 是一个用于处理文件路径的 Bash 命令。它的主要目的是从给定的路径中提取出文件名部分，去掉路径前缀和可选的后缀。这在脚本中非常有用，尤其是在需要处理文件名而不关心其完整路径时。

## 用法
基本语法如下：
```bash
basename [路径] [后缀]
```
- **路径**: 需要处理的文件路径。
- **后缀**: 可选参数，如果提供，`basename` 会在返回文件名之前去掉这个后缀。

## 示例
以下是一些实际使用 `basename` 的示例：

1. 提取文件名：
   ```bash
   basename /usr/local/bin/script.sh
   ```
   输出：
   ```
   script.sh
   ```

2. 提取文件名并去掉后缀：
   ```bash
   basename /usr/local/bin/script.sh .sh
   ```
   输出：
   ```
   script
   ```

## 提示
- 使用 `basename` 时，确保路径是有效的，以避免意外的错误。
- 如果你只想获取文件名而不需要去掉后缀，可以省略第二个参数。
- 在处理多个文件时，可以结合 `for` 循环使用 `basename`，例如：
  ```bash
  for file in /path/to/files/*; do
      echo $(basename "$file")
  done
  ```
  这将列出指定目录下所有文件的文件名。