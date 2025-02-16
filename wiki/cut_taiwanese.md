# [Linux] Bash cut 使用法: 切割文本行

## Overview
`cut` 命令用於從文本行中提取特定的部分，通常用於處理以分隔符分隔的數據，如 CSV 文件或其他格式的文本數據。

## Usage
基本語法如下：
```
cut [options] [arguments]
```

## Common Options
- `-f`：指定要提取的字段（以分隔符分隔）。
- `-d`：指定字段的分隔符，預設為制表符。
- `-c`：按字符位置提取。
- `--complement`：提取不符合指定字段或字符的部分。

## Common Examples
1. 提取以逗號分隔的第二個字段：
   ```bash
   cut -d ',' -f 2 filename.txt
   ```

2. 提取特定字符範圍：
   ```bash
   cut -c 1-5 filename.txt
   ```

3. 提取多個字段（例如第一和第三個字段）：
   ```bash
   cut -d ',' -f 1,3 filename.txt
   ```

4. 提取不符合指定字段的部分：
   ```bash
   cut -d ',' -f 2 --complement filename.txt
   ```

## Tips
- 確保選擇正確的分隔符，這對於正確提取字段至關重要。
- 使用 `-n` 選項可以避免在提取時顯示空行。
- 結合管道使用 `cut` 可以有效地處理來自其他命令的輸出。