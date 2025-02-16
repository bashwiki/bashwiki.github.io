# [Linux] Bash yes 用法: 自動重複輸出

## Overview
`yes` 命令用於不斷重複輸出指定的字符串，通常用於自動化腳本中以提供持續的確認或輸入。

## Usage
基本語法如下：
```
yes [options] [arguments]
```

## Common Options
- `-n`：不輸出換行符號。
- `--help`：顯示幫助信息。
- `--version`：顯示版本信息。

## Common Examples
1. **重複輸出 "y"**：
   ```bash
   yes y
   ```
   這將不斷輸出 "y"，直到手動停止。

2. **重複輸出自定義字符串**：
   ```bash
   yes "Hello, World!"
   ```
   這將不斷輸出 "Hello, World!"。

3. **將輸出重定向到文件**：
   ```bash
   yes "yes" > output.txt
   ```
   這將在 `output.txt` 文件中寫入不斷的 "yes"。

4. **與其他命令結合使用**：
   ```bash
   yes | head -n 5
   ```
   這將只顯示前五行的 "y"。

## Tips
- 使用 `yes` 時，請小心無限輸出可能會佔用大量資源。
- 結合 `head` 或 `tail` 可以控制輸出的行數，避免過多輸出。
- 在需要自動確認的情況下，`yes` 可以與其他命令結合使用，提升效率。