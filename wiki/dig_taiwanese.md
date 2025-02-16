# [Linux] Bash dig 使用法: 查詢 DNS 記錄

## Overview
`dig` 是一個用於查詢 DNS（域名系統）記錄的命令行工具。它可以幫助用戶獲取有關域名的詳細資訊，例如 A 記錄、MX 記錄和 NS 記錄等。

## Usage
基本語法如下：

```
dig [選項] [參數]
```

## Common Options
- `@server`：指定要查詢的 DNS 伺服器。
- `-t type`：指定查詢的記錄類型（例如 A、MX、CNAME 等）。
- `+short`：簡化輸出，只顯示結果。
- `+trace`：跟蹤查詢過程，顯示每一步的查詢結果。

## Common Examples
查詢某個域名的 A 記錄：
```bash
dig example.com
```

查詢特定 DNS 伺服器的 A 記錄：
```bash
dig @8.8.8.8 example.com
```

查詢 MX 記錄：
```bash
dig example.com -t MX
```

使用簡化輸出：
```bash
dig example.com +short
```

跟蹤查詢過程：
```bash
dig example.com +trace
```

## Tips
- 使用 `+short` 可以快速獲取結果，特別是在查詢時只需要最基本的資訊。
- 當遇到 DNS 問題時，使用 `+trace` 可以幫助你了解查詢的每一步，方便排除故障。
- 嘗試不同的 DNS 伺服器（如 Google 的 8.8.8.8 或 Cloudflare 的 1.1.1.1）來獲取更準確的結果。