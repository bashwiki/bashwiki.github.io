# [台灣] Bash svn 使用方式: 版本控制工具

## Overview
`svn`（Subversion）是一個版本控制系統，用於管理檔案和目錄的變更，並能夠協助多位使用者協作開發。它可以追蹤檔案的歷史紀錄，讓使用者能夠隨時回溯到先前的版本。

## Usage
基本語法如下：
```bash
svn [options] [arguments]
```

## Common Options
- `checkout`: 從版本庫檢出檔案。
- `commit`: 提交變更到版本庫。
- `update`: 更新本地工作副本以反映版本庫中的最新變更。
- `add`: 將新檔案或目錄加入版本控制。
- `delete`: 刪除版本控制中的檔案或目錄。
- `status`: 顯示工作副本的狀態。

## Common Examples
- 檢出版本庫：
  ```bash
  svn checkout https://example.com/svn/myproject
  ```

- 提交變更：
  ```bash
  svn commit -m "更新了README檔案"
  ```

- 更新工作副本：
  ```bash
  svn update
  ```

- 新增檔案到版本控制：
  ```bash
  svn add newfile.txt
  ```

- 刪除檔案：
  ```bash
  svn delete oldfile.txt
  ```

- 查看工作副本狀態：
  ```bash
  svn status
  ```

## Tips
- 在提交變更之前，使用 `svn status` 檢查工作副本的狀態，以避免意外提交不必要的檔案。
- 使用 `svn log` 可以查看版本歷史紀錄，了解過去的變更。
- 定期更新工作副本，以確保與版本庫的同步，避免合併衝突。