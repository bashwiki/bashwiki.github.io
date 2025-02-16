# [台灣] Bash rmdir 使用方式: 刪除空目錄

## Overview
`rmdir` 命令用於刪除空的目錄。如果目錄中有檔案或其他目錄，則無法使用此命令刪除。

## Usage
基本語法如下：
```
rmdir [選項] [參數]
```

## Common Options
- `-p`：刪除目錄及其父目錄（如果它們也是空的）。
- `--ignore-fail-on-non-empty`：忽略非空目錄的錯誤，不會顯示錯誤訊息。

## Common Examples
1. 刪除一個空目錄：
   ```bash
   rmdir my_empty_directory
   ```

2. 刪除多個空目錄：
   ```bash
   rmdir dir1 dir2 dir3
   ```

3. 使用 `-p` 選項刪除父目錄：
   ```bash
   rmdir -p parent_directory/child_directory
   ```

4. 忽略非空目錄的錯誤：
   ```bash
   rmdir --ignore-fail-on-non-empty non_empty_directory
   ```

## Tips
- 確保目錄是空的，否則 `rmdir` 會報錯。
- 使用 `-p` 選項時要小心，因為它會刪除父目錄，可能會影響其他檔案結構。
- 在刪除目錄之前，可以使用 `ls` 命令檢查目錄內容。