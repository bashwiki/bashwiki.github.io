# [Linux] Bash unset 用法: 刪除變數或函數

## Overview
`unset` 命令用於刪除指定的變數或函數。這個命令可以幫助你清理不再需要的變數，釋放資源，或是避免命名衝突。

## Usage
基本語法如下：
```
unset [選項] [參數]
```

## Common Options
- `-v`：刪除變數。
- `-f`：刪除函數。

## Common Examples
以下是一些常見的使用範例：

1. 刪除變數：
   ```bash
   my_var="Hello, World!"
   echo $my_var  # 輸出: Hello, World!
   unset my_var
   echo $my_var  # 輸出: (無輸出)
   ```

2. 刪除函數：
   ```bash
   my_function() {
       echo "This is a function."
   }
   my_function  # 輸出: This is a function.
   unset -f my_function
   my_function  # 輸出: bash: my_function: command not found
   ```

3. 同時刪除多個變數：
   ```bash
   var1="First"
   var2="Second"
   unset var1 var2
   echo $var1  # 輸出: (無輸出)
   echo $var2  # 輸出: (無輸出)
   ```

## Tips
- 在使用 `unset` 時，確保你不會刪除系統或環境變數，這可能會影響到你的 shell 環境。
- 使用 `unset` 刪除變數後，該變數將無法再被使用，請在確定不需要時再執行此命令。
- 你可以使用 `declare -p` 來檢查變數是否存在，這樣可以幫助你避免不必要的錯誤。