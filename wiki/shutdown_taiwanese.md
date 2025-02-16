# [台灣] Bash shutdown 使用法: 關閉系統

## Overview
`shutdown` 命令用於安全地關閉或重啟系統。這個命令可以讓使用者選擇立即關閉、延遲關閉或重啟系統，並且可以選擇是否發送警告給其他使用者。

## Usage
基本語法如下：
```
shutdown [options] [arguments]
```

## Common Options
- `-h`：關閉系統。
- `-r`：重啟系統。
- `-t`：設定關閉或重啟的延遲時間（以秒為單位）。
- `now`：立即執行關閉或重啟。
- `+m`：在指定的分鐘後執行關閉或重啟（例如 `+5` 表示 5 分鐘後）。

## Common Examples
- 立即關閉系統：
  ```bash
  shutdown -h now
  ```

- 立即重啟系統：
  ```bash
  shutdown -r now
  ```

- 在 10 分鐘後關閉系統：
  ```bash
  shutdown -h +10
  ```

- 在 5 分鐘後重啟系統：
  ```bash
  shutdown -r +5
  ```

- 發送關閉警告給其他使用者：
  ```bash
  shutdown -h +1 "系統將在 1 分鐘後關閉，請儲存您的工作。"
  ```

## Tips
- 在執行關閉或重啟命令之前，最好通知其他使用者，以避免資料遺失。
- 使用 `shutdown -c` 可以取消已排定的關閉或重啟。
- 確保您擁有適當的權限來執行 `shutdown` 命令，通常需要 root 權限。