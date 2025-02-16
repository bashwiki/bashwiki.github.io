# [Linux] Bash break 使用法: 終止迴圈

## Overview
`break` 命令用於終止最內層的迴圈，讓程式流程跳出當前的迴圈結構。這在需要根據特定條件提前結束迴圈時非常有用。

## Usage
基本語法如下：
```bash
break [n]
```
其中 `n` 是一個可選的參數，表示要終止的迴圈層級，預設為 1。

## Common Options
- `n`: 指定要終止的迴圈層級，若不提供，則終止最近的一層迴圈。

## Common Examples

### 終止單層迴圈
當迴圈中的條件滿足時，使用 `break` 終止迴圈。
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        break
    fi
    echo $i
done
```
輸出：
```
1
2
```

### 終止多層迴圈
可以使用 `n` 參數來終止指定層級的迴圈。
```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            break 2
        fi
        echo "i: $i, j: $j"
    done
done
```
輸出：
```
i: 1, j: 1
```

### 與 while 迴圈搭配使用
在 `while` 迴圈中也可以使用 `break` 來終止迴圈。
```bash
count=1
while [ $count -le 5 ]; do
    if [ $count -eq 4 ]; then
        break
    fi
    echo $count
    count=$((count + 1))
done
```
輸出：
```
1
2
3
```

## Tips
- 在使用 `break` 時，確保清楚了解迴圈的結構，以避免意外終止不該終止的迴圈。
- 使用 `break` 可以提高程式的效率，特別是在處理大型資料集時，能夠避免不必要的迴圈運算。
- 結合 `continue` 命令使用，可以更靈活地控制迴圈的流程。