# [Linux] Bash blkid 用法: 查詢磁碟分割區的 UUID 和檔案系統類型

## Overview
`blkid` 是一個用於查詢和顯示磁碟分割區的 UUID（通用唯一識別碼）和檔案系統類型的命令。這個工具對於管理磁碟和檔案系統非常有用，特別是在需要識別和配置磁碟分割區時。

## Usage
基本語法如下：
```
blkid [options] [arguments]
```

## Common Options
- `-o, --output <type>`: 指定輸出格式，例如 `value` 或 `full`。
- `-s, --match-tag <tag>`: 僅顯示指定標籤的資訊。
- `-p, --probe`: 強制檢查設備，即使它已經被標記為已知。
- `-c, --cache <file>`: 使用指定的快取檔案。

## Common Examples
1. **查詢所有分割區的 UUID 和檔案系統類型**：
   ```bash
   blkid
   ```

2. **查詢特定分割區的資訊**：
   ```bash
   blkid /dev/sda1
   ```

3. **以特定格式輸出 UUID**：
   ```bash
   blkid -o value -s UUID /dev/sda1
   ```

4. **顯示特定標籤的資訊**：
   ```bash
   blkid -s TYPE /dev/sda1
   ```

## Tips
- 使用 `blkid` 時，確保你有適當的權限來訪問磁碟設備，通常需要以 root 身份執行。
- 可以將 `blkid` 的輸出結果重定向到檔案中，以便後續查閱：
  ```bash
  blkid > blkid_output.txt
  ```
- 若要快速查詢特定分割區的 UUID，使用 `-o value -s UUID` 會更為方便。