# [Linux] Bash column 用法: 格式化文本為列

## Overview
`column` 命令用於將文本格式化為列，便於閱讀和顯示。它可以將輸入的數據排列成整齊的列，特別適合用於顯示表格數據。

## Usage
基本語法如下：
```bash
column [options] [arguments]
```

## Common Options
- `-t`: 以表格形式顯示，根據空格或制表符自動對齊列。
- `-s`: 指定分隔符，預設為空格。
- `-n`: 不顯示標題行。
- `-x`: 以行為主的方式顯示列，這樣可以更好地利用空間。

## Common Examples
以下是一些常見的用法範例：

1. **基本用法**：將文本文件格式化為列。
   ```bash
   column file.txt
   ```

2. **使用分隔符**：使用逗號作為分隔符格式化數據。
   ```bash
   column -s, -t file.csv
   ```

3. **以表格形式顯示**：將輸入數據以表格形式顯示。
   ```bash
   echo -e "Name\tAge\nAlice\t30\nBob\t25" | column -t
   ```

4. **行為主的顯示**：以行為主的方式顯示列。
   ```bash
   echo -e "A B C D\nE F G H" | column -x
   ```

## Tips
- 使用 `-t` 選項可以讓輸出更加整齊，特別是在處理多列數據時。
- 當處理帶有特殊字符的數據時，確保選擇正確的分隔符以避免格式錯誤。
- 可以將 `column` 與其他命令結合使用，例如 `cat` 或 `grep`，以便處理更複雜的數據流。