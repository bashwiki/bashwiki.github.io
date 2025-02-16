# [Linux] Bash readarray 使用法: 讀取檔案內容到陣列

## Overview
`readarray` 命令用於將檔案的每一行讀取到 Bash 陣列中。這使得處理檔案內容變得更加方便，因為可以直接以陣列的形式操作每一行。

## Usage
基本語法如下：

```bash
readarray [options] [array_name]
```

## Common Options
- `-t`: 移除每行結尾的換行符號。
- `-n <number>`: 只讀取指定數量的行。
- `-s <number>`: 跳過指定數量的行。

## Common Examples

### 例子 1: 讀取檔案到陣列
將檔案 `file.txt` 的內容讀取到陣列 `lines` 中：

```bash
readarray lines < file.txt
```

### 例子 2: 移除換行符號
將檔案內容讀取到陣列中，並移除每行結尾的換行符號：

```bash
readarray -t lines < file.txt
```

### 例子 3: 只讀取前 5 行
只從檔案中讀取前 5 行到陣列中：

```bash
readarray -n 5 lines < file.txt
```

### 例子 4: 跳過前 2 行
從檔案中跳過前 2 行，然後將其餘行讀取到陣列中：

```bash
readarray -s 2 lines < file.txt
```

## Tips
- 使用 `-t` 選項可以避免在處理陣列時出現意外的換行符號。
- 在讀取大型檔案時，考慮使用 `-n` 和 `-s` 選項來控制讀取的行數，這樣可以提高效率。
- 確保檔案存在且可讀，否則 `readarray` 會報錯。