# [Linux] Bash selinuxenabled 用法: 检查 SELinux 状态

## 概述
`selinuxenabled` 命令用于检查系统中 SELinux（安全增强 Linux）的状态。它可以快速判断 SELinux 是否启用，返回相应的状态码。

## 用法
基本语法如下：
```bash
selinuxenabled [options] [arguments]
```

## 常用选项
- `-h`, `--help`：显示帮助信息。
- `-V`, `--version`：显示版本信息。

## 常见示例
1. 检查 SELinux 是否启用：
   ```bash
   selinuxenabled
   ```
   如果返回值为 0，表示 SELinux 启用；如果返回值为 1，表示未启用。

2. 查看帮助信息：
   ```bash
   selinuxenabled --help
   ```

3. 查看版本信息：
   ```bash
   selinuxenabled --version
   ```

## 提示
- 在进行系统安全配置时，确保了解 SELinux 的状态，以便做出相应的调整。
- 使用 `selinuxenabled` 命令时，可以结合其他命令进行脚本编写，以自动化安全检查过程。