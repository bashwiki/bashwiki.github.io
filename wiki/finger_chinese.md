# [Linux] Bash finger 使用方法: 显示用户信息

## 概述
`finger` 命令用于显示系统中用户的详细信息，包括用户名、登录时间、终端、空闲时间以及用户的真实姓名等。这对于了解当前系统用户的状态非常有用。

## 用法
基本语法如下：
```
finger [options] [arguments]
```

## 常用选项
- `-l`：以长格式显示用户信息。
- `-m`：仅显示匹配的用户。
- `-s`：以简短格式显示用户信息。
- `-p`：不显示用户的计划信息。

## 常见示例
1. 显示所有用户的信息：
   ```bash
   finger
   ```

2. 显示特定用户的信息：
   ```bash
   finger username
   ```

3. 以长格式显示特定用户的信息：
   ```bash
   finger -l username
   ```

4. 以简短格式显示所有用户的信息：
   ```bash
   finger -s
   ```

5. 显示匹配的用户：
   ```bash
   finger -m user*
   ```

## 小贴士
- 使用 `finger` 命令时，确保你有足够的权限查看其他用户的信息。
- 结合 `grep` 命令，可以更方便地筛选特定用户的信息，例如：
  ```bash
  finger | grep username
  ```
- 了解用户的空闲时间可以帮助系统管理员判断用户的活跃程度。