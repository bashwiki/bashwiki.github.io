# [Linux] Bash awk 用法: 文本处理工具

## 概述
`awk` 是一个强大的文本处理工具，主要用于模式扫描和处理。它可以对文本文件中的数据进行分析、格式化和报告生成，特别适合处理结构化数据，如 CSV 文件。

## 用法
基本语法如下：
```bash
awk [options] 'pattern { action }' [file...]
```

## 常用选项
- `-F` : 指定字段分隔符，默认为空格。
- `-v` : 定义变量，便于在脚本中使用。
- `-f` : 从文件中读取 awk 脚本。
- `-e` : 直接在命令行中执行 awk 脚本。

## 常见示例
1. **打印文件的第一列**
   ```bash
   awk '{print $1}' filename.txt
   ```

2. **使用自定义分隔符**
   ```bash
   awk -F ',' '{print $1}' filename.csv
   ```

3. **条件筛选**
   ```bash
   awk '$3 > 50 {print $1, $2}' filename.txt
   ```

4. **计算总和**
   ```bash
   awk '{sum += $1} END {print sum}' filename.txt
   ```

5. **格式化输出**
   ```bash
   awk '{printf "Name: %s, Age: %d\n", $1, $2}' filename.txt
   ```

## 小贴士
- 使用 `-F` 选项可以轻松处理不同格式的文件。
- 在处理大型文件时，尽量使用 `awk` 的内置变量和函数，以提高效率。
- 通过将常用的 awk 脚本保存到文件中，可以简化重复操作。