# [Linux] Bash last 使用法: 顯示登入紀錄

## Overview
`last` 命令用於顯示系統的登入紀錄，包括用戶名、登入時間和登出時間。這個命令可以幫助系統管理員追蹤用戶活動和檢查安全性。

## Usage
基本語法如下：
```
last [options] [arguments]
```

## Common Options
- `-a`: 顯示登入的主機名稱。
- `-n [number]`: 限制顯示的紀錄數量。
- `-R`: 不顯示主機名稱。
- `-x`: 顯示系統關機和重啟的紀錄。

## Common Examples
1. 顯示所有登入紀錄：
   ```bash
   last
   ```

2. 限制顯示最近的 5 條紀錄：
   ```bash
   last -n 5
   ```

3. 顯示登入的主機名稱：
   ```bash
   last -a
   ```

4. 顯示系統關機和重啟的紀錄：
   ```bash
   last -x
   ```

## Tips
- 使用 `last` 命令可以幫助你檢查是否有未經授權的登入。
- 定期檢查登入紀錄有助於維護系統安全。
- 結合 `grep` 命令可以更方便地查找特定用戶的登入紀錄，例如：
  ```bash
  last | grep username
  ```