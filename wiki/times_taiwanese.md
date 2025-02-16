# [Linux] Bash times 使用法: 計算執行時間

## Overview
`times` 命令用於顯示當前 shell 進程及其子進程的執行時間。這些時間包括用於用戶模式和系統模式的 CPU 時間，對於性能分析和優化非常有用。

## Usage
基本語法如下：
```bash
times [options] [arguments]
```

## Common Options
- `-p`: 以 POSIX 格式輸出時間，這樣更容易與其他工具一起使用。

## Common Examples
以下是一些常見的使用範例：

1. **顯示當前 shell 的執行時間**
   ```bash
   times
   ```

2. **使用 POSIX 格式顯示執行時間**
   ```bash
   times -p
   ```

3. **在執行其他命令後查看時間**
   ```bash
   sleep 5
   times
   ```

## Tips
- 在執行長時間運行的腳本或命令後使用 `times`，可以幫助你了解資源的使用情況。
- 如果你需要將時間輸出格式化以便於分析，可以考慮使用 `times -p` 來獲得更一致的格式。