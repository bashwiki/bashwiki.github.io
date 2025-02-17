# [Linux] Bash export 用法: 设置环境变量

## 概述
`export` 命令用于设置或标记环境变量，使其在当前 shell 会话及其子进程中可用。通过使用 `export`，用户可以将变量的值传递给其他程序或脚本。

## 用法
基本语法如下：
```bash
export [options] [arguments]
```

## 常用选项
- `-p`：显示所有已导出的环境变量及其值。
- `-n`：取消导出指定的变量，使其不再在子进程中可用。

## 常见示例
1. **导出一个变量**
   ```bash
   MY_VAR="Hello, World!"
   export MY_VAR
   ```

2. **直接在导出时赋值**
   ```bash
   export MY_VAR="Hello, World!"
   ```

3. **查看所有导出的变量**
   ```bash
   export -p
   ```

4. **取消导出一个变量**
   ```bash
   export -n MY_VAR
   ```

5. **在同一行中导出并执行命令**
   ```bash
   export MY_VAR="Hello" && echo $MY_VAR
   ```

## 提示
- 在导出变量时，确保变量名遵循命名规则（只能包含字母、数字和下划线，且不能以数字开头）。
- 使用 `export -p` 可以快速查看当前所有导出的环境变量，方便调试。
- 在脚本中使用 `export` 可以确保变量在子进程中可用，避免出现未定义变量的错误。