# [Linux] Bash jq 用法: JSON 資料處理工具

## Overview
`jq` 是一個輕量級的命令行工具，用於解析、過濾和轉換 JSON 格式的資料。它能夠讓使用者輕鬆地從 JSON 資料中提取所需的資訊，並進行格式化輸出。

## Usage
基本語法如下：
```bash
jq [options] [arguments]
```

## Common Options
- `-c`: 輸出為壓縮格式，將每個 JSON 對象放在一行。
- `-r`: 以原始格式輸出，不加引號。
- `-f <file>`: 從指定的文件中讀取 jq 表達式。
- `--arg <name> <value>`: 定義一個變數，並在 jq 表達式中使用。

## Common Examples
以下是一些常見的使用範例：

1. **提取 JSON 中的特定欄位**
   ```bash
   echo '{"name": "Alice", "age": 30}' | jq '.name'
   ```
   輸出：
   ```
   "Alice"
   ```

2. **過濾 JSON 陣列中的對象**
   ```bash
   echo '[{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]' | jq '.[] | select(.name == "Bob")'
   ```
   輸出：
   ```
   {
     "name": "Bob"
   }
   ```

3. **修改 JSON 中的值**
   ```bash
   echo '{"name": "Alice", "age": 30}' | jq '.age = 31'
   ```
   輸出：
   ```
   {
     "name": "Alice",
     "age": 31
   }
   ```

4. **將 JSON 輸出為壓縮格式**
   ```bash
   echo '[{"name": "Alice"}, {"name": "Bob"}]' | jq -c '.'
   ```
   輸出：
   ```
   {"name":"Alice"}{"name":"Bob"}
   ```

## Tips
- 使用 `-r` 選項可以獲得更乾淨的輸出，特別是在需要將結果傳遞給其他命令時。
- 結合 `--arg` 選項來動態傳遞變數，可以讓你的 jq 表達式更加靈活。
- 熟悉 jq 的過濾器和運算符，能夠幫助你更有效率地處理 JSON 資料。