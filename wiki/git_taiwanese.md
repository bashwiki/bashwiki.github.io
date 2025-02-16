# [台灣] Bash git 使用方法: 版本控制工具

## Overview
`git` 是一個分散式版本控制系統，主要用於追蹤檔案的變更，協助多個使用者協作開發。它能夠有效地管理專案的歷史紀錄，並支援分支和合併等功能。

## Usage
基本語法如下：
```
git [options] [arguments]
```

## Common Options
- `git init`：初始化一個新的 Git 倉庫。
- `git clone <repository>`：從遠端倉庫複製一個本地副本。
- `git add <file>`：將檔案變更加入暫存區。
- `git commit -m "<message>"`：提交暫存區的變更並附上說明。
- `git push`：將本地提交推送到遠端倉庫。
- `git pull`：從遠端倉庫獲取並合併變更。

## Common Examples
以下是一些常見的 `git` 使用範例：

1. 初始化新的 Git 倉庫：
   ```bash
   git init my_project
   ```

2. 從遠端倉庫複製專案：
   ```bash
   git clone https://github.com/user/repo.git
   ```

3. 將檔案變更加入暫存區：
   ```bash
   git add README.md
   ```

4. 提交變更：
   ```bash
   git commit -m "新增 README 檔案"
   ```

5. 推送變更到遠端倉庫：
   ```bash
   git push origin main
   ```

6. 獲取並合併遠端變更：
   ```bash
   git pull origin main
   ```

## Tips
- 在提交前，使用 `git status` 檢查當前的檔案狀態。
- 經常使用 `git log` 來查看提交歷史，了解專案的變更紀錄。
- 使用分支來管理不同的功能開發，這樣可以保持主分支的穩定性。