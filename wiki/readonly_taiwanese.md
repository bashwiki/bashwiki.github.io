# [台灣] Bash readonly 用法: 設定變數為唯讀

## Overview
`readonly` 命令用於將變數設為唯讀，這意味著一旦變數被設定為唯讀，就無法再修改或刪除它的值。這在腳本中非常有用，可以防止意外的變數改變。

## Usage
基本語法如下：
```
readonly [options] [arguments]
```

## Common Options
- `-p`: 列出所有唯讀變數及其值。

## Common Examples
以下是一些常見的使用範例：

1. 設定變數為唯讀：
   ```bash
   MY_VAR="Hello, World!"
   readonly MY_VAR
   ```

2. 嘗試修改唯讀變數（將會失敗）：
   ```bash
   MY_VAR="New Value"  # 這將會報錯
   ```

3. 列出所有唯讀變數：
   ```bash
   readonly -p
   ```

4. 在腳本中使用唯讀變數：
   ```bash
   #!/bin/bash
   readonly CONFIG_PATH="/etc/myapp/config"
   echo "Config path is: $CONFIG_PATH"
   ```

## Tips
- 在腳本中使用 `readonly` 可以幫助維護變數的穩定性，避免意外修改。
- 使用 `readonly -p` 可以快速檢查當前的唯讀變數，方便調試。
- 將重要的設定變數設為唯讀，能提高腳本的安全性和可預測性。