# [리눅스] Bash export 사용법

## 概述
`export` 命令用于设置或标记环境变量，使其在当前 shell 会话及其子进程中可用。通过使用 `export`，用户可以将变量导出到环境中，以便其他程序和脚本能够访问这些变量。

## 用法
基本语法如下：
```bash
export VARIABLE_NAME=value
```
- `VARIABLE_NAME`：要设置的环境变量的名称。
- `value`：环境变量的值。

如果只想将现有变量导出而不赋值，可以使用：
```bash
export VARIABLE_NAME
```

### 常用选项
- `-n`：取消导出指定的变量。
- `-p`：显示所有已导出的环境变量。

## 示例
### 示例 1：设置并导出变量
```bash
export MY_VAR="Hello, World!"
```
在这个例子中，我们创建了一个名为 `MY_VAR` 的环境变量，并将其值设置为 "Hello, World!"。此后，`MY_VAR` 可以在当前 shell 会话及其子进程中使用。

### 示例 2：导出现有变量
```bash
MY_VAR="Hello, World!"
export MY_VAR
```
在这个例子中，我们首先设置了一个变量 `MY_VAR`，然后使用 `export` 命令将其导出。这样，`MY_VAR` 将在当前 shell 会话及其子进程中可用。

## 提示
- 在脚本中使用 `export` 时，请确保在脚本的开头设置变量，以便在整个脚本中都能访问。
- 使用 `export -p` 可以查看当前所有已导出的环境变量，这对于调试非常有用。
- 尽量避免使用与系统保留的环境变量相同的名称，以免引起混淆或错误。