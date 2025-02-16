# [Linux] Bash mkdir 使用方式: 創建目錄

## Overview
`mkdir` 命令用於在檔案系統中創建新目錄。這是一個基本的命令，常用於組織檔案和資料夾結構。

## Usage
基本語法如下：
```bash
mkdir [options] [arguments]
```

## Common Options
- `-p`：同時創建多層目錄，若上層目錄不存在，則會自動創建。
- `-v`：在創建目錄時顯示詳細信息。
- `-m`：設定新目錄的權限模式。

## Common Examples
1. 創建單一目錄：
   ```bash
   mkdir myfolder
   ```

2. 創建多層目錄：
   ```bash
   mkdir -p parent/child/grandchild
   ```

3. 創建目錄並顯示詳細信息：
   ```bash
   mkdir -v newfolder
   ```

4. 創建目錄並設定權限：
   ```bash
   mkdir -m 755 mysecurefolder
   ```

## Tips
- 使用 `-p` 選項可以避免因為上層目錄不存在而導致的錯誤。
- 在創建目錄時，考慮使用有意義的名稱，以便於未來的檔案管理。
- 定期檢查和清理不再需要的目錄，以保持檔案系統的整潔。