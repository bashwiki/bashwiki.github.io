# [Linux] Bash id 使用法: 查詢使用者識別資訊

## Overview
`id` 命令用於顯示當前使用者或指定使用者的用戶識別資訊，包括用戶 ID (UID)、群組 ID (GID) 以及所屬的群組。

## Usage
基本語法如下：
```
id [選項] [使用者]
```

## Common Options
- `-u`：顯示用戶的 UID。
- `-g`：顯示主群組的 GID。
- `-G`：顯示所有群組的 GID。
- `-n`：顯示名稱而不是數字 ID。
- `-r`：顯示實際的 UID 或 GID，而不是有效的。

## Common Examples
1. 顯示當前使用者的所有識別資訊：
   ```bash
   id
   ```

2. 顯示指定使用者的 UID 和 GID：
   ```bash
   id username
   ```

3. 只顯示當前使用者的 UID：
   ```bash
   id -u
   ```

4. 顯示當前使用者的主群組 GID：
   ```bash
   id -g
   ```

5. 顯示當前使用者所屬的所有群組 GID：
   ```bash
   id -G
   ```

6. 顯示指定使用者的名稱和 UID：
   ```bash
   id -n username
   ```

## Tips
- 使用 `id` 命令可以快速檢查用戶的權限和群組設定，特別是在進行系統管理時。
- 結合其他命令使用，例如 `grep`，可以過濾出特定的群組資訊。
- 確保在使用 `id` 命令時擁有適當的權限，以便查詢其他使用者的資訊。