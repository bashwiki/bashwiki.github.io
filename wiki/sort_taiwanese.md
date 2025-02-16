# [Linux] Bash sort 使用法: 排序檔案內容

## Overview
`sort` 命令用於對文本檔案中的行進行排序。它可以根據字母順序、數字順序或其他自定義排序方式來排列資料，並且非常適合處理大型檔案。

## Usage
基本語法如下：
```
sort [options] [arguments]
```

## Common Options
- `-n`：按數字順序排序。
- `-r`：反向排序，從大到小。
- `-k`：指定排序的鍵（欄位）。
- `-u`：刪除重複的行。
- `-o`：將排序結果輸出到指定檔案。

## Common Examples
以下是一些常見的使用範例：

1. **對檔案內容進行字母排序**：
   ```bash
   sort filename.txt
   ```

2. **按數字順序排序**：
   ```bash
   sort -n numbers.txt
   ```

3. **反向排序**：
   ```bash
   sort -r filename.txt
   ```

4. **指定排序鍵**：
   ```bash
   sort -k 2 filename.txt
   ```

5. **刪除重複行並排序**：
   ```bash
   sort -u filename.txt
   ```

6. **將排序結果輸出到新檔案**：
   ```bash
   sort -o sorted.txt filename.txt
   ```

## Tips
- 在處理大型檔案時，可以考慮使用 `-S` 選項來指定可用的記憶體大小，以提高排序效率。
- 使用 `-t` 選項來指定分隔符，這對於以特定字符分隔的檔案特別有用。
- 結合 `uniq` 命令可以進一步處理排序後的結果，特別是當需要去除重複行時。