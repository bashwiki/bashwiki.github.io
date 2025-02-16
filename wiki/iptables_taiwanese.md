# [台灣] Bash iptables 使用方式: 管理網路流量的防火牆

## Overview
iptables 是一個用於設定和管理 Linux 系統防火牆的命令行工具。它可以控制進出系統的網路流量，並根據設定的規則來允許或拒絕特定的連接。

## Usage
基本語法如下：
```bash
iptables [options] [arguments]
```

## Common Options
- `-A`：添加一條規則到指定的鏈。
- `-D`：刪除指定鏈中的一條規則。
- `-L`：列出當前的規則。
- `-F`：清空指定鏈中的所有規則。
- `-P`：設定預設策略（接受或拒絕）。

## Common Examples
1. **列出當前的規則**
   ```bash
   iptables -L
   ```

2. **添加一條規則以允許 HTTP 流量**
   ```bash
   iptables -A INPUT -p tcp --dport 80 -j ACCEPT
   ```

3. **刪除一條規則**
   ```bash
   iptables -D INPUT -p tcp --dport 80 -j ACCEPT
   ```

4. **清空所有規則**
   ```bash
   iptables -F
   ```

5. **設定預設策略為拒絕所有進入流量**
   ```bash
   iptables -P INPUT DROP
   ```

## Tips
- 在修改 iptables 規則之前，建議先備份當前的規則，以便於恢復。
- 測試新規則時，可以使用 `-n` 參數來避免 DNS 查詢，這樣可以加快顯示速度。
- 定期檢查和更新規則，以確保防火牆的安全性和有效性。