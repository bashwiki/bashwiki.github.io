# [Linux] Bash userdel 使用法: 刪除使用者帳號

## Overview
`userdel` 命令用來刪除系統中的使用者帳號。這個命令可以移除使用者的帳號及其相關的檔案，確保系統的安全性和整潔性。

## Usage
基本語法如下：
```
userdel [選項] [使用者名稱]
```

## Common Options
- `-r`：同時刪除使用者的主目錄及其內容。
- `-f`：強制刪除使用者，即使使用者目前已登入。
- `-h`：顯示幫助資訊。

## Common Examples
1. 刪除一個使用者帳號：
   ```bash
   userdel username
   ```

2. 刪除使用者帳號及其主目錄：
   ```bash
   userdel -r username
   ```

3. 強制刪除正在登入的使用者帳號：
   ```bash
   userdel -f username
   ```

4. 顯示幫助資訊：
   ```bash
   userdel -h
   ```

## Tips
- 在刪除使用者之前，建議先備份重要資料。
- 使用 `-r` 選項時要小心，因為這會永久刪除使用者的所有檔案。
- 確保你有足夠的權限來執行 `userdel` 命令，通常需要以 root 身份執行。