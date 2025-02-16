# [台灣] Bash tcpdump 使用方法: 捕獲網路封包

## Overview
tcpdump 是一個強大的命令行工具，用於捕獲和分析網路封包。它可以幫助用戶監控網路流量，診斷網路問題，或進行安全分析。

## Usage
基本語法如下：
```bash
tcpdump [options] [arguments]
```

## Common Options
- `-i <interface>`: 指定要監控的網路介面。
- `-n`: 不解析主機名稱，顯示 IP 地址。
- `-c <count>`: 捕獲指定數量的封包後停止。
- `-w <file>`: 將捕獲的封包寫入檔案。
- `-r <file>`: 從檔案中讀取封包進行分析。
- `-s <snaplen>`: 設定捕獲的封包大小。

## Common Examples
捕獲所有流量：
```bash
tcpdump
```

捕獲特定介面的流量：
```bash
tcpdump -i eth0
```

捕獲指定數量的封包：
```bash
tcpdump -c 10
```

將捕獲的封包寫入檔案：
```bash
tcpdump -w output.pcap
```

從檔案中讀取封包：
```bash
tcpdump -r output.pcap
```

## Tips
- 在使用 tcpdump 時，最好以 root 權限運行，以獲取完整的封包資訊。
- 使用 `-n` 選項可以加快捕獲速度，因為不需要進行 DNS 查詢。
- 定期檢查捕獲的封包大小，避免佔用過多磁碟空間。