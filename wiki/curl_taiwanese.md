# [台灣] Bash curl 使用法: 用於傳輸資料的工具

## Overview
`curl` 是一個用於在網路上傳輸資料的命令行工具。它支持多種協議，包括 HTTP、HTTPS、FTP 等，並且可以用來發送請求、下載檔案或與 API 互動。

## Usage
基本語法如下：
```bash
curl [options] [arguments]
```

## Common Options
- `-X`: 指定 HTTP 方法，例如 GET、POST 等。
- `-d`: 傳送數據，通常用於 POST 請求。
- `-H`: 添加自定義的 HTTP 標頭。
- `-o`: 將輸出保存到檔案中。
- `-I`: 只獲取 HTTP 標頭。

## Common Examples
以下是一些常見的 `curl` 使用範例：

1. 獲取網頁內容：
   ```bash
   curl http://example.com
   ```

2. 下載檔案並保存：
   ```bash
   curl -o myfile.txt http://example.com/file.txt
   ```

3. 發送 POST 請求：
   ```bash
   curl -X POST -d "name=John&age=30" http://example.com/api
   ```

4. 添加自定義標頭：
   ```bash
   curl -H "Authorization: Bearer token" http://example.com/api
   ```

5. 獲取 HTTP 標頭：
   ```bash
   curl -I http://example.com
   ```

## Tips
- 使用 `-s` 選項可以讓 `curl` 在執行時不顯示進度條，適合在腳本中使用。
- 結合 `-o` 和 `-L` 來處理重定向的下載。
- 測試 API 時，可以使用 `-v` 選項來查看詳細的請求和響應過程，這對於除錯非常有幫助。