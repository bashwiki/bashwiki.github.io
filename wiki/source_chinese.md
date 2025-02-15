# [리눅스] Bash source 사용법

## 概述
`source` 命令是 Bash 中用于在当前 shell 环境中执行脚本文件的命令。它的主要目的是使得脚本中的变量和函数在当前 shell 会话中可用，而不是在子 shell 中执行。通过使用 `source`，用户可以加载配置文件、环境变量或自定义函数，而无需退出当前的 shell 会话。

## 用法
基本语法如下：
```bash
source 文件名
```
或者使用点（`.`）命令，效果相同：
```bash
. 文件名
```

### 常见选项
`source` 命令本身没有特别的选项，但它可以与其他命令结合使用，以实现更复杂的功能。例如，您可以在脚本中使用 `source` 来加载其他脚本文件。

## 示例
### 示例 1：加载环境变量
假设您有一个名为 `env.sh` 的脚本文件，其中定义了一些环境变量：
```bash
# env.sh
export MY_VAR="Hello, World!"
```
您可以使用 `source` 命令加载这个文件：
```bash
source env.sh
echo $MY_VAR
```
输出将是：
```
Hello, World!
```

### 示例 2：加载函数
您还可以使用 `source` 来加载包含函数的脚本。例如，假设您有一个名为 `functions.sh` 的文件：
```bash
# functions.sh
greet() {
    echo "Hello, $1!"
}
```
您可以通过以下命令加载并使用这个函数：
```bash
source functions.sh
greet "Alice"
```
输出将是：
```
Hello, Alice!
```

## 提示
- 使用 `source` 命令时，请确保脚本文件的路径正确。如果脚本不在当前目录中，您需要提供完整路径或相对路径。
- 如果您希望在脚本中使用 `source` 加载其他脚本，确保这些脚本的权限设置为可执行。
- 在调试脚本时，可以使用 `set -x` 命令来跟踪 `source` 命令的执行过程，帮助您发现潜在的问题。

通过使用 `source` 命令，您可以更灵活地管理和组织您的 Bash 环境，提高开发效率。