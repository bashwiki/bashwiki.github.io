# [台灣] Bash tail 使用方式: 顯示檔案的尾端內容

## Overview
`tail` 命令用來顯示檔案的最後幾行內容，通常用於查看日誌檔案或其他不斷增長的檔案的最新資訊。

## Usage
基本語法如下：
```
tail [選項] [檔案]
```

## Common Options
- `-n [數字]`：顯示檔案的最後幾行，數字可以指定行數。
- `-f`：持續追蹤檔案的新增內容，適合用於即時監控日誌。
- `-c [數字]`：顯示檔案的最後幾個字元。

## Common Examples
1. 顯示檔案的最後10行（預設行數）：
   ```bash
   tail filename.txt
   ```

2. 顯示檔案的最後20行：
   ```bash
   tail -n 20 filename.txt
   ```

3. 持續追蹤日誌檔案的新增內容：
   ```bash
   tail -f logfile.log
   ```

4. 顯示檔案的最後100個字元：
   ```bash
   tail -c 100 filename.txt
   ```

## Tips
- 使用 `tail -f` 來監控日誌檔案時，可以按 `Ctrl+C` 停止追蹤。
- 結合 `grep` 使用 `tail`，可以過濾出特定關鍵字的最新日誌行：
  ```bash
  tail -f logfile.log | grep "ERROR"
  ```
- 若需要查看檔案的開頭內容，可以使用 `head` 命令。