# [台灣] Bash typeset 用法: 設定變數屬性

## Overview
`typeset` 命令用於在 Bash 中設定變數的屬性，這些屬性可以控制變數的行為，例如是否為只讀、是否為數字等。

## Usage
基本語法如下：
```bash
typeset [options] [arguments]
```

## Common Options
- `-r`：將變數設為只讀，無法被修改。
- `-i`：將變數設為整數，所有賦值會自動轉換為整數。
- `-a`：將變數設為陣列。
- `-A`：將變數設為關聯陣列。
- `-x`：將變數導出到環境變數中。

## Common Examples
以下是一些常見的 `typeset` 使用範例：

### 設定只讀變數
```bash
typeset -r MY_VAR="Hello"
echo $MY_VAR  # 輸出: Hello
MY_VAR="World"  # 將會報錯，因為 MY_VAR 是只讀的
```

### 設定整數變數
```bash
typeset -i COUNT=5
COUNT=10
echo $COUNT  # 輸出: 10
COUNT="20"  # 也可以直接賦值字串，會自動轉換為整數
```

### 設定陣列變數
```bash
typeset -a MY_ARRAY
MY_ARRAY[0]="Apple"
MY_ARRAY[1]="Banana"
echo ${MY_ARRAY[0]}  # 輸出: Apple
```

### 設定關聯陣列變數
```bash
typeset -A MY_ASSOC_ARRAY
MY_ASSOC_ARRAY["key1"]="value1"
MY_ASSOC_ARRAY["key2"]="value2"
echo ${MY_ASSOC_ARRAY["key1"]}  # 輸出: value1
```

## Tips
- 使用 `typeset` 設定變數屬性可以幫助避免意外的變數修改，特別是在大型腳本中。
- 當你需要處理數字運算時，記得使用 `-i` 選項，這樣可以避免字串轉換帶來的錯誤。
- 對於需要在子進程中使用的變數，使用 `-x` 將其導出為環境變數。