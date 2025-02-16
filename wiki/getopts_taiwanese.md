# [Linux] Bash getopts 使用法: 解析命令行選項

## Overview
`getopts` 是一個用於解析命令行選項的 Bash 內建命令。它使得腳本能夠輕鬆地處理選項和參數，並且能夠支持短選項和長選項的解析。

## Usage
基本語法如下：
```bash
getopts optstring variable
```
- `optstring` 是一個字串，定義了可接受的選項。
- `variable` 是用來存儲當前選項的變數名稱。

## Common Options
- `-a`: 這是一個示範選項，通常用於指定某個行為。
- `-b`: 另一個示範選項，可能用於開啟或關閉某個功能。
- `-c`: 用於指定某個參數的選項。

## Common Examples
以下是一些實用的範例：

### 基本範例
```bash
#!/bin/bash
while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "選項 -a 被選擇"
      ;;
    b)
      echo "選項 -b 被選擇，參數為 '$OPTARG'"
      ;;
    c)
      echo "選項 -c 被選擇，參數為 '$OPTARG'"
      ;;
    *)
      echo "無效的選項"
      ;;
  esac
done
```

### 使用範例
假設你將上述腳本命名為 `script.sh`，可以這樣執行：
```bash
bash script.sh -a -b value1 -c value2
```
輸出將會是：
```
選項 -a 被選擇
選項 -b 被選擇，參數為 'value1'
選項 -c 被選擇，參數為 'value2'
```

### 處理無效選項
```bash
#!/bin/bash
while getopts "a:b:" opt; do
  case $opt in
    a)
      echo "選項 -a 被選擇"
      ;;
    b)
      echo "選項 -b 被選擇，參數為 '$OPTARG'"
      ;;
    *)
      echo "無效的選項"
      exit 1
      ;;
  esac
done
```

## Tips
- 確保在 `optstring` 中正確地定義選項，特別是需要參數的選項後面要加上冒號 `:`。
- 使用 `OPTARG` 變數來獲取當前選項的參數值。
- 在處理選項時，記得使用 `case` 語句來提高可讀性和維護性。