# [Linux] Bash logrotate 使用法: 管理日誌檔案的輪替

## Overview
logrotate 是一個用於管理系統日誌檔案的工具，可以自動輪替、壓縮、刪除和郵寄日誌檔案。這樣可以防止日誌檔案佔用過多的磁碟空間，並保持系統的整潔。

## Usage
基本語法如下：
```
logrotate [options] [arguments]
```

## Common Options
- `-f`：強制執行日誌輪替，即使沒有達到輪替條件。
- `-s`：指定狀態檔案的位置，狀態檔案用於記錄上次輪替的狀態。
- `-v`：啟用詳細模式，顯示執行過程中的詳細信息。
- `-d`：進入調試模式，顯示將要執行的操作，但不實際執行。

## Common Examples
以下是一些常見的使用範例：

1. **手動執行日誌輪替**
   ```bash
   logrotate -f /etc/logrotate.conf
   ```

2. **使用自定義狀態檔案**
   ```bash
   logrotate -s /path/to/statefile /etc/logrotate.conf
   ```

3. **查看詳細執行過程**
   ```bash
   logrotate -v /etc/logrotate.conf
   ```

4. **進入調試模式**
   ```bash
   logrotate -d /etc/logrotate.conf
   ```

## Tips
- 確保定期檢查 logrotate 的配置檔，以便適應系統日誌的變化。
- 使用 `logrotate` 的 `-d` 選項來測試配置，避免意外刪除重要日誌。
- 考慮將日誌檔案壓縮，以節省磁碟空間，這可以在 logrotate 的配置中設定。