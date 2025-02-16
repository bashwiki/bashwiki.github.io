# [Linux] Bash head 使用方法：顯示檔案的前幾行

## Overview
`head` 命令用於顯示檔案的前幾行。這在查看大型檔案的開頭部分時特別有用，讓使用者能快速獲取檔案的內容概覽。

## Usage
基本語法如下：
```bash
head [options] [arguments]
```

## Common Options
- `-n <number>`：指定要顯示的行數，預設為10行。
- `-c <number>`：指定要顯示的字元數。
- `-q`：不顯示檔案名稱，適用於多個檔案時。
- `-v`：顯示檔案名稱，即使只有一個檔案。

## Common Examples
1. 顯示檔案的前10行（預設行數）：
   ```bash
   head filename.txt
   ```

2. 顯示檔案的前5行：
   ```bash
   head -n 5 filename.txt
   ```

3. 顯示檔案的前100個字元：
   ```bash
   head -c 100 filename.txt
   ```

4. 顯示多個檔案的前10行，並顯示檔案名稱：
   ```bash
   head -v file1.txt file2.txt
   ```

5. 顯示檔案的前20行，不顯示檔案名稱：
   ```bash
   head -q -n 20 file1.txt file2.txt
   ```

## Tips
- 使用 `-n` 選項時，可以使用 `-n -<number>` 來顯示從檔案末尾向上計算的行數。
- 結合 `tail` 命令，可以更靈活地查看檔案的特定部分。
- 在處理大型檔案時，`head` 是快速檢查檔案內容的好幫手。