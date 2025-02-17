# [Linux] Bash tee 用法: 将输出重定向到文件和标准输出

## 概述
`tee` 命令用于从标准输入读取数据，并将其同时输出到标准输出和一个或多个文件中。这使得用户能够在查看输出的同时将其保存到文件中。

## 用法
基本语法如下：
```bash
tee [选项] [文件...]
```

## 常用选项
- `-a`：以追加模式写入文件，而不是覆盖文件。
- `-i`：忽略中断信号。
- `--help`：显示帮助信息。

## 常见示例
1. 将输出保存到文件：
   ```bash
   echo "Hello, World!" | tee output.txt
   ```
   这条命令将 "Hello, World!" 输出到标准输出，并同时保存到 `output.txt` 文件中。

2. 追加输出到文件：
   ```bash
   echo "Another line" | tee -a output.txt
   ```
   使用 `-a` 选项将 "Another line" 追加到 `output.txt` 文件中，而不是覆盖它。

3. 同时输出到多个文件：
   ```bash
   echo "Data for multiple files" | tee file1.txt file2.txt
   ```
   这条命令将输出同时写入 `file1.txt` 和 `file2.txt`。

4. 从命令输出中使用 tee：
   ```bash
   ls -l | tee directory_listing.txt
   ```
   这条命令将 `ls -l` 的输出显示在终端，并保存到 `directory_listing.txt` 文件中。

## 小贴士
- 使用 `tee` 时，可以结合管道命令，方便地处理和保存数据。
- 注意文件权限，确保您有权限写入目标文件。
- 在使用 `-a` 选项时，确保您了解文件内容，以避免意外追加不必要的数据。