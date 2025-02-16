# [台灣] Bash htop 使用法: 監控系統資源

## Overview
htop 是一個互動式的進程查看器，能夠顯示系統的資源使用情況，包括 CPU、記憶體和進程等。它提供了一個友好的使用者介面，讓使用者能夠更輕鬆地監控和管理系統資源。

## Usage
基本語法如下：
```bash
htop [options] [arguments]
```

## Common Options
- `-h`, `--help`: 顯示幫助資訊。
- `-s`, `--sort`: 設定排序方式，例如 `-s PERCENT_CPU` 依 CPU 使用率排序。
- `-p`, `--pid`: 只顯示指定的進程 ID，例如 `-p 1234`。
- `-u`, `--user`: 只顯示指定用戶的進程，例如 `-u username`。

## Common Examples
- 啟動 htop：
  ```bash
  htop
  ```

- 依 CPU 使用率排序：
  ```bash
  htop -s PERCENT_CPU
  ```

- 只顯示特定進程：
  ```bash
  htop -p 1234
  ```

- 只顯示特定用戶的進程：
  ```bash
  htop -u username
  ```

## Tips
- 使用方向鍵來瀏覽進程列表，並按 `F9` 可以終止選中的進程。
- 可以按 `F2` 進入設定選單，自訂顯示的內容和排序方式。
- 利用 `F3` 和 `F4` 進行搜尋和過濾進程，讓你更快速找到需要的進程。