# [Linux] Bash readonly 用法: 设置只读变量

## 概述
`readonly` 命令用于将变量设置为只读状态。一旦变量被标记为只读，就不能再被修改或删除。这在脚本中非常有用，可以防止意外更改重要的变量值。

## 用法
基本语法如下：
```bash
readonly [options] [arguments]
```

## 常用选项
- `-p`：显示所有只读变量及其值。

## 常见示例

### 示例 1: 创建只读变量
```bash
readonly MY_VAR="Hello, World!"
```
此命令创建一个名为 `MY_VAR` 的只读变量，值为 "Hello, World!"。

### 示例 2: 尝试修改只读变量
```bash
MY_VAR="New Value"  # 这将会失败，提示错误
```
尝试修改 `MY_VAR` 的值会导致错误，因为它是只读的。

### 示例 3: 显示所有只读变量
```bash
readonly -p
```
此命令将列出当前所有的只读变量及其值。

## 小贴士
- 在脚本开始时设置重要的变量为只读，以避免后续代码意外修改。
- 使用 `readonly` 时，确保变量的初始值是正确的，因为一旦设置为只读，将无法更改。
- 结合使用 `declare -r` 也可以创建只读变量，语法为 `declare -r VAR_NAME="value"`。