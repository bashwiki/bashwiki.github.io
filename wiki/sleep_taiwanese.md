# [Linux] Bash sleep 用法: 暫停執行

## Overview
`sleep` 命令用於暫停執行一段指定的時間。這在腳本中非常有用，當你需要等待某些操作完成或是控制執行的節奏時。

## Usage
基本語法如下：
```
sleep [options] [arguments]
```

## Common Options
- `-m`：以分鐘為單位指定時間。
- `-s`：以秒為單位指定時間（預設為秒）。
- `-h`：以小時為單位指定時間。

## Common Examples
以下是一些常見的使用範例：

1. 暫停 5 秒：
   ```bash
   sleep 5
   ```

2. 暫停 2 分鐘：
   ```bash
   sleep 2m
   ```

3. 暫停 1 小時：
   ```bash
   sleep 1h
   ```

4. 在腳本中使用 sleep 來延遲執行：
   ```bash
   #!/bin/bash
   echo "開始執行..."
   sleep 10
   echo "10 秒後繼續執行"
   ```

## Tips
- 使用 `sleep` 時，確保你知道需要等待的時間，避免不必要的延遲。
- 在長時間運行的腳本中，適當使用 `sleep` 可以減少系統資源的使用。
- 結合 `&&` 或 `;` 使用 `sleep` 可以在多個命令之間添加延遲。