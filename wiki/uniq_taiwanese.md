# [Linux] Bash uniq 用法: 刪除重複行

## Overview
`uniq` 命令用於從已排序的文本中刪除重複的行。它通常與 `sort` 命令一起使用，以確保輸入的行是有序的，這樣才能正確地刪除重複項。

## Usage
基本語法如下：
```
uniq [選項] [檔案]
```

## Common Options
- `-c`：計算每一行出現的次數。
- `-d`：只顯示重複的行。
- `-u`：只顯示唯一的行。
- `-i`：忽略大小寫的差異。

## Common Examples
1. 刪除重複行並顯示結果：
   ```bash
   sort input.txt | uniq
   ```

2. 計算每一行出現的次數：
   ```bash
   sort input.txt | uniq -c
   ```

3. 只顯示重複的行：
   ```bash
   sort input.txt | uniq -d
   ```

4. 只顯示唯一的行：
   ```bash
   sort input.txt | uniq -u
   ```

5. 忽略大小寫的重複行：
   ```bash
   sort input.txt | uniq -i
   ```

## Tips
- 確保在使用 `uniq` 之前先對檔案進行排序，這樣才能正確刪除重複行。
- 可以將 `uniq` 與其他命令結合使用，例如 `grep`，以進行更複雜的文本處理。
- 使用 `-c` 選項時，可以快速了解哪些行出現的次數最多，這對於數據分析非常有用。