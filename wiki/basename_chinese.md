# [Linux] Bash basename 用法: 提取文件名

## 概述
`basename` 命令用于从给定的路径中提取文件名部分。它可以帮助用户获取文件的基本名称，而不包括路径信息。

## 用法
基本语法如下：
```bash
basename [options] [arguments]
```

## 常用选项
- `-a`：处理多个路径，返回每个路径的基本名称。
- `-s`：指定一个后缀，去掉文件名中的该后缀。

## 常见示例
以下是一些常见的 `basename` 使用示例：

1. 提取单个文件名：
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

3. 处理多个路径：
   ```bash
   basename -a /usr/local/bin/script.sh /home/user/doc.txt
   ```
   输出：
   ```
   script.sh
   doc.txt
   ```

4. 提取文件名并去掉特定后缀：
   ```bash
   basename -s .txt /home/user/doc.txt
   ```
   输出：
   ```
   doc
   ```

## 提示
- 使用 `basename` 时，可以结合其他命令（如 `find`）来处理文件列表。
- 注意处理文件名中的特殊字符时，可能需要使用引号来确保正确解析。
- 在脚本中使用 `basename` 可以提高代码的可读性，特别是在处理文件路径时。