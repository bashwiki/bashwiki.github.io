# [台灣] Bash scp 使用方法: 複製檔案至遠端伺服器

## Overview
`scp`（Secure Copy Protocol）是一個用於在本地和遠端伺服器之間安全地複製檔案或目錄的命令。它利用 SSH 協議來加密傳輸過程，確保資料的安全性。

## Usage
基本語法如下：
```bash
scp [options] [source] [destination]
```

## Common Options
- `-r`: 遞迴複製整個目錄。
- `-P`: 指定遠端伺服器的端口號（注意是大寫的 P）。
- `-i`: 指定使用的 SSH 私鑰檔案。
- `-v`: 顯示詳細的傳輸過程，用於除錯。

## Common Examples
1. 複製本地檔案到遠端伺服器：
   ```bash
   scp /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
   ```

2. 複製遠端檔案到本地：
   ```bash
   scp user@remote_host:/path/to/remote/file.txt /path/to/local/directory/
   ```

3. 遞迴複製整個目錄到遠端伺服器：
   ```bash
   scp -r /path/to/local/directory user@remote_host:/path/to/remote/directory/
   ```

4. 使用指定的 SSH 私鑰檔案進行複製：
   ```bash
   scp -i /path/to/private_key.pem /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
   ```

## Tips
- 確保 SSH 服務在遠端伺服器上運行，並且您有正確的訪問權限。
- 使用 `-v` 選項可以幫助您排除問題，特別是在連接失敗時。
- 當複製大型檔案時，考慮使用 `-C` 選項來啟用壓縮，以加快傳輸速度。