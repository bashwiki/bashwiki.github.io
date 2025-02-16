# [台灣] Bash traceroute 用法: 追蹤網路路徑

## Overview
`traceroute` 命令用於顯示從本地計算機到目標主機之間的路由路徑。它可以幫助用戶了解數據包在網絡中傳輸的過程，並識別可能的延遲或問題點。

## Usage
基本語法如下：
```bash
traceroute [options] [arguments]
```

## Common Options
- `-m <max_ttl>`: 設定最大生存時間（TTL），限制跳數。
- `-p <port>`: 指定使用的端口號。
- `-n`: 直接使用IP地址而不進行域名解析。
- `-w <timeout>`: 設定每個回應的超時時間（秒）。

## Common Examples
1. 基本使用，追蹤到某個網站的路徑：
   ```bash
   traceroute example.com
   ```

2. 使用指定的端口號：
   ```bash
   traceroute -p 80 example.com
   ```

3. 限制最大跳數為 10：
   ```bash
   traceroute -m 10 example.com
   ```

4. 不進行域名解析，直接顯示IP地址：
   ```bash
   traceroute -n example.com
   ```

5. 設定每個回應的超時時間為 2 秒：
   ```bash
   traceroute -w 2 example.com
   ```

## Tips
- 在進行故障排除時，使用 `-n` 選項可以加快顯示速度，因為不需要進行DNS查詢。
- 如果你發現某個跳數的延遲異常，可以進一步使用 `ping` 命令來檢查該節點的狀態。
- 使用 `-m` 選項來避免不必要的長時間追蹤，特別是在連接不穩定的情況下。