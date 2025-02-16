# [Linux] Bash basename 用法: 取得檔案名稱

## Overview
`basename` 命令用於從完整的檔案路徑中提取檔案名稱。這對於處理檔案時特別有用，因為它可以幫助你獲得不帶路徑的純檔案名稱。

## Usage
基本語法如下：
```bash
basename [options] [arguments]
```

## Common Options
- `-a`：處理多個檔案，並返回每個檔案的名稱。
- `-s`：指定要去除的後綴，這樣可以只保留檔案名稱的主要部分。

## Common Examples
以下是一些常見的使用範例：

1. 取得單一檔案名稱：
   ```bash
   basename /home/user/documents/file.txt
   ```
   輸出：
   ```
   file.txt
   ```

2. 取得多個檔案名稱：
   ```bash
   basename -a /home/user/documents/file1.txt /home/user/documents/file2.txt
   ```
   輸出：
   ```
   file1.txt
   file2.txt
   ```

3. 去除檔案後綴：
   ```bash
   basename /home/user/documents/file.txt .txt
   ```
   輸出：
   ```
   file
   ```

4. 使用變數來取得檔案名稱：
   ```bash
   FILE_PATH="/home/user/documents/file.txt"
   basename "$FILE_PATH"
   ```
   輸出：
   ```
   file.txt
   ```

## Tips
- 當你需要處理多個檔案時，使用 `-a` 選項可以一次性獲得所有檔案名稱。
- 使用 `-s` 選項可以方便地去除特定的檔案後綴，這對於批量處理檔案特別有用。
- 結合其他命令（如 `find`）使用 `basename` 可以提高工作效率，例如在處理搜尋結果時。