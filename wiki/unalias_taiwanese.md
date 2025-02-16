# [台灣] Bash unalias 使用法: 移除別名

## Overview
`unalias` 命令用於移除先前設定的命令別名。當你不再需要某個別名，或希望恢復原始命令的行為時，可以使用此命令。

## Usage
基本語法如下：
```
unalias [選項] [參數]
```

## Common Options
- `-a`：移除所有別名。
- `-p`：顯示當前所有別名的列表。

## Common Examples
以下是一些常見的使用範例：

1. 移除特定別名：
   ```bash
   unalias ll
   ```

2. 移除所有別名：
   ```bash
   unalias -a
   ```

3. 顯示當前所有別名：
   ```bash
   unalias -p
   ```

## Tips
- 在使用 `unalias` 之前，建議先使用 `alias` 命令查看目前設定的別名，以避免意外移除重要的別名。
- 如果你希望在每次啟動終端時自動移除某些別名，可以將 `unalias` 命令加入到你的 shell 配置檔（例如 `.bashrc` 或 `.bash_profile`）中。