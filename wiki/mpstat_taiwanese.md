# [台灣] Bash mpstat 用法: 監控 CPU 使用情況

## Overview
`mpstat` 是一個用於顯示各個 CPU 核心的使用情況的命令。它可以幫助用戶監控系統的 CPU 負載，並分析性能瓶頸。

## Usage
基本語法如下：
```bash
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`：顯示所有 CPU 核心的使用情況。
- `-u`：顯示 CPU 使用率。
- `-h`：以可讀性更高的格式顯示輸出。
- `-o`：將輸出保存到指定的文件中。

## Common Examples
1. 顯示所有 CPU 核心的使用情況：
   ```bash
   mpstat -P ALL
   ```

2. 每 2 秒更新一次 CPU 使用率：
   ```bash
   mpstat 2
   ```

3. 將 CPU 使用情況輸出到文件：
   ```bash
   mpstat -o JSON > cpu_usage.json
   ```

4. 顯示 CPU 使用率，並以可讀性更高的格式輸出：
   ```bash
   mpstat -u -h
   ```

## Tips
- 定期監控 CPU 使用情況可以幫助及早發現性能問題。
- 使用 `-P ALL` 選項可以獲得更詳細的資訊，特別是在多核心系統上。
- 將輸出保存到文件中，可以方便後續的分析和報告。