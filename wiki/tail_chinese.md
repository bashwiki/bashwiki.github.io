# [Linux] Bash tail 使用方法: 查看文件末尾内容

## 概述
`tail` 命令用于显示文件的最后几行内容。它通常用于查看日志文件或大文件的末尾部分，以便快速获取最新的信息。

## 用法
基本语法如下：
```bash
tail [选项] [参数]
```

## 常用选项
- `-n <行数>`: 指定要显示的行数，默认显示最后10行。
- `-f`: 持续跟踪文件的新增内容，适用于实时查看日志。
- `-c <字节数>`: 显示文件末尾的字节数，而不是行数。

## 常见示例
1. 显示文件的最后10行（默认行为）：
   ```bash
   tail filename.txt
   ```

2. 显示文件的最后20行：
   ```bash
   tail -n 20 filename.txt
   ```

3. 实时跟踪日志文件的新增内容：
   ```bash
   tail -f /var/log/syslog
   ```

4. 显示文件末尾的最后100个字节：
   ```bash
   tail -c 100 filename.txt
   ```

## 提示
- 使用 `-f` 选项时，可以按 `Ctrl + C` 停止跟踪。
- 结合 `grep` 命令，可以过滤 `tail` 输出的内容，例如：
  ```bash
  tail -f /var/log/syslog | grep "error"
  ```
- 如果需要查看多个文件的末尾，可以将文件名一起列出：
  ```bash
  tail file1.txt file2.txt
  ```