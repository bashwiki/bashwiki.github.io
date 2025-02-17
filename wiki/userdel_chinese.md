# [Linux] Bash userdel 用法: 删除用户账户

## 概述
`userdel` 命令用于删除 Linux 系统中的用户账户。使用此命令可以有效地移除不再需要的用户及其相关文件。

## 用法
基本语法如下：
```
userdel [options] [arguments]
```

## 常用选项
- `-r`：同时删除用户的主目录及其文件。
- `-f`：强制删除用户，即使用户当前正在登录。
- `-Z`：在删除用户时，保留 SELinux 上下文。

## 常见示例
1. 删除用户但保留主目录：
   ```bash
   userdel username
   ```

2. 删除用户及其主目录：
   ```bash
   userdel -r username
   ```

3. 强制删除正在登录的用户：
   ```bash
   userdel -f username
   ```

4. 删除用户并保留 SELinux 上下文：
   ```bash
   userdel -Z username
   ```

## 提示
- 在删除用户之前，确保备份重要数据，以免丢失。
- 使用 `-f` 选项时要小心，因为这可能会影响正在使用该账户的进程。
- 定期检查系统用户列表，及时清理不再使用的账户。