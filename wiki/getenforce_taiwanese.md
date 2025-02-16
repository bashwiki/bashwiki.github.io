# [Linux] Bash getenforce 使用方法: 查詢 SELinux 狀態

## Overview
`getenforce` 是一個用於查詢 SELinux（安全增強 Linux）當前運行模式的命令。它可以幫助用戶了解系統的安全性設置，並確定 SELinux 是啟用、禁用還是處於寬鬆模式。

## Usage
基本語法如下：
```bash
getenforce [options]
```

## Common Options
`getenforce` 命令沒有特定的選項，因為它主要用於顯示當前的 SELinux 狀態。它的輸出結果可能是以下三種之一：
- `Enforcing`：表示 SELinux 正在強制執行安全策略。
- `Permissive`：表示 SELinux 正在以寬鬆模式運行，僅記錄違規事件，但不強制執行。
- `Disabled`：表示 SELinux 已被禁用。

## Common Examples
以下是一些常見的用法示例：

1. 查詢當前 SELinux 狀態：
   ```bash
   getenforce
   ```

2. 在腳本中使用 `getenforce` 來檢查 SELinux 狀態：
   ```bash
   if [ "$(getenforce)" == "Enforcing" ]; then
       echo "SELinux is enforcing."
   else
       echo "SELinux is not enforcing."
   fi
   ```

3. 結合其他命令使用，例如檢查 SELinux 狀態並顯示系統信息：
   ```bash
   echo "Current SELinux status: $(getenforce)"
   uname -a
   ```

## Tips
- 在進行系統管理或安全配置時，定期檢查 SELinux 狀態是個好習慣。
- 如果你在開發過程中遇到權限問題，檢查 SELinux 狀態可能會提供有用的線索。
- 使用 `sestatus` 命令可以獲得更詳細的 SELinux 信息，包括策略和上下文。