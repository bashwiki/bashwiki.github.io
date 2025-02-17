# [Linux] Bash printf 用法: 格式化输出文本

## 概述
`printf` 命令用于格式化输出文本。它允许用户根据指定的格式将数据输出到标准输出或文件中，类似于 C 语言中的 `printf` 函数。

## 用法
基本语法如下：
```bash
printf [options] [arguments]
```

## 常用选项
- `-v name`：将输出赋值给变量 `name`。
- `--help`：显示帮助信息。
- `--version`：显示版本信息。

## 常见示例
以下是一些常用的 `printf` 示例：

1. **输出简单文本**
   ```bash
   printf "Hello, World!\n"
   ```

2. **格式化数字**
   ```bash
   printf "Number: %d\n" 42
   ```

3. **输出浮点数**
   ```bash
   printf "Pi: %.2f\n" 3.14159
   ```

4. **输出多个变量**
   ```bash
   name="Alice"
   age=30
   printf "%s is %d years old.\n" "$name" "$age"
   ```

5. **输出带填充的字符串**
   ```bash
   printf "|%10s|\n" "test"  # 右对齐
   printf "|%-10s|\n" "test"  # 左对齐
   ```

## 提示
- 使用 `\n` 来换行，确保输出格式整齐。
- 可以使用 `%` 符号指定格式，例如 `%s` 表示字符串，`%d` 表示整数。
- 对于复杂的输出，考虑使用变量来提高可读性和可维护性。