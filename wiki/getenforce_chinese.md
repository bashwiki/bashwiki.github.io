# [Linux] Bash getenforce 用法: 查询SELinux状态

## 概述
`getenforce` 命令用于查询当前系统的SELinux（安全增强Linux）状态。它可以帮助用户了解系统的安全策略是否处于启用、宽松或禁用状态。

## 用法
基本语法如下：
```
getenforce [options] [arguments]
```

## 常用选项
`getenforce` 命令没有特别的选项，主要用于直接查询状态。返回的结果有三种：
- `Enforcing`：表示SELinux处于强制模式。
- `Permissive`：表示SELinux处于宽松模式。
- `Disabled`：表示SELinux已禁用。

## 常见示例
以下是一些使用 `getenforce` 的示例：

1. 查询当前SELinux状态：
   ```bash
   getenforce
   ```

2. 将结果存储在变量中：
   ```bash
   status=$(getenforce)
   echo "当前SELinux状态是: $status"
   ```

3. 在脚本中使用 `getenforce` 进行条件判断：
   ```bash
   if [ "$(getenforce)" = "Enforcing" ]; then
       echo "SELinux处于强制模式"
   else
       echo "SELinux不处于强制模式"
   fi
   ```

## 提示
- 定期检查SELinux状态，以确保系统安全。
- 在进行系统配置或安装新软件时，注意SELinux的状态可能会影响操作。
- 如果需要更改SELinux状态，可以使用 `setenforce` 命令，但请确保了解其影响。