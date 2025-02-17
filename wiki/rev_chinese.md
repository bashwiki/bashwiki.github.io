# [Linux] Bash rev 命令: 反转每一行的字符

## 概述
`rev` 命令用于反转输入文本的每一行字符。它可以处理来自文件或标准输入的文本，并将每一行的字符顺序颠倒。

## 用法
基本语法如下：
```
rev [选项] [参数]
```

## 常用选项
- `-o, --output=FILE`：将输出写入指定的文件，而不是标准输出。
- `-h, --help`：显示帮助信息并退出。
- `-V, --version`：显示版本信息并退出。

## 常见示例
1. 反转标准输入的文本：
   ```bash
   echo "Hello World" | rev
   ```
   输出：
   ```
   dlroW olleH
   ```

2. 反转文件内容：
   ```bash
   rev filename.txt
   ```

3. 将反转的内容输出到新文件：
   ```bash
   rev filename.txt -o reversed.txt
   ```

4. 处理多行文本：
   ```bash
   cat <<EOF | rev
   Line 1
   Line 2
   Line 3
   EOF
   ```
   输出：
   ```
   1 eniL
   2 eniL
   3 eniL
   ```

## 提示
- 使用 `rev` 时，可以通过管道将其与其他命令结合使用，例如 `grep` 或 `sort`，以实现更复杂的文本处理。
- 确保输入的文本格式正确，`rev` 只会反转字符，不会处理文本的其他格式或结构。
- 在处理大文件时，考虑使用 `-o` 选项将输出直接写入文件，以避免在终端中显示大量数据。