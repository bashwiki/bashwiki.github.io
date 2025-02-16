# [Linux] Bash groups 使用方式: 顯示使用者所屬的群組

## Overview
`groups` 命令用來顯示當前使用者或指定使用者所屬的群組。這對於管理使用者權限和了解系統中使用者的群組結構非常有用。

## Usage
基本語法如下：
```
groups [options] [arguments]
```

## Common Options
- `-h`, `--help`: 顯示幫助信息。
- `-v`, `--version`: 顯示版本信息。

## Common Examples
以下是一些常見的使用範例：

1. 顯示當前使用者所屬的群組：
   ```bash
   groups
   ```

2. 顯示指定使用者（例如 `username`）所屬的群組：
   ```bash
   groups username
   ```

3. 使用 `--help` 選項查看幫助信息：
   ```bash
   groups --help
   ```

4. 使用 `--version` 選項查看版本信息：
   ```bash
   groups --version
   ```

## Tips
- 當你需要檢查某個使用者的群組時，使用 `groups username` 是非常方便的。
- 了解使用者所屬的群組可以幫助你更好地管理系統的安全性和權限。
- 如果你在多用戶環境中工作，定期檢查群組成員可以幫助你保持系統的整潔。