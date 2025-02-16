# [Linux] Bash groupmod 使用法: 修改群組屬性

## Overview
`groupmod` 命令用於修改現有群組的屬性。這個命令可以用來改變群組名稱或群組的其他屬性，幫助系統管理員有效地管理用戶群組。

## Usage
基本語法如下：
```bash
groupmod [選項] [參數]
```

## Common Options
- `-n, --new-name <新名稱>`: 將群組名稱更改為指定的新名稱。
- `-g, --gid <新GID>`: 更改群組的 GID（群組識別碼）。
- `-h, --help`: 顯示幫助信息並退出。
- `-o, --non-unique`: 允許使用非唯一的 GID。

## Common Examples
以下是一些常見的使用範例：

1. 更改群組名稱：
   ```bash
   groupmod -n newgroup oldgroup
   ```

2. 更改群組的 GID：
   ```bash
   groupmod -g 1001 groupname
   ```

3. 使用非唯一 GID：
   ```bash
   groupmod -o -g 1000 anothergroup
   ```

4. 查看幫助信息：
   ```bash
   groupmod --help
   ```

## Tips
- 在更改群組名稱或 GID 之前，建議先確認該名稱或 GID 是否已被其他群組使用。
- 使用 `getent group` 命令可以查詢當前系統中的群組信息，幫助你做出更改前的決策。
- 修改群組屬性後，請檢查相關用戶的權限，以確保不會影響系統的正常運行。