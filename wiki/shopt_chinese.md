# [Linux] Bash shopt 用法: 配置 Bash 选项

## Overview
`shopt` 是一个用于设置和取消设置 Bash shell 选项的命令。通过使用 `shopt`，用户可以启用或禁用特定的 shell 功能，以自定义其工作环境。

## Usage
基本语法如下：
```bash
shopt [options] [arguments]
```

## Common Options
- `-s`：设置选项（启用）。
- `-u`：取消设置选项（禁用）。
- `-p`：显示当前所有选项及其状态。

## Common Examples
1. **启用扩展的通配符匹配**：
   ```bash
   shopt -s extglob
   ```
   这将允许使用扩展的通配符，如 `+(pattern)` 和 `?(pattern)`。

2. **禁用自动补全**：
   ```bash
   shopt -u progcomp
   ```
   这将关闭 Bash 的程序补全功能。

3. **查看所有选项及其状态**：
   ```bash
   shopt -p
   ```
   这将列出所有可用的选项及其当前设置状态。

4. **启用文件名扩展**：
   ```bash
   shopt -s globstar
   ```
   这将允许使用 `**` 来匹配任意数量的目录。

## Tips
- 在修改选项之前，可以使用 `shopt -p` 查看当前设置，以避免意外更改。
- 通过在 `.bashrc` 文件中添加 `shopt` 命令，可以在每次启动 Bash 时自动应用这些设置。
- 使用 `shopt` 时要小心，某些选项可能会改变脚本的行为，确保在测试环境中验证更改。