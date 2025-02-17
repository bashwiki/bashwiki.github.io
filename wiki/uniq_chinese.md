# [Linux] Bash uniq 用法: 去除重复行

## Overview
`uniq` 命令用于从已排序的文件或输入中去除重复的行。它通常与 `sort` 命令结合使用，以确保输入是排序的，从而有效地去除重复项。

## Usage
基本语法如下：
```
uniq [options] [arguments]
```

## Common Options
- `-c`：在输出中显示每个唯一行的出现次数。
- `-d`：仅显示重复的行。
- `-u`：仅显示唯一的行。
- `-i`：忽略大小写进行比较。

## Common Examples
1. 去除文件中的重复行：
   ```bash
   sort input.txt | uniq > output.txt
   ```

2. 显示每个唯一行的出现次数：
   ```bash
   sort input.txt | uniq -c
   ```

3. 仅显示重复的行：
   ```bash
   sort input.txt | uniq -d
   ```

4. 忽略大小写去除重复行：
   ```bash
   sort -f input.txt | uniq -i > output.txt
   ```

## Tips
- 确保在使用 `uniq` 之前对输入进行排序，以获得正确的结果。
- 使用 `-c` 选项可以帮助你快速了解每个行的出现频率。
- 在处理大文件时，可以考虑使用管道将 `sort` 和 `uniq` 结合使用，以节省内存。