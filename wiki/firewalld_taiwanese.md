# [Linux] Bash firewalld 使用法: 管理防火牆設定

## Overview
`firewalld` 是一個動態防火牆管理工具，主要用於管理 Linux 系統的網路流量。它提供了一個簡單的界面來設置和管理防火牆規則，支持區域和服務的概念，讓用戶能夠更靈活地控制進出系統的流量。

## Usage
基本語法如下：
```bash
firewalld [options] [arguments]
```

## Common Options
- `--zone=<zone>`: 指定要使用的區域。
- `--add-service=<service>`: 將指定的服務添加到防火牆規則中。
- `--remove-service=<service>`: 從防火牆規則中移除指定的服務。
- `--add-port=<port>/<protocol>`: 開放指定的端口和協議。
- `--remove-port=<port>/<protocol>`: 關閉指定的端口和協議。
- `--list-all`: 列出當前區域的所有設定。

## Common Examples
1. **查看當前防火牆狀態**
   ```bash
   firewall-cmd --state
   ```

2. **列出所有區域的設定**
   ```bash
   firewall-cmd --get-active-zones
   ```

3. **添加 HTTP 服務到防火牆**
   ```bash
   firewall-cmd --add-service=http --permanent
   ```

4. **開放特定端口（例如 8080）**
   ```bash
   firewall-cmd --add-port=8080/tcp --permanent
   ```

5. **重新載入防火牆設定**
   ```bash
   firewall-cmd --reload
   ```

## Tips
- 使用 `--permanent` 選項可以確保設定在防火牆重啟後依然有效。
- 在進行任何更改之前，建議先備份當前的防火牆設定。
- 定期檢查防火牆的狀態和規則，以確保系統的安全性。