# [台灣] Bash ping 用法: 測試網路連接

## Overview
`ping` 命令用來測試與另一台主機的網路連接。它透過發送 ICMP 回音請求來檢查目標主機是否可達，並計算回應時間。

## Usage
基本語法如下：
```
ping [選項] [主機名稱或 IP 位址]
```

## Common Options
- `-c [次數]`：指定發送的回音請求數量。
- `-i [秒數]`：設定發送請求的間隔時間（預設為 1 秒）。
- `-t [TTL]`：設定存活時間（Time To Live），限制封包的跳數。
- `-s [大小]`：指定發送的封包大小。

## Common Examples
1. **基本使用**：測試與 Google 的連接。
   ```bash
   ping google.com
   ```

2. **指定發送次數**：發送 4 次請求。
   ```bash
   ping -c 4 google.com
   ```

3. **設定封包大小**：發送 1000 字節的封包。
   ```bash
   ping -s 1000 google.com
   ```

4. **設定發送間隔**：每 2 秒發送一次請求。
   ```bash
   ping -i 2 google.com
   ```

5. **設定 TTL**：限制封包的跳數為 64。
   ```bash
   ping -t 64 google.com
   ```

## Tips
- 使用 `-c` 選項可以避免無限迴圈，方便測試。
- 在網路故障排除時，記得檢查防火牆設定，可能會影響 `ping` 的結果。
- 若要測試內部網路設備，使用其內部 IP 位址會更有效。