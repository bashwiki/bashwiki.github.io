# [Linux] Bash diff 用法: 比較檔案差異

## Overview
`diff` 命令用於比較兩個檔案的內容，並顯示它們之間的差異。這對於版本控制和檔案比對非常有用。

## Usage
基本語法如下：
```bash
diff [options] [file1] [file2]
```

## Common Options
- `-u`: 以統一格式顯示差異，通常更易於閱讀。
- `-c`: 以上下文格式顯示差異，提供更多上下文資訊。
- `-i`: 忽略大小寫的差異。
- `-w`: 忽略空白字符的差異。
- `-r`: 遞迴比較目錄中的檔案。

## Common Examples
1. 比較兩個檔案的差異：
   ```bash
   diff file1.txt file2.txt
   ```

2. 使用統一格式顯示差異：
   ```bash
   diff -u file1.txt file2.txt
   ```

3. 忽略大小寫的差異：
   ```bash
   diff -i file1.txt file2.txt
   ```

4. 遞迴比較兩個目錄：
   ```bash
   diff -r dir1/ dir2/
   ```

5. 使用上下文格式顯示差異：
   ```bash
   diff -c file1.txt file2.txt
   ```

## Tips
- 使用 `-u` 選項可以讓差異更易於理解，特別是在進行程式碼審查時。
- 當比較目錄時，`-r` 選項可以幫助你快速找到所有檔案的差異。
- 在處理大型檔案時，可以考慮將輸出重定向到檔案中，方便後續檢查：
  ```bash
  diff file1.txt file2.txt > differences.txt
  ```