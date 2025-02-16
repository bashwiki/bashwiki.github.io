# [台灣] Bash shopt 用法: 設定 Bash 行為的選項

## Overview
`shopt` 是一個用於設定和查詢 Bash 的行為選項的命令。它可以幫助用戶開啟或關閉某些功能，以便自訂 Bash 環境。

## Usage
基本語法如下：
```
shopt [options] [arguments]
```

## Common Options
- `-s`：啟用指定的選項。
- `-u`：禁用指定的選項。
- `-p`：列出所有選項及其當前狀態。

## Common Examples
1. **啟用 `nullglob` 選項**：
   ```bash
   shopt -s nullglob
   ```
   這樣當沒有匹配的檔案時，通配符不會返回自身。

2. **禁用 `dotglob` 選項**：
   ```bash
   shopt -u dotglob
   ```
   這樣在使用通配符時，隱藏檔案不會被包含在內。

3. **列出所有選項及其狀態**：
   ```bash
   shopt -p
   ```
   這會顯示所有可用的選項及其當前的啟用或禁用狀態。

## Tips
- 在修改選項之前，可以使用 `shopt -p` 來檢查當前的選項狀態，以避免不必要的變更。
- 使用 `nullglob` 可以在處理檔案時避免錯誤，特別是在腳本中使用通配符時。
- 將常用的 `shopt` 設定添加到你的 `.bashrc` 文件中，以便每次啟動終端時自動應用。