# [台灣] Bash awk 使用法: 文本處理工具

## Overview
`awk` 是一個強大的文本處理工具，主要用於模式匹配和數據提取。它可以從文件或標準輸入中讀取數據，並根據指定的模式進行處理，特別適合用於表格數據的操作。

## Usage
基本語法如下：

```bash
awk [options] [arguments]
```

## Common Options
- `-F` : 指定字段分隔符，預設為空格。
- `-v` : 定義變數，方便在腳本中使用。
- `-f` : 從指定的文件中讀取 `awk` 腳本。
- `-e` : 直接在命令行中編寫 `awk` 程式碼。

## Common Examples
以下是一些常見的 `awk` 使用範例：

1. **打印特定列**：
   打印文件的第一列：
   ```bash
   awk '{print $1}' filename.txt
   ```

2. **使用自定義分隔符**：
   使用逗號作為分隔符，打印第二列：
   ```bash
   awk -F, '{print $2}' filename.csv
   ```

3. **條件篩選**：
   只打印大於 50 的數字：
   ```bash
   awk '$1 > 50' numbers.txt
   ```

4. **計算總和**：
   計算文件中第一列的總和：
   ```bash
   awk '{sum += $1} END {print sum}' numbers.txt
   ```

5. **格式化輸出**：
   格式化輸出每行的第一和第二列：
   ```bash
   awk '{printf "Name: %s, Age: %s\n", $1, $2}' data.txt
   ```

## Tips
- 使用 `-F` 選項來處理不同格式的文件，這樣可以更靈活地提取數據。
- 在處理大型文件時，考慮使用 `awk` 的內建變數如 `NR` 和 `NF` 來獲取行號和字段數量。
- 將常用的 `awk` 腳本保存到文件中，使用 `-f` 選項來執行，這樣可以提高效率和可讀性。