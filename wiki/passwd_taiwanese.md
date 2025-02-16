# [Linux] Bash passwd 用法: 更改使用者密碼

## Overview
`passwd` 命令用於更改使用者的密碼。這個命令可以讓使用者更新自己的密碼，或者由管理員為其他使用者設定密碼。

## Usage
基本語法如下：
```bash
passwd [選項] [使用者名稱]
```

## Common Options
- `-d`：刪除使用者的密碼，讓使用者無需密碼登入。
- `-e`：立即過期使用者的密碼，強制使用者在下次登入時更改密碼。
- `-l`：鎖定使用者帳號，禁止登入。
- `-u`：解鎖使用者帳號，允許登入。

## Common Examples
1. 更改當前使用者的密碼：
   ```bash
   passwd
   ```

2. 更改指定使用者的密碼（需要管理員權限）：
   ```bash
   sudo passwd username
   ```

3. 刪除使用者的密碼：
   ```bash
   sudo passwd -d username
   ```

4. 鎖定使用者帳號：
   ```bash
   sudo passwd -l username
   ```

5. 解鎖使用者帳號：
   ```bash
   sudo passwd -u username
   ```

## Tips
- 在設定新密碼時，請確保密碼強度足夠，包含大小寫字母、數字及特殊符號。
- 定期更改密碼以增強安全性。
- 使用 `passwd -e username` 來強制使用者在下次登入時更改密碼，這對於管理員來說是一個很好的安全措施。