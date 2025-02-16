# [台灣] Bash nslookup 使用方法: 查詢域名的IP地址

## Overview
`nslookup` 是一個用於查詢域名系統（DNS）的命令行工具。它可以幫助用戶獲取域名對應的IP地址，或是反向查詢IP地址以獲取相應的域名。

## Usage
基本語法如下：
```bash
nslookup [選項] [參數]
```

## Common Options
- `-type=TYPE`：指定查詢的記錄類型，例如 A、MX、CNAME 等。
- `-timeout=SEC`：設定查詢超時的時間（以秒為單位）。
- `-retry=NUM`：設定查詢失敗後的重試次數。

## Common Examples
以下是一些常見的使用範例：

1. 查詢域名的IP地址：
   ```bash
   nslookup example.com
   ```

2. 查詢特定類型的DNS記錄（例如MX記錄）：
   ```bash
   nslookup -type=MX example.com
   ```

3. 反向查詢IP地址以獲取域名：
   ```bash
   nslookup 93.184.216.34
   ```

4. 設定查詢的DNS伺服器：
   ```bash
   nslookup example.com 8.8.8.8
   ```

## Tips
- 使用 `-debug` 選項可以獲取更詳細的查詢過程，幫助排除故障。
- 當查詢失敗時，檢查網路連接或DNS伺服器的可用性。
- 可以將 `nslookup` 與其他命令結合使用，例如在腳本中自動化查詢過程。