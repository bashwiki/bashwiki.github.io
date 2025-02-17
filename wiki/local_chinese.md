# [Linux] Bash local 命令: 定义局部变量

## 概述
`local` 命令用于在 Bash 脚本或函数中定义局部变量。局部变量仅在其定义的函数或上下文中可用，避免了与全局变量的冲突。

## 用法
基本语法如下：
```bash
local [options] [name[=value]]
```

## 常用选项
- `name`: 要定义的变量名称。
- `value`: 可选的初始值。如果未提供，变量将被初始化为空。

## 常见示例
以下是一些使用 `local` 命令的实际示例：

### 示例 1: 定义一个简单的局部变量
```bash
function my_function {
    local my_var="Hello, World!"
    echo $my_var
}
my_function  # 输出: Hello, World!
echo $my_var  # 输出: (无输出，因为 my_var 是局部变量)
```

### 示例 2: 使用局部变量进行计算
```bash
function calculate {
    local num1=5
    local num2=10
    local sum=$((num1 + num2))
    echo "Sum: $sum"
}
calculate  # 输出: Sum: 15
```

### 示例 3: 在循环中使用局部变量
```bash
function loop_example {
    for ((i=1; i<=5; i++)); do
        local square=$((i * i))
        echo "Square of $i is $square"
    done
}
loop_example
```

## 提示
- 使用 `local` 定义变量可以避免意外修改全局变量，确保函数的独立性。
- 在函数内部尽量使用局部变量，以提高代码的可读性和可维护性。
- 如果需要在函数外部访问某个变量，请使用全局变量，而不是局部变量。