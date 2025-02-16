# [台灣] Bash iostat 使用方法: 監控系統 I/O 性能

## Overview
`iostat` 是一個用於監控系統輸入/輸出 (I/O) 性能的命令。它可以顯示 CPU 使用率以及每個設備的 I/O 活動，幫助用戶分析系統性能瓶頸。

## Usage
基本語法如下：
```
iostat [選項] [參數]
```

## Common Options
- `-c`：顯示 CPU 使用情況。
- `-d`：顯示設備的 I/O 統計數據。
- `-x`：顯示擴展的設備 I/O 統計數據。
- `-h`：以可讀性更高的格式顯示數據（例如，使用 KB、MB 等單位）。
- `-t`：顯示時間戳。

## Common Examples
以下是一些常見的 `iostat` 使用範例：

1. 顯示 CPU 使用情況：
   ```bash
   iostat -c
   ```

2. 顯示所有設備的 I/O 統計數據：
   ```bash
   iostat -d
   ```

3. 顯示擴展的設備 I/O 統計數據：
   ```bash
   iostat -dx
   ```

4. 每 2 秒更新一次 I/O 統計數據：
   ```bash
   iostat -d 2
   ```

5. 顯示帶有時間戳的 I/O 統計數據：
   ```bash
   iostat -d -t
   ```

## Tips
- 使用 `iostat` 時，建議定期監控系統性能，以便及早發現潛在的問題。
- 結合其他工具（如 `vmstat` 和 `mpstat`）使用，可以獲得更全面的系統性能分析。
- 如果系統中有多個磁碟，使用 `-x` 選項可以獲得更詳細的每個磁碟的性能數據，幫助定位瓶頸。