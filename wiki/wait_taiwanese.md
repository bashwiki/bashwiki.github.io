# [Linux] Bash wait 使用法: 等待子程序結束

## Overview
`wait` 命令用於等待一個或多個子程序的結束，並返回其退出狀態。這在腳本中非常有用，當你需要確保某些任務完成後再執行後續操作時。

## Usage
基本語法如下：
```
wait [options] [arguments]
```

## Common Options
- `-n`：等待下一個子程序結束，而不是所有子程序。
- `-p`：等待指定的進程ID（PID）結束。
- `-f`：在等待時，強制等待所有子程序，即使它們在背景中運行。

## Common Examples

### 等待所有子程序結束
```bash
#!/bin/bash
sleep 3 &
sleep 5 &
wait
echo "所有子程序已結束"
```

### 等待特定的子程序
```bash
#!/bin/bash
sleep 3 &
pid=$!
echo "等待進程 $pid 結束"
wait $pid
echo "進程 $pid 已結束"
```

### 使用 `-n` 等待下一個子程序
```bash
#!/bin/bash
sleep 3 &
sleep 5 &
wait -n
echo "下一個子程序已結束"
```

## Tips
- 在腳本中使用 `wait` 可以確保資源的正確釋放，避免潛在的資源衝突。
- 使用 `$?` 可以獲取最後一個子程序的退出狀態，這對於錯誤處理非常重要。
- 如果你在腳本中啟動多個背景進程，使用 `wait` 可以幫助你控制執行流程，確保所有任務完成後再進行後續操作。