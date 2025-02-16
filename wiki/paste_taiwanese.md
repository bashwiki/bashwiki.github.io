# [Linux] Bash paste 使用法: 合併檔案內容

## Overview
`paste` 命令用於將多個檔案的內容進行水平合併，並將結果輸出到標準輸出或指定的檔案中。這個命令特別適合用於處理多行資料，將它們並排顯示。

## Usage
基本語法如下：
```
paste [options] [arguments]
```

## Common Options
- `-d`：指定分隔符，預設為制表符。
- `-s`：將每個檔案的內容串接在一起，而不是並排顯示。
- `-z`：將輸入視為零結尾的，而不是行結尾的。

## Common Examples
1. 合併兩個檔案的內容：
   ```bash
   paste file1.txt file2.txt
   ```

2. 使用自定義分隔符（例如逗號）：
   ```bash
   paste -d ',' file1.txt file2.txt
   ```

3. 串接檔案內容而不是並排顯示：
   ```bash
   paste -s file1.txt file2.txt
   ```

4. 合併多個檔案並將結果輸出到新檔案：
   ```bash
   paste file1.txt file2.txt > output.txt
   ```

5. 使用零結尾的輸入：
   ```bash
   paste -z file1.txt file2.txt
   ```

## Tips
- 使用 `-d` 選項可以自定義輸出格式，讓結果更符合需求。
- 當處理大量檔案時，考慮使用 `-s` 來簡化輸出。
- 確保檔案的行數相同，以避免輸出不一致的情況。