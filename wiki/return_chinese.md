# [Linux] Bash return 用法等价: 返回函数的退出状态

## 概述
`return` 命令用于在 Bash 脚本或函数中返回一个退出状态。它通常用于指示函数的执行结果，0 表示成功，非零值表示错误或特定的状态。

## 用法
基本语法如下：
```bash
return [n]
```
其中 `n` 是要返回的退出状态码，范围通常是 0 到 255。

## 常用选项
- `n`：指定要返回的退出状态码。默认情况下，如果不指定，`return` 将返回函数的最后一个命令的退出状态。

## 常见示例
1. 返回成功状态：
   ```bash
   my_function() {
       echo "Function executed successfully."
       return 0
   }
   my_function
   ```

2. 返回错误状态：
   ```bash
   my_function() {
       echo "An error occurred."
       return 1
   }
   my_function
   ```

3. 使用返回值进行条件判断：
   ```bash
   my_function() {
       return 2
   }
   my_function
   if [ $? -eq 2 ]; then
       echo "Function returned 2."
   fi
   ```

4. 在脚本中使用 return：
   ```bash
   #!/bin/bash
   my_function() {
       return 5
   }
   my_function
   echo "Returned status: $?"
   ```

## 提示
- 在函数中使用 `return` 时，确保在函数内部调用，而不是在全局上下文中。
- 使用 `$?` 来获取上一个命令或函数的返回状态。
- 在调试时，可以使用 `set -x` 来查看函数执行的详细信息，帮助理解返回状态的来源。