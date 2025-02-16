# [Linux] Bash source 使用法: 載入腳本

## Overview
`source` 命令用來在當前的 shell 環境中執行指定的腳本文件。這意味著腳本中的變數和函數會在當前的 shell 中可用，而不是在子 shell 中執行。

## Usage
基本語法如下：
```
source [選項] [參數]
```

## Common Options
- `-h`, `--help`: 顯示幫助信息。
- `-V`, `--version`: 顯示版本信息。

## Common Examples

1. **載入環境變數**
   ```bash
   source ~/.bashrc
   ```
   這個命令會載入用戶的 `.bashrc` 文件，更新當前 shell 的環境變數。

2. **執行自定義腳本**
   ```bash
   source my_script.sh
   ```
   這會在當前 shell 中執行 `my_script.sh` 腳本，並使其中的變數和函數立即可用。

3. **載入多個腳本**
   ```bash
   source script1.sh && source script2.sh
   ```
   這個命令將依次載入 `script1.sh` 和 `script2.sh`，確保兩個腳本都在同一個 shell 環境中執行。

## Tips
- 使用 `source` 而不是直接執行腳本可以避免創建新的子 shell，這對於需要修改當前 shell 環境的情況非常有用。
- 確保腳本具有執行權限，否則可能會遇到權限問題。
- 使用 `source` 來快速測試腳本中的變數和函數，這樣可以即時看到變更的效果。