# [Linux] Bash help 使用說明: 獲取命令的幫助資訊

## Overview
`help` 命令用於顯示 Bash 內建命令的幫助資訊。這對於了解如何使用特定命令或查詢其選項非常有用。

## Usage
基本語法如下：
```
help [options] [arguments]
```

## Common Options
- `-d`：顯示命令的簡短描述。
- `-m`：以可讀性較高的格式顯示幫助資訊。
- `-s`：僅顯示命令的簡短說明，不顯示詳細資訊。

## Common Examples
以下是一些實用的範例：

1. 獲取 `cd` 命令的幫助資訊：
   ```bash
   help cd
   ```

2. 獲取 `echo` 命令的簡短說明：
   ```bash
   help -d echo
   ```

3. 獲取所有內建命令的列表：
   ```bash
   help
   ```

4. 以可讀性較高的格式顯示 `set` 命令的幫助資訊：
   ```bash
   help -m set
   ```

## Tips
- 使用 `help` 命令可以快速了解內建命令的用法，而不需要查閱外部文檔。
- 如果你不確定某個命令的具體用法，先試試 `help`，這樣可以節省時間。
- 結合 `man` 命令來獲取更詳細的資訊，特別是對於外部命令。