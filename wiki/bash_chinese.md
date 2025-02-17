# [Linux] Bash bash 使用: 执行命令行指令

## 概述
Bash 是一种命令行解释器，允许用户在类 Unix 操作系统中执行命令和脚本。它是 Linux 和 macOS 系统中最常用的 shell 之一，提供了强大的功能来管理文件、执行程序和自动化任务。

## 使用方法
基本语法如下：
```bash
bash [选项] [参数]
```

## 常用选项
- `-c`：从字符串中读取命令并执行。
- `-i`：以交互模式运行 Bash。
- `-l`：以登录 shell 模式启动 Bash。
- `-s`：从标准输入读取命令。

## 常见示例
1. **执行一个简单的命令**
   ```bash
   bash -c "echo Hello, World!"
   ```

2. **以交互模式启动 Bash**
   ```bash
   bash -i
   ```

3. **从文件中执行命令**
   ```bash
   bash script.sh
   ```

4. **在登录模式下启动 Bash**
   ```bash
   bash -l
   ```

## 提示
- 使用 `bash -i` 进入交互模式时，可以直接输入命令并查看输出。
- 在编写脚本时，确保文件具有可执行权限，可以使用 `chmod +x script.sh` 命令。
- 使用 `bash -c` 可以方便地在其他脚本或程序中执行 Bash 命令。