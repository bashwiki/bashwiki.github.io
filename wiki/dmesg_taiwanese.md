# [Linux] Bash dmesg 用法: 查看內核環境信息

## Overview
`dmesg` 命令用於顯示內核環境信息，特別是啟動過程中的信息和設備驅動程序的日誌。這些信息對於診斷系統問題和了解硬體狀態非常有用。

## Usage
基本語法如下：
```bash
dmesg [options] [arguments]
```

## Common Options
- `-C`：清除當前的緩衝區。
- `-n level`：設置日誌級別，僅顯示指定級別以上的消息。
- `-T`：將時間戳轉換為人類可讀的格式。
- `-w`：持續監視內核消息，類似於 `tail -f`。

## Common Examples
1. 查看所有內核消息：
   ```bash
   dmesg
   ```

2. 以人類可讀的格式查看內核消息：
   ```bash
   dmesg -T
   ```

3. 清除當前的緩衝區：
   ```bash
   dmesg -C
   ```

4. 監視新的內核消息：
   ```bash
   dmesg -w
   ```

5. 設置日誌級別為 3，僅顯示警告及以上級別的消息：
   ```bash
   dmesg -n 3
   ```

## Tips
- 定期檢查 `dmesg` 輸出可以幫助你及早發現硬體問題。
- 使用 `dmesg -T` 可以更方便地理解時間戳，特別是在排查問題時。
- 當系統啟動時，`dmesg` 的輸出可以提供關於啟動過程的詳細信息，對於系統管理員來說非常重要。