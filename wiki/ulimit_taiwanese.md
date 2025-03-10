# [Linux] Bash ulimit 使用說明: 設定資源限制

## Overview
`ulimit` 是一個用於設定或顯示當前 shell 進程可用資源限制的命令。這些限制可以防止單一進程消耗過多的系統資源，從而保護系統的穩定性。

## Usage
基本語法如下：
```
ulimit [選項] [參數]
```

## Common Options
- `-a`：顯示所有資源限制的當前值。
- `-c`：設定核心檔案的大小限制（以字節為單位）。
- `-d`：設定數據段的大小限制（以字節為單位）。
- `-f`：設定檔案大小限制（以字節為單位）。
- `-l`：設定可鎖定的內存大小限制（以字節為單位）。
- `-m`：設定物理內存的大小限制（以字節為單位）。
- `-n`：設定可打開的檔案數量限制。
- `-s`：設定堆疊大小限制（以字節為單位）。
- `-t`：設定 CPU 時間限制（以秒為單位）。
- `-u`：設定每個用戶可擁有的進程數量限制。

## Common Examples
- 顯示所有資源限制：
  ```bash
  ulimit -a
  ```

- 設定最大可打開檔案數量為 1024：
  ```bash
  ulimit -n 1024
  ```

- 設定核心檔案大小限制為 0（禁用核心檔案生成）：
  ```bash
  ulimit -c 0
  ```

- 設定堆疊大小限制為 8MB：
  ```bash
  ulimit -s 8192
  ```

- 設定 CPU 時間限制為 60 秒：
  ```bash
  ulimit -t 60
  ```

## Tips
- 在修改資源限制之前，建議先使用 `ulimit -a` 查看當前設置，以避免不必要的錯誤。
- 設定的限制只對當前 shell 及其子進程有效，若要永久生效，需將設定添加到用戶的啟動檔案（如 `.bashrc`）。
- 注意，某些系統限制可能會受到系統管理員的設定影響，無法隨意更改。