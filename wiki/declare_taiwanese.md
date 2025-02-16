# [Linux] Bash declare 用法: 宣告變數及其屬性

## Overview
`declare` 命令用於在 Bash 中宣告變數及其屬性。這個命令可以幫助使用者設定變數的類型、範圍以及其他屬性，從而提高腳本的可讀性和可維護性。

## Usage
基本語法如下：
```
declare [options] [arguments]
```

## Common Options
- `-a`：宣告一個陣列變數。
- `-i`：宣告一個整數變數，所有賦值都會自動轉換為整數。
- `-r`：宣告一個唯讀變數，無法被修改。
- `-x`：宣告一個環境變數，會被導出到子進程中。

## Common Examples

### 宣告一個整數變數
```bash
declare -i num=10
num=5
echo $num  # 輸出 5
```

### 宣告一個唯讀變數
```bash
declare -r constant=100
echo $constant  # 輸出 100
# constant=200  # 這行會報錯，因為 constant 是唯讀的
```

### 宣告一個陣列變數
```bash
declare -a fruits=("apple" "banana" "cherry")
echo ${fruits[1]}  # 輸出 banana
```

### 宣告一個環境變數
```bash
declare -x PATH="/usr/local/bin:$PATH"
echo $PATH  # 輸出更新後的 PATH
```

## Tips
- 使用 `declare -p` 可以查看變數的屬性及其當前值。
- 在腳本開頭使用 `declare` 可以清楚地定義變數，增強可讀性。
- 當需要保護變數不被修改時，使用 `-r` 選項是個好習慣。