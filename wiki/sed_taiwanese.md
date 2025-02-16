# [Linux] Bash sed 用法: 文本處理工具

## Overview
`sed` 是一個強大的流編輯器，用於處理和轉換文本數據。它可以在不打開編輯器的情況下，直接對文件或標準輸入進行文本替換、刪除和插入等操作。

## Usage
基本語法如下：
```bash
sed [options] [arguments]
```

## Common Options
- `-e`: 指定要執行的編輯命令。
- `-i`: 直接在文件中進行修改，而不是輸出到標準輸出。
- `-n`: 僅輸出符合條件的行。
- `s`: 替換命令，用於替換文本。

## Common Examples
1. **簡單文本替換**
   將文件中的 "apple" 替換為 "orange"：
   ```bash
   sed 's/apple/orange/' filename.txt
   ```

2. **直接修改文件**
   直接在文件中將 "cat" 替換為 "dog"：
   ```bash
   sed -i 's/cat/dog/g' filename.txt
   ```

3. **刪除行**
   刪除文件中第2行：
   ```bash
   sed '2d' filename.txt
   ```

4. **僅顯示匹配行**
   僅顯示包含 "error" 的行：
   ```bash
   sed -n '/error/p' filename.txt
   ```

5. **多個替換**
   同時將 "foo" 替換為 "bar" 和 "baz" 替換為 "qux"：
   ```bash
   sed -e 's/foo/bar/g' -e 's/baz/qux/g' filename.txt
   ```

## Tips
- 使用 `-i` 選項時，建議先備份原始文件，以防不小心刪除重要數據。
- 可以使用正則表達式來進行更複雜的匹配和替換。
- 結合管道（`|`）使用 `sed` 可以實現更強大的文本處理功能。