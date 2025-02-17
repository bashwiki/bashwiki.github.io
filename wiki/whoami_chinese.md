# [Linux] Bash whoami 用法: 显示当前用户的用户名

## 概述
`whoami` 命令用于显示当前登录用户的用户名。它是一个非常简单但实用的命令，常用于确认你以哪个用户身份在系统中操作。

## 用法
基本语法如下：
```bash
whoami [选项] [参数]
```

## 常用选项
- `--help`：显示帮助信息。
- `--version`：显示版本信息。

## 常见示例
1. **显示当前用户的用户名**
   ```bash
   whoami
   ```
   输出示例：
   ```
   username
   ```

2. **显示帮助信息**
   ```bash
   whoami --help
   ```
   输出示例：
   ```
   Usage: whoami [OPTION]
   Print the effective username of the current user.
   ```

3. **显示版本信息**
   ```bash
   whoami --version
   ```
   输出示例：
   ```
   whoami (GNU coreutils) 8.32
   ```

## 提示
- 使用 `whoami` 可以快速确认当前用户，特别是在使用多个用户账户时。
- 结合其他命令使用，例如 `sudo whoami`，可以查看以超级用户身份执行命令时的用户名。
- 在脚本中使用 `whoami` 可以帮助调试和记录当前用户的操作。