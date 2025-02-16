# [Linux] Bash compgen 用法: 自動補全選項

## Overview
`compgen` 是一個 Bash 命令，用於生成可用的補全選項。這個命令通常與自動補全功能一起使用，幫助用戶快速找到可用的命令或文件名。

## Usage
基本語法如下：
```
compgen [options] [arguments]
```

## Common Options
- `-c`: 列出所有可用的命令。
- `-a`: 列出所有的別名。
- `-b`: 列出所有的內建命令。
- `-k`: 列出所有的關鍵字。
- `-A`: 根據指定的類型列出選項，例如 `file` 或 `command`。

## Common Examples
以下是一些常見的使用範例：

1. 列出所有可用的命令：
   ```bash
   compgen -c
   ```

2. 列出所有的別名：
   ```bash
   compgen -a
   ```

3. 列出所有的內建命令：
   ```bash
   compgen -b
   ```

4. 列出所有的關鍵字：
   ```bash
   compgen -k
   ```

5. 根據文件類型列出可用的文件名：
   ```bash
   compgen -A file
   ```

## Tips
- 使用 `compgen` 時，可以將結果與 `grep` 結合，以過濾特定的選項，例如：
  ```bash
  compgen -c | grep ssh
  ```
- 在撰寫腳本時，利用 `compgen` 可以幫助用戶更快地找到可用的命令或選項，提升效率。
- 結合 `readline` 或其他自動補全功能，可以讓命令行操作更加流暢。