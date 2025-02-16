# [Linux] Bash dirs 用法: 顯示目錄堆疊

## Overview
`dirs` 命令用於顯示當前的目錄堆疊。它可以幫助用戶查看在 Bash 環境中使用 `pushd` 和 `popd` 命令所管理的目錄列表。

## Usage
基本語法如下：
```bash
dirs [options] [arguments]
```

## Common Options
- `-l`：以完整路徑顯示目錄。
- `-p`：以簡短格式顯示目錄堆疊。

## Common Examples
1. 顯示當前目錄堆疊：
   ```bash
   dirs
   ```

2. 顯示完整路徑的目錄堆疊：
   ```bash
   dirs -l
   ```

3. 顯示簡短格式的目錄堆疊：
   ```bash
   dirs -p
   ```

## Tips
- 使用 `pushd` 命令來將目錄添加到堆疊，然後可以使用 `dirs` 查看當前堆疊狀態。
- 結合 `popd` 命令可以方便地在目錄之間切換，並使用 `dirs` 來確認當前的目錄堆疊。