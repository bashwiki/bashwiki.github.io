# [Linux] Bash printf 使用法: 格式化輸出文本

## Overview
`printf` 命令用於格式化輸出文本，類似於 C 語言中的 `printf` 函數。它允許用戶以指定的格式輸出字符串、數字等，提供更靈活的輸出選項。

## Usage
基本語法如下：
```bash
printf [options] [arguments]
```

## Common Options
- `-v var`: 將輸出存儲到變量 `var` 中，而不是顯示在終端。
- `--help`: 顯示幫助信息。
- `--version`: 顯示版本信息。

## Common Examples
1. **基本字符串輸出**
   ```bash
   printf "Hello, World!\n"
   ```
   這將輸出：`Hello, World!`

2. **格式化數字**
   ```bash
   printf "Number: %d\n" 42
   ```
   這將輸出：`Number: 42`

3. **浮點數格式化**
   ```bash
   printf "Pi: %.2f\n" 3.14159
   ```
   這將輸出：`Pi: 3.14`

4. **多個參數**
   ```bash
   printf "Name: %s, Age: %d\n" "Alice" 30
   ```
   這將輸出：`Name: Alice, Age: 30`

5. **將輸出存儲到變量**
   ```bash
   printf -v myVar "Hello, %s!" "User"
   echo "$myVar"
   ```
   這將輸出：`Hello, User!`

## Tips
- 使用 `\n` 來換行，確保輸出格式整齊。
- 可以使用 `%s`、`%d`、`%f` 等格式符來格式化不同類型的數據。
- 在處理大量數據時，考慮使用 `printf` 來提高輸出效率和可讀性。