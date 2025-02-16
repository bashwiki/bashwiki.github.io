# [Linux] Bash mapfile 使用方式: 將檔案內容讀入陣列

## Overview
`mapfile` 是一個 Bash 命令，用於將檔案的每一行讀取並存入一個陣列中。這個命令特別適合需要處理大量資料的情況，因為它可以快速將檔案內容轉換為易於操作的陣列格式。

## Usage
基本語法如下：
```bash
mapfile [options] [array_name]
```

## Common Options
- `-n` : 指定要讀取的行數。
- `-s` : 跳過指定的行數。
- `-t` : 去除每行結尾的換行符號。

## Common Examples

### 例子 1: 將檔案內容讀入陣列
```bash
mapfile lines < filename.txt
```
這會將 `filename.txt` 的每一行讀入名為 `lines` 的陣列中。

### 例子 2: 讀取部分行
```bash
mapfile -n 5 lines < filename.txt
```
這會將 `filename.txt` 的前五行讀入 `lines` 陣列中。

### 例子 3: 跳過前幾行
```bash
mapfile -s 2 lines < filename.txt
```
這會跳過 `filename.txt` 的前兩行，然後將剩下的行讀入 `lines` 陣列中。

### 例子 4: 去除行尾換行符
```bash
mapfile -t lines < filename.txt
```
這會將 `filename.txt` 的每一行讀入 `lines` 陣列中，同時去除每行的換行符號。

## Tips
- 使用 `-t` 選項可以讓你在處理陣列時避免不必要的換行符，這對於後續的字串處理非常有幫助。
- 如果你只需要檔案的某幾行，考慮使用 `-n` 和 `-s` 選項來提高效率。
- `mapfile` 對於處理大型檔案特別有效，因為它能夠一次性讀取整個檔案並存入陣列，避免了逐行讀取的性能損耗。