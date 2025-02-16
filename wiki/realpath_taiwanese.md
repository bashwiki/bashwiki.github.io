# [台灣] Bash realpath 使用方法: 獲取絕對路徑

## Overview
`realpath` 命令用於將相對路徑轉換為絕對路徑，並解析符號鏈接。這對於確保文件或目錄的正確路徑非常有用。

## Usage
基本語法如下：
```bash
realpath [options] [arguments]
```

## Common Options
- `-m`：允許返回不存在的路徑。
- `-q`：靜默模式，不顯示錯誤信息。
- `-s`：返回簡化的路徑，去除多餘的斜杠。

## Common Examples
1. 獲取當前目錄的絕對路徑：
   ```bash
   realpath .
   ```

2. 獲取特定文件的絕對路徑：
   ```bash
   realpath myfile.txt
   ```

3. 處理符號鏈接，獲取實際文件的路徑：
   ```bash
   realpath /path/to/symlink
   ```

4. 使用 `-m` 參數獲取不存在的路徑：
   ```bash
   realpath -m /nonexistent/path
   ```

## Tips
- 當你需要確保路徑的正確性時，使用 `realpath` 是一個好習慣。
- 結合其他命令使用，例如在腳本中自動獲取路徑，可以提高效率。
- 使用 `-q` 參數可以避免在處理不存在的路徑時顯示錯誤信息，讓輸出更乾淨。