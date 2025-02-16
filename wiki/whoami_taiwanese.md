# [Linux] Bash whoami 使用法: 獲取當前用戶名稱

## Overview
`whoami` 命令用來顯示當前登入系統的用戶名稱。這個命令非常有用，尤其是在多用戶環境中，幫助用戶確認自己當前的身份。

## Usage
基本語法如下：
```
whoami [options] [arguments]
```

## Common Options
- `--help`：顯示幫助信息。
- `--version`：顯示版本信息。

## Common Examples
以下是一些常見的使用範例：

1. 簡單顯示當前用戶名稱：
   ```bash
   whoami
   ```

2. 顯示幫助信息：
   ```bash
   whoami --help
   ```

3. 顯示版本信息：
   ```bash
   whoami --version
   ```

## Tips
- 在需要確認當前用戶身份的腳本中使用 `whoami`，可以避免權限問題。
- 結合其他命令使用，例如在檢查用戶權限時，可以使用 `whoami` 來獲取用戶名稱並進行比較。