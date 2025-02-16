# [Linux] Bash rev 反轉字串: 反轉每一行的字元順序

## Overview
`rev` 是一個用於反轉每一行字元順序的命令。當你需要將文本中的每一行字元反轉時，這個命令非常有用。

## Usage
基本語法如下：
```
rev [options] [arguments]
```

## Common Options
- `-` : 從標準輸入讀取資料。
- `-o <file>` : 將輸出的反轉結果寫入指定的檔案。

## Common Examples
以下是一些常見的使用範例：

1. 反轉檔案中的每一行：
   ```bash
   rev filename.txt
   ```

2. 從標準輸入反轉字串：
   ```bash
   echo "Hello World" | rev
   ```

3. 將反轉結果寫入新檔案：
   ```bash
   rev filename.txt -o reversed.txt
   ```

4. 反轉多行文字：
   ```bash
   cat << EOF | rev
   Line one
   Line two
   Line three
   EOF
   ```

## Tips
- 當你需要快速反轉字串時，可以使用管道將輸入傳遞給 `rev`。
- 確保檔案存在，否則 `rev` 將無法執行。
- 使用 `-o` 選項可以方便地將結果保存到檔案中，避免在終端機中查看長輸出。