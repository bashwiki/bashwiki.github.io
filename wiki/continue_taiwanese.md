# [Linux] Bash continue 使用法: 繼續執行迴圈

## Overview
`continue` 命令用於在迴圈中跳過當前的迭代，並立即開始下一次迭代。這在需要根據特定條件跳過某些步驟時非常有用。

## Usage
基本語法如下：
```
continue [n]
```
其中 `n` 是可選的，表示跳過的迭代次數。

## Common Options
- `n`：指定要跳過的迭代次數。如果不指定，則默認為 1，表示跳過當前迭代。

## Common Examples

### 範例 1：在 for 迴圈中使用 continue
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "Number: $i"
done
```
這段程式碼會輸出 1、2、4 和 5，因為當 `i` 等於 3 時，`continue` 命令會跳過該迭代。

### 範例 2：在 while 迴圈中使用 continue
```bash
count=1
while [ $count -le 5 ]; do
    if [ $count -eq 4 ]; then
        count=$((count + 1))
        continue
    fi
    echo "Count: $count"
    count=$((count + 1))
done
```
這段程式碼會輸出 1、2、3 和 5，因為當 `count` 等於 4 時，`continue` 命令會跳過該迭代。

### 範例 3：使用 continue 跳過特定條件
```bash
for num in {1..10}; do
    if [ $((num % 2)) -eq 0 ]; then
        continue
    fi
    echo "Odd Number: $num"
done
```
這段程式碼會輸出所有的奇數：1、3、5、7 和 9。

## Tips
- 使用 `continue` 時，確保你了解迴圈的邏輯，以免意外跳過重要的步驟。
- 在複雜的迴圈中，考慮使用註解來說明 `continue` 的用途，讓程式碼更易於理解。
- 測試你的迴圈邏輯，確保在特定條件下 `continue` 的行為符合預期。