# [Linux] Bash egrep 用法: 用于模式匹配的工具

## 概述
`egrep` 是一个用于在文件中搜索文本的命令行工具，它支持扩展的正则表达式。与 `grep` 相比，`egrep` 允许使用更复杂的模式匹配，使得文本搜索更加灵活和强大。

## 用法
基本语法如下：
```
egrep [选项] [参数]
```

## 常用选项
- `-i`：忽略大小写。
- `-v`：反向匹配，显示不符合模式的行。
- `-c`：仅输出匹配行的计数。
- `-n`：在输出中显示行号。
- `-r` 或 `-R`：递归搜索目录中的文件。

## 常见示例
1. **基本文本搜索**
   ```bash
   egrep "hello" file.txt
   ```
   在 `file.txt` 中查找包含 "hello" 的行。

2. **忽略大小写**
   ```bash
   egrep -i "hello" file.txt
   ```
   在 `file.txt` 中查找包含 "hello" 或 "HELLO" 的行。

3. **反向匹配**
   ```bash
   egrep -v "hello" file.txt
   ```
   显示 `file.txt` 中不包含 "hello" 的所有行。

4. **显示行号**
   ```bash
   egrep -n "hello" file.txt
   ```
   在输出中显示包含 "hello" 的行及其行号。

5. **递归搜索**
   ```bash
   egrep -r "hello" /path/to/directory
   ```
   在指定目录及其子目录中查找包含 "hello" 的文件。

## 提示
- 使用 `-i` 选项可以提高搜索的灵活性，尤其是在处理用户输入时。
- 结合使用 `-n` 和 `-c` 选项，可以快速了解匹配模式的分布情况。
- 在处理大文件时，可以考虑使用 `less` 命令与 `egrep` 结合，以便于浏览长输出。