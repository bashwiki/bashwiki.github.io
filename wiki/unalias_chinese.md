# [Linux] Bash unalias 用法: 取消别名

## 概述
`unalias` 命令用于取消之前设置的命令别名。别名是用户为命令设置的简短名称，使用 `unalias` 可以删除这些别名，使得原始命令可以被恢复使用。

## 用法
基本语法如下：
```
unalias [选项] [参数]
```

## 常用选项
- `-a`：取消所有别名。
- `-p`：打印当前所有别名的列表。

## 常见示例
1. 取消一个特定的别名：
   ```bash
   unalias ll
   ```

2. 取消多个别名：
   ```bash
   unalias ll rm
   ```

3. 取消所有别名：
   ```bash
   unalias -a
   ```

4. 打印当前所有别名：
   ```bash
   unalias -p
   ```

## 提示
- 在使用 `unalias` 之前，可以使用 `alias` 命令查看当前设置的别名，以避免误取消。
- 如果希望在每次启动终端时都取消某些别名，可以将 `unalias` 命令添加到你的 shell 配置文件中，如 `.bashrc` 或 `.bash_profile`。