# [Linux] Bash eval 使用法: 執行字串為命令

## Overview
`eval` 命令用於將字串解析為命令並執行。這對於動態生成命令或在腳本中處理變數特別有用。

## Usage
基本語法如下：
```bash
eval [options] [arguments]
```

## Common Options
`eval` 命令本身沒有特定的選項，主要是用來處理輸入的字串。它的功能主要依賴於傳遞的參數。

## Common Examples

### 例子 1: 簡單的命令執行
```bash
command="ls -l"
eval $command
```
這將執行 `ls -l` 命令，顯示當前目錄的詳細列表。

### 例子 2: 使用變數
```bash
filename="myfile.txt"
eval "echo The file is $filename"
```
這將輸出 `The file is myfile.txt`。

### 例子 3: 動態生成命令
```bash
cmd="mkdir new_folder"
eval $cmd
```
這會創建一個名為 `new_folder` 的新目錄。

### 例子 4: 結合變數和命令
```bash
var="Hello"
eval "echo \$var World"
```
這將輸出 `Hello World`。注意在字串中使用 `\$` 來避免變數提前解析。

## Tips
- 使用 `eval` 時要小心，因為它會執行任何傳遞的命令，這可能導致安全問題。
- 確保傳遞給 `eval` 的字串是可信的，避免執行潛在的惡意命令。
- 在需要動態生成命令的情況下使用 `eval`，但在其他情況下，考慮使用更安全的替代方案。