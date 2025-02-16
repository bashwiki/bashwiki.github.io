# [Linux] Bash export 使用法: 設定環境變數

## Overview
`export` 命令用於設定環境變數，讓這些變數可以在子進程中使用。這對於配置系統環境或傳遞參數給執行的程式非常有用。

## Usage
基本語法如下：
```
export [options] [arguments]
```

## Common Options
- `-p`：顯示所有已導出的環境變數。
- `-n`：取消導出指定的變數。
- `-f`：導出函數，而不僅僅是變數。

## Common Examples
1. 導出一個變數：
   ```bash
   MY_VAR="Hello, World!"
   export MY_VAR
   ```

2. 在導出時直接設定變數：
   ```bash
   export MY_VAR="Hello, World!"
   ```

3. 顯示所有導出的變數：
   ```bash
   export -p
   ```

4. 取消導出一個變數：
   ```bash
   export -n MY_VAR
   ```

5. 導出一個函數：
   ```bash
   my_function() {
       echo "This is a function."
   }
   export -f my_function
   ```

## Tips
- 確保在導出變數之前先進行賦值，否則將導出一個空變數。
- 使用 `export -p` 可以快速檢查當前的環境變數設定。
- 對於需要在多個子進程中使用的變數，記得使用 `export` 來確保它們可用。