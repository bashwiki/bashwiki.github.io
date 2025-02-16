# [Linux] Bash journalctl 使用法: 查看系統日誌

## Overview
`journalctl` 是一個用於查看和管理系統日誌的命令，這些日誌由 systemd 的日誌系統收集。它可以幫助用戶檢查系統狀態、故障排除和監控系統活動。

## Usage
基本語法如下：
```
journalctl [options] [arguments]
```

## Common Options
- `-b`：顯示當前啟動以來的日誌。
- `-f`：實時跟蹤日誌輸出，類似於 `tail -f`。
- `--since`：顯示自指定時間以來的日誌，例如 `--since "2023-10-01"`。
- `--until`：顯示直到指定時間的日誌，例如 `--until "2023-10-02"`。
- `-u`：顯示特定單元（service）的日誌，例如 `-u ssh.service`。

## Common Examples
- 查看所有日誌：
  ```bash
  journalctl
  ```

- 查看當前啟動以來的日誌：
  ```bash
  journalctl -b
  ```

- 實時跟蹤日誌輸出：
  ```bash
  journalctl -f
  ```

- 查看特定服務的日誌：
  ```bash
  journalctl -u nginx.service
  ```

- 查看自特定日期以來的日誌：
  ```bash
  journalctl --since "2023-10-01"
  ```

## Tips
- 使用 `-p` 選項可以根據日誌的嚴重性過濾，例如 `-p err` 只顯示錯誤日誌。
- 結合 `--no-pager` 選項可以直接在終端中顯示所有日誌，而不使用分頁器。
- 定期檢查日誌可以幫助及早發現系統問題，建議將其納入日常維護工作中。