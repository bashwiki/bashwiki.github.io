# [台灣] Bash mkfifo 使用法: 創建命名管道

## Overview
`mkfifo` 命令用於創建一個命名管道（FIFO），這是一種特殊的文件類型，允許進程之間進行通信。命名管道可以在不同的進程之間傳遞數據，這使得它在多任務處理和數據流傳輸中非常有用。

## Usage
基本語法如下：
```bash
mkfifo [選項] [參數]
```

## Common Options
- `-m, --mode=MODE`：設置新創建的管道的權限模式。
- `--help`：顯示幫助信息。
- `--version`：顯示版本信息。

## Common Examples
以下是一些常見的使用範例：

### 創建一個基本的命名管道
```bash
mkfifo mypipe
```

### 創建一個具有特定權限的命名管道
```bash
mkfifo -m 644 mypipe
```

### 在一個終端中寫入數據到命名管道
```bash
echo "Hello, World!" > mypipe
```

### 在另一個終端中讀取命名管道中的數據
```bash
cat mypipe
```

## Tips
- 在使用命名管道時，確保有一個進程在讀取數據，否則寫入操作會被阻塞。
- 可以使用 `rm mypipe` 刪除不再需要的命名管道。
- 命名管道的權限設置可以影響其他用戶的訪問權限，請根據需要設置適當的權限。