# [Linux] Bash pwd 用法: 顯示當前工作目錄

## Overview
`pwd`（print working directory）是一個用於顯示當前工作目錄的命令。當你在終端中執行此命令時，它會顯示你目前所在的路徑。

## Usage
基本語法如下：
```
pwd [options]
```

## Common Options
- `-L`：顯示邏輯路徑，這是預設選項。
- `-P`：顯示物理路徑，會解析符號連結。

## Common Examples
1. 顯示當前工作目錄：
   ```bash
   pwd
   ```

2. 顯示物理路徑：
   ```bash
   pwd -P
   ```

3. 顯示邏輯路徑：
   ```bash
   pwd -L
   ```

## Tips
- 使用 `pwd` 命令可以幫助你確認當前的工作目錄，特別是在進行檔案操作時。
- 結合其他命令使用，例如在使用 `cd` 命令後，可以立即使用 `pwd` 確認你已經切換到正確的目錄。