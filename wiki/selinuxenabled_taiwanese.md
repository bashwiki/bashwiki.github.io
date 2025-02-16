# [Linux] Bash selinuxenabled 使用方法: 檢查 SELinux 狀態

## Overview
`selinuxenabled` 是一個用來檢查系統中 SELinux（安全增強 Linux）是否啟用的命令。當這個命令返回 0 時，表示 SELinux 已啟用；如果返回 1，則表示未啟用。

## Usage
基本語法如下：
```bash
selinuxenabled [options]
```

## Common Options
`selinuxenabled` 命令並沒有太多選項，主要是用來簡單檢查 SELinux 的狀態。以下是一些常見的選項：

- `-h`, `--help`: 顯示幫助信息。
- `-V`, `--version`: 顯示版本信息。

## Common Examples
以下是一些實用的範例：

1. **檢查 SELinux 是否啟用**
   ```bash
   selinuxenabled
   ```

2. **檢查 SELinux 狀態並根據返回碼執行不同操作**
   ```bash
   if selinuxenabled; then
       echo "SELinux is enabled."
   else
       echo "SELinux is disabled."
   fi
   ```

3. **顯示幫助信息**
   ```bash
   selinuxenabled --help
   ```

## Tips
- 在使用 `selinuxenabled` 前，確保你有適當的權限來執行此命令，通常需要在具有管理權限的終端中運行。
- 此命令非常適合在腳本中使用，以便根據 SELinux 的狀態執行不同的操作。