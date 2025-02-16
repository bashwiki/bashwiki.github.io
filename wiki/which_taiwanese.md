# [Linux] Bash which 使用法: 查找可執行檔路徑

## Overview
`which` 命令用於查找並顯示指定命令的可執行檔路徑。這對於確認系統中某個命令的安裝位置非常有用。

## Usage
基本語法如下：
```
which [options] [arguments]
```

## Common Options
- `-a`：顯示所有匹配的可執行檔路徑，而不僅僅是第一個找到的。
- `-p`：在查找時不使用 PATH 環境變數，僅查找預設路徑。

## Common Examples
以下是一些實用的範例：

1. 查找 `python` 的可執行檔路徑：
   ```bash
   which python
   ```

2. 查找 `git` 的可執行檔路徑，顯示所有匹配的路徑：
   ```bash
   which -a git
   ```

3. 查找 `node` 的可執行檔路徑，並使用預設路徑：
   ```bash
   which -p node
   ```

## Tips
- 使用 `which` 可以幫助你確認某個命令是否安裝在系統上。
- 如果你發現某個命令的路徑不在預期的位置，考慮檢查你的 PATH 環境變數設定。
- 結合其他命令使用，例如 `alias`，可以幫助你更好地管理命令的使用。