# [台灣] Bash uuidgen 使用方式: 生成唯一識別碼

## Overview
`uuidgen` 是一個用於生成通用唯一識別碼（UUID）的命令行工具。UUID 是一種標準的識別碼格式，通常用於標識資料庫中的記錄或其他需要唯一標識的對象。

## Usage
基本語法如下：
```
uuidgen [options] [arguments]
```

## Common Options
- `-r`：生成隨機 UUID。
- `-t`：生成時間戳 UUID。
- `-h`：顯示幫助信息。

## Common Examples
生成一個隨機 UUID：
```bash
uuidgen -r
```

生成一個時間戳 UUID：
```bash
uuidgen -t
```

生成多個 UUID（例如，生成 5 個）：
```bash
for i in {1..5}; do uuidgen; done
```

## Tips
- 使用 `uuidgen` 生成的 UUID 是非常適合用於資料庫主鍵的，因為它們幾乎不會重複。
- 在需要大量唯一識別碼的情況下，可以考慮使用迴圈來批量生成 UUID。
- 確保在需要唯一性和安全性的場合使用 UUID，特別是在分佈式系統中。