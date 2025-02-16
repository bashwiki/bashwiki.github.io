# [台灣] Bash rar 用法: 壓縮和解壓縮檔案

## Overview
`rar` 是一個用於壓縮和解壓縮檔案的命令行工具。它可以將多個檔案和資料夾打包成一個壓縮檔案，並且支援多種壓縮格式，特別是 RAR 格式。

## Usage
基本的命令語法如下：

```bash
rar [options] [arguments]
```

## Common Options
- `a`：新增檔案到壓縮檔案中。
- `x`：從壓縮檔案中提取檔案。
- `t`：測試壓縮檔案的完整性。
- `v`：顯示詳細的壓縮過程。
- `m`：設置壓縮等級（0-5，0為不壓縮，5為最大壓縮）。

## Common Examples
- **壓縮檔案**：
  ```bash
  rar a archive.rar file1.txt file2.txt
  ```
  這個命令會將 `file1.txt` 和 `file2.txt` 壓縮成 `archive.rar`。

- **解壓縮檔案**：
  ```bash
  rar x archive.rar
  ```
  這個命令會將 `archive.rar` 中的所有檔案解壓縮到當前目錄。

- **測試壓縮檔案的完整性**：
  ```bash
  rar t archive.rar
  ```
  這個命令會檢查 `archive.rar` 的完整性，確保檔案沒有損壞。

- **設置壓縮等級**：
  ```bash
  rar a -m5 archive.rar file1.txt
  ```
  這個命令會以最高壓縮等級將 `file1.txt` 壓縮到 `archive.rar`。

## Tips
- 在壓縮大量檔案時，考慮使用 `-v` 選項來獲取詳細的進度資訊。
- 定期測試壓縮檔案的完整性，以避免資料損壞。
- 使用適當的壓縮等級來平衡壓縮速度和檔案大小，根據需求選擇合適的等級。