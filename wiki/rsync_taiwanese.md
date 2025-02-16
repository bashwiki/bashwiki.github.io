# [Linux] Bash rsync 使用法: 檔案同步與備份工具

## Overview
`rsync` 是一個用於檔案和目錄之間同步的工具，常用於備份和鏡像。它能夠高效地傳輸和同步檔案，僅傳輸變更的部分，從而節省帶寬和時間。

## Usage
基本語法如下：
```bash
rsync [options] [source] [destination]
```

## Common Options
- `-a`: 以歸檔模式傳輸，保留檔案的所有屬性。
- `-v`: 顯示詳細的傳輸過程。
- `-z`: 在傳輸過程中進行壓縮。
- `-r`: 遞迴進入子目錄。
- `--delete`: 刪除目標中在來源中不存在的檔案。

## Common Examples
1. **基本檔案同步**
   ```bash
   rsync -av /path/to/source/ /path/to/destination/
   ```

2. **壓縮傳輸**
   ```bash
   rsync -az /path/to/source/ user@remote:/path/to/destination/
   ```

3. **遞迴同步整個目錄**
   ```bash
   rsync -ar /path/to/source/ /path/to/destination/
   ```

4. **刪除目標中不存在的檔案**
   ```bash
   rsync -av --delete /path/to/source/ /path/to/destination/
   ```

5. **顯示詳細資訊的同步**
   ```bash
   rsync -av --progress /path/to/source/ /path/to/destination/
   ```

## Tips
- 在使用 `rsync` 時，建議先使用 `-n` 或 `--dry-run` 選項進行測試，這樣可以預覽將要執行的操作而不實際執行。
- 確保來源和目標路徑的結尾有斜線 `/`，這樣可以確保正確同步內容。
- 使用 `-z` 選項在網路速度較慢的情況下可以加快檔案傳輸速度。