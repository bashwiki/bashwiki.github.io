# [Linux] Bash umask 用法: 设置默认文件权限

## 概述
`umask` 命令用于设置新创建文件和目录的默认权限掩码。它决定了在创建文件时，哪些权限将被禁止，从而影响文件的可访问性。

## 用法
基本语法如下：
```
umask [选项] [参数]
```

## 常用选项
- `-S`：以符号方式显示当前的 umask 值。
- `-p`：以可读的方式显示当前的 umask 值，适用于脚本和其他命令。

## 常见示例
1. 查看当前 umask 值：
   ```bash
   umask
   ```

2. 设置 umask 值为 022（新文件权限为 644，目录权限为 755）：
   ```bash
   umask 022
   ```

3. 使用符号方式查看当前 umask 值：
   ```bash
   umask -S
   ```

4. 临时设置 umask 值并创建文件：
   ```bash
   (umask 007; touch myfile)
   ```

## 提示
- 在脚本中设置 umask 值可以确保文件权限的一致性。
- 使用 umask 022 可以确保新创建的文件对其他用户可读，但不可写。
- 定期检查 umask 值，以确保其符合安全策略。