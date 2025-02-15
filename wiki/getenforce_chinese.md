# [리눅스] Bash getenforce 사용법

## 概述
`getenforce` 是一个用于查询当前 SELinux（安全增强 Linux）状态的命令。SELinux 是一种 Linux 内核安全模块，它提供了一种强制访问控制机制。通过 `getenforce` 命令，用户可以快速了解系统当前的安全策略模式，主要有三种状态：Enforcing（强制）、Permissive（宽容）和Disabled（禁用）。

## 用法
基本语法如下：
```bash
getenforce
```

该命令没有复杂的选项，执行后将返回当前 SELinux 的状态。

## 示例
以下是使用 `getenforce` 命令的两个实际示例：

1. **查询当前 SELinux 状态**：
   ```bash
   getenforce
   ```
   执行此命令后，您可能会看到以下输出之一：
   - `Enforcing`：表示 SELinux 正在强制执行安全策略。
   - `Permissive`：表示 SELinux 处于宽容模式，不会阻止任何操作，但会记录违规行为。
   - `Disabled`：表示 SELinux 已被禁用。

2. **在脚本中使用**：
   您可以在 Bash 脚本中使用 `getenforce` 来检查 SELinux 状态并根据状态执行不同的操作。例如：
   ```bash
   #!/bin/bash
   status=$(getenforce)
   if [ "$status" == "Enforcing" ]; then
       echo "SELinux is enforcing."
   else
       echo "SELinux is not enforcing."
   fi
   ```

## 提示
- 在进行系统安全配置时，了解 SELinux 的状态非常重要。建议定期检查 SELinux 状态，以确保系统的安全性。
- 如果您在开发或测试环境中遇到权限问题，可以临时将 SELinux 设置为 `Permissive` 模式，以便更轻松地调试问题，但请确保在生产环境中将其设置回 `Enforcing` 模式以保持安全性。
- 使用 `getenforce` 命令时，确保您具有足够的权限来查询 SELinux 状态，通常需要以 root 用户或具有相应权限的用户身份运行。