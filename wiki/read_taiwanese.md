# [Linux] Bash read 使用法: 讀取使用者輸入

## Overview
`read` 命令用於從標準輸入讀取一行資料，並將其儲存到變數中。這在腳本中非常有用，可以讓使用者輸入資料以便後續處理。

## Usage
基本語法如下：
```bash
read [options] [arguments]
```

## Common Options
- `-p`: 提供提示訊息，讓使用者知道要輸入什麼。
- `-s`: 隱藏輸入，通常用於密碼輸入。
- `-a`: 將輸入的內容儲存為陣列。
- `-d`: 指定結束字元，讀取到該字元為止。

## Common Examples
1. **基本使用**
   ```bash
   read name
   echo "Hello, $name!"
   ```

2. **使用提示訊息**
   ```bash
   read -p "請輸入您的名字: " name
   echo "你好, $name!"
   ```

3. **隱藏輸入（例如密碼）**
   ```bash
   read -s -p "請輸入密碼: " password
   echo "密碼已儲存。"
   ```

4. **將輸入儲存為陣列**
   ```bash
   read -a fruits
   echo "你輸入的水果有: ${fruits[@]}"
   ```

5. **使用自訂結束字元**
   ```bash
   echo "請輸入資料，輸入#結束:"
   read -d '#' input
   echo "你輸入的資料是: $input"
   ```

## Tips
- 當使用 `-s` 隱藏輸入時，建議在輸入完成後提供反饋，以免使用者不確定是否輸入成功。
- 使用 `-p` 提供清晰的提示訊息，可以提高使用者體驗。
- 當處理多個變數時，考慮使用 `-a` 來簡化代碼。