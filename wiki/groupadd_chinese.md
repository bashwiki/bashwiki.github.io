# [Linux] Bash groupadd 用法: 创建新用户组

## 概述
`groupadd` 命令用于在 Linux 系统中创建新的用户组。用户组是管理用户权限和访问控制的重要工具，能够帮助系统管理员更好地组织和管理用户。

## 用法
基本语法如下：
```
groupadd [选项] [组名]
```

## 常用选项
- `-g GID`：指定新组的组标识符（GID）。
- `-r`：创建系统组，系统组的 GID 通常小于 1000。
- `-f`：如果指定的组名已存在，则不返回错误。

## 常见示例
1. 创建一个名为 `developers` 的新用户组：
   ```bash
   groupadd developers
   ```

2. 创建一个具有特定 GID 的用户组 `admins`，GID 为 2000：
   ```bash
   groupadd -g 2000 admins
   ```

3. 创建一个系统组 `sysadmins`：
   ```bash
   groupadd -r sysadmins
   ```

4. 尝试创建一个已存在的用户组 `users`，并使用 `-f` 选项避免错误：
   ```bash
   groupadd -f users
   ```

## 提示
- 在创建用户组之前，确保组名不与现有组名冲突。
- 使用 `getent group` 命令可以查看当前系统中的所有用户组。
- 为了安全起见，尽量使用系统组来管理系统服务和特权用户。