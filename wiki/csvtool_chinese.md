# [Linux] Bash csvtool 用法：处理 CSV 文件的工具

## 概述
csvtool 是一个用于处理 CSV（逗号分隔值）文件的命令行工具。它可以帮助用户轻松地提取、修改和格式化 CSV 数据。

## 用法
基本语法如下：
```bash
csvtool [options] [arguments]
```

## 常用选项
- `-c`：指定要提取的列。
- `-r`：指定要提取的行。
- `-t`：指定分隔符，默认为逗号。
- `-n`：输出行号。
- `-h`：显示帮助信息。

## 常见示例
1. 提取特定列：
   ```bash
   csvtool -c 1,3 data.csv
   ```
   这个命令将提取 `data.csv` 文件中的第 1 列和第 3 列。

2. 使用自定义分隔符：
   ```bash
   csvtool -t ";" -c 2 data.txt
   ```
   这里，`data.txt` 文件使用分号作为分隔符，命令提取第 2 列。

3. 提取特定行：
   ```bash
   csvtool -r 2-4 data.csv
   ```
   该命令将提取 `data.csv` 文件中的第 2 行到第 4 行。

4. 显示行号：
   ```bash
   csvtool -n -c 1 data.csv
   ```
   这个命令将提取第 1 列并显示行号。

## 提示
- 在处理大型 CSV 文件时，可以结合使用 `-r` 和 `-c` 选项，以减少输出数据量。
- 使用 `-h` 选项查看帮助信息，了解更多可用功能。
- 确保 CSV 文件格式正确，以避免解析错误。