# [Linux] Bash useradd 用法: 创建新用户

## 概述
`useradd` 命令用于在 Linux 系统中创建新用户账户。它是系统管理员管理用户的基本工具之一，允许用户设置账户的基本属性。

## 用法
基本语法如下：
```bash
useradd [options] [arguments]
```

## 常用选项
- `-m`：创建用户的主目录。
- `-s`：指定用户的登录 shell。
- `-G`：将用户添加到指定的附加组。
- `-d`：指定用户的主目录路径。
- `-e`：设置用户账户的到期日期。

## 常见示例
1. 创建一个新用户并自动创建主目录：
   ```bash
   useradd -m newuser
   ```

2. 创建一个用户并指定登录 shell：
   ```bash
   useradd -m -s /bin/bash newuser
   ```

3. 创建一个用户并将其添加到多个附加组：
   ```bash
   useradd -m -G wheel,developers newuser
   ```

4. 创建一个用户并指定主目录：
   ```bash
   useradd -d /home/customuser -m customuser
   ```

5. 创建一个用户并设置账户到期日期：
   ```bash
   useradd -e 2023-12-31 newuser
   ```

## 小贴士
- 在创建用户后，通常需要使用 `passwd` 命令为用户设置密码。
- 使用 `-m` 选项时，确保系统的 `/etc/skel` 目录中有默认文件，以便新用户的主目录可以正确初始化。
- 定期检查用户账户的有效性和安全性，避免不必要的账户存在。