# [Linux] Bash exit 使用法: 結束執行的指令

## Overview
`exit` 指令用於結束當前的 shell 或腳本執行，並可以返回一個狀態碼給呼叫者。這個狀態碼通常用來表示執行的結果，成功或失敗。

## Usage
基本語法如下：
```bash
exit [options] [n]
```
其中 `n` 是可選的，代表退出狀態碼，預設為 0。

## Common Options
- `n`: 指定退出狀態碼，通常使用 0 表示成功，非 0 表示錯誤。
- `-`: 如果不指定狀態碼，則返回上一次執行的命令的狀態碼。

## Common Examples
1. 結束當前 shell，返回成功狀態：
   ```bash
   exit 0
   ```

2. 結束腳本執行，返回錯誤狀態：
   ```bash
   exit 1
   ```

3. 在一個腳本中使用 exit，根據條件返回不同的狀態碼：
   ```bash
   if [ -f "file.txt" ]; then
       echo "File exists."
       exit 0
   else
       echo "File does not exist."
       exit 1
   fi
   ```

4. 使用 `exit` 結束一個交互式 shell：
   ```bash
   exit
   ```

## Tips
- 在腳本中，使用 `exit` 可以幫助其他程序或使用者了解腳本的執行結果。
- 確保在腳本的結尾使用 `exit`，以明確結束腳本的執行。
- 使用適當的狀態碼可以提高腳本的可讀性和可維護性。