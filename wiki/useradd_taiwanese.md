# [Linux] Bash useradd 使用法: 新增使用者帳號

## Overview
`useradd` 命令用於在 Linux 系統中新增使用者帳號。這個命令可以設定使用者的基本資訊，例如使用者名稱、密碼、家目錄等。

## Usage
基本語法如下：
```bash
useradd [選項] [參數]
```

## Common Options
- `-m`：自動建立使用者的家目錄。
- `-s`：指定使用者的預設 shell。
- `-c`：添加使用者的描述資訊。
- `-G`：指定使用者所屬的附加群組。
- `-d`：指定使用者的家目錄路徑。

## Common Examples
以下是一些常見的使用範例：

1. 新增一個基本的使用者帳號：
   ```bash
   useradd newuser
   ```

2. 新增一個使用者並建立家目錄：
   ```bash
   useradd -m newuser
   ```

3. 新增一個使用者並指定預設 shell：
   ```bash
   useradd -s /bin/bash newuser
   ```

4. 新增一個使用者並添加描述：
   ```bash
   useradd -c "新使用者" newuser
   ```

5. 新增一個使用者並指定附加群組：
   ```bash
   useradd -G sudo newuser
   ```

## Tips
- 在使用 `useradd` 之後，通常需要使用 `passwd` 命令來設定使用者的密碼。
- 確保在新增使用者時，使用者名稱是唯一的，避免與現有帳號衝突。
- 使用 `-d` 選項時，確保指定的家目錄路徑是有效的，否則可能會導致問題。