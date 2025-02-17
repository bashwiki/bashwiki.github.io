# [Linux] Bash getopts 用法: 解析命令行选项

## 概述
`getopts` 是一个用于解析命令行选项的 Bash 内置命令。它可以帮助脚本处理用户输入的选项和参数，使得脚本更加灵活和用户友好。

## 用法
基本语法如下：
```bash
getopts [options] [arguments]
```

## 常用选项
- `-a`：指定选项的字符集。
- `-d`：设置分隔符。
- `-n`：指定脚本名称。
- `-s`：静默模式，不输出错误信息。

## 常见示例
以下是一些使用 `getopts` 的实际示例：

### 示例 1: 基本选项解析
```bash
#!/bin/bash

while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "Option A is set."
      ;;
    b)
      echo "Option B is set with value: $OPTARG"
      ;;
    c)
      echo "Option C is set with value: $OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done
```

### 示例 2: 使用默认值
```bash
#!/bin/bash

value="default"

while getopts "v:" opt; do
  case $opt in
    v)
      value=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

echo "Value is: $value"
```

### 示例 3: 处理多个选项
```bash
#!/bin/bash

while getopts "abc" opt; do
  case $opt in
    a)
      echo "Option A is set."
      ;;
    b)
      echo "Option B is set."
      ;;
    c)
      echo "Option C is set."
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done
```

## 小贴士
- 在使用 `getopts` 时，确保选项字符后面有冒号（:）表示该选项需要参数。
- 使用 `OPTARG` 变量获取选项的参数值。
- 在处理无效选项时，使用 `\?` 来捕获并处理错误。
- 适当使用默认值可以提高脚本的用户体验。