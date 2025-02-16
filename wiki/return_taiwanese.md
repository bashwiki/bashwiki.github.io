# [Linux] Bash return 使用法: 返回上一個命令的退出狀態

## Overview
`return` 命令用於在函數中返回退出狀態碼。這個狀態碼可以用來指示函數的執行結果，通常是成功或失敗的標誌。

## Usage
基本語法如下：
```bash
return [n]
```
其中 `n` 是要返回的退出狀態碼，預設為上一個命令的狀態碼。

## Common Options
- `n`：指定要返回的退出狀態碼，範圍通常是 0 到 255。0 通常表示成功，非 0 值表示錯誤或異常。

## Common Examples
以下是一些常見的使用範例：

### 返回成功狀態
```bash
function my_function {
    echo "執行成功"
    return 0
}
my_function
```

### 返回失敗狀態
```bash
function my_function {
    echo "執行失敗"
    return 1
}
my_function
```

### 使用返回值進行判斷
```bash
function my_function {
    return 2
}

my_function
if [ $? -eq 2 ]; then
    echo "函數返回了狀態碼 2"
fi
```

## Tips
- 在函數中使用 `return` 時，確保你明確知道要返回的狀態碼，這樣可以幫助調試和錯誤處理。
- 使用 `$?` 變數來檢查上一個命令或函數的退出狀態碼，這對於流程控制非常有用。
- 盡量使用 0 表示成功，其他數字表示不同的錯誤類型，以便於後續的錯誤處理。