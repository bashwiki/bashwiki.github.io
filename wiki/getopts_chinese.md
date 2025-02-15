# [리눅스] Bash getopts 사용법

## 概述
`getopts` 是一个用于解析命令行选项的 Bash 内置命令。它的主要目的是帮助脚本开发者处理传递给脚本的选项和参数，使得脚本能够更灵活地接受用户输入。通过使用 `getopts`，开发者可以轻松地定义和管理短选项（如 `-a`）和长选项（如 `--option`），并且可以为每个选项指定相应的参数。

## 用法
`getopts` 的基本语法如下：

```bash
getopts "options" variable
```

- `options`：一个字符串，定义了可接受的选项及其参数。每个选项后面可以跟一个冒号（`:`），表示该选项需要一个参数。
- `variable`：用于存储当前选项的变量名。

### 常见选项
- `:`：如果选项后面跟着冒号，表示该选项需要一个参数。
- `?`：如果遇到未知选项，`getopts` 会将其存储到变量中，并且可以通过条件语句进行处理。

## 示例
以下是一些使用 `getopts` 的实际示例：

### 示例 1：基本选项解析
```bash
#!/bin/bash

while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "选项 -a 被选中"
      ;;
    b)
      echo "选项 -b 被选中，参数为 '$OPTARG'"
      ;;
    c)
      echo "选项 -c 被选中，参数为 '$OPTARG'"
      ;;
    *)
      echo "无效选项"
      ;;
  esac
done
```
在这个示例中，脚本接受选项 `-a`、`-b` 和 `-c`，其中 `-b` 和 `-c` 需要参数。运行脚本时，可以使用如下命令：
```bash
./script.sh -a -b value1 -c value2
```

### 示例 2：处理未知选项
```bash
#!/bin/bash

while getopts "abc:" opt; do
  case $opt in
    a)
      echo "选项 -a 被选中"
      ;;
    b)
      echo "选项 -b 被选中"
      ;;
    c)
      echo "选项 -c 被选中，参数为 '$OPTARG'"
      ;;
    *)
      echo "无效选项: -$OPTARG"
      ;;
  esac
done
```
在这个示例中，如果用户输入了无效的选项，脚本会输出相应的错误信息。

## 提示
- 在使用 `getopts` 时，确保选项字符串中每个需要参数的选项后面都加上冒号。
- 使用 `OPTARG` 变量来获取当前选项的参数值。
- 通过使用 `case` 语句，可以方便地处理不同的选项和参数。
- 如果需要处理长选项（如 `--option`），可以考虑使用 `getopt` 命令，它支持更复杂的选项解析。

通过使用 `getopts`，您可以使 Bash 脚本更加灵活和用户友好，方便用户输入参数和选项。