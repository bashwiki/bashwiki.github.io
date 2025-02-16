# [Linux] Bash local 使用法: 定義區域變數

## Overview
`local` 命令用於在 Bash 腳本中定義區域變數。這些變數的作用範圍僅限於其所在的函數內部，當函數執行結束後，這些變數將不再可用。

## Usage
基本語法如下：
```bash
local [options] [variable_name=value]
```

## Common Options
- `-n`: 使變數成為只讀，無法被修改。
- `-p`: 列出當前所有區域變數及其值。

## Common Examples
以下是一些常見的使用範例：

### 定義區域變數
```bash
function my_function {
    local my_var="Hello, World!"
    echo $my_var
}
my_function  # 輸出: Hello, World!
echo $my_var # 不會輸出任何東西，因為 my_var 是區域變數
```

### 使用 `-n` 選項
```bash
function my_function {
    local -n ref_var=my_var
    my_var="Hello, World!"
}
my_function
echo $my_var # 輸出: Hello, World!
```

### 列出區域變數
```bash
function my_function {
    local var1="Value1"
    local var2="Value2"
    local -p # 列出所有區域變數
}
my_function
```

## Tips
- 使用 `local` 可以避免全域變數的衝突，特別是在大型腳本中。
- 在函數內部使用 `local` 定義變數時，請確保變數名稱不會與全域變數重複，以減少混淆。
- 使用 `-p` 選項可以幫助你調試，了解當前函數內部的變數狀態。