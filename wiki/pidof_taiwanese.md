# [Linux] Bash pidof 使用法: 獲取進程ID

## Overview
`pidof` 命令用於查詢指定程序的進程ID（PID）。這在管理系統進程時非常有用，特別是當你需要終止或監控特定程序時。

## Usage
基本語法如下：
```
pidof [options] [arguments]
```

## Common Options
- `-o`：排除指定的進程ID。
- `-s`：只顯示第一個找到的進程ID。
- `-c`：顯示進程的命令行。

## Common Examples
以下是一些常見的使用範例：

1. 獲取 `bash` 進程的ID：
   ```bash
   pidof bash
   ```

2. 獲取 `nginx` 進程的ID，並排除特定的進程：
   ```bash
   pidof -o <PID> nginx
   ```

3. 獲取 `httpd` 進程的第一個ID：
   ```bash
   pidof -s httpd
   ```

4. 獲取 `python` 進程的ID並顯示命令行：
   ```bash
   pidof -c python
   ```

## Tips
- 使用 `pidof` 時，確保指定的程序名稱正確無誤，否則將無法找到對應的進程ID。
- 結合其他命令如 `kill` 使用，可以方便地終止特定進程，例如：
  ```bash
  kill $(pidof <process_name>)
  ```
- 若要獲取多個進程的ID，直接列出進程名稱即可：
  ```bash
  pidof process1 process2
  ```