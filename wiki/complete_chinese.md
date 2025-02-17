# [Linux] Bash 完整命令：自动补全命令

## 概述
`complete` 命令用于为 Bash shell 中的命令提供自动补全功能。通过定义特定命令的补全规则，用户可以更高效地输入命令和参数。

## 用法
基本语法如下：
```bash
complete [options] [arguments]
```

## 常用选项
- `-A`：指定补全类型，例如文件名、用户等。
- `-o`：添加选项，例如 `default`，表示默认补全。
- `-F`：指定一个函数，用于生成补全的内容。

## 常见示例
1. 为 `git` 命令添加文件名补全：
   ```bash
   complete -o default -A file git
   ```

2. 为自定义命令 `mycmd` 添加补全：
   ```bash
   _mycmd_completions() {
       local commands="start stop restart"
       COMPREPLY=( $(compgen -W "$commands" -- "${COMP_WORDS[1]}") )
   }
   complete -F _mycmd_completions mycmd
   ```

3. 为 `ssh` 命令添加用户补全：
   ```bash
   complete -A user ssh
   ```

## 小贴士
- 在使用 `complete` 时，确保你了解要补全的命令及其参数。
- 可以通过创建自定义补全函数来实现复杂的补全逻辑。
- 定期检查和更新补全规则，以适应新的命令或参数变化。