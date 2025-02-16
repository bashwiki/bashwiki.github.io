# [Linux] Bash mv 使用方法: 移動或重新命名檔案

## Overview
`mv` 命令用於移動檔案或目錄，或是重新命名它們。這個命令是 Linux 和其他 Unix-like 系統中非常基本且常用的工具。

## Usage
基本語法如下：
```bash
mv [options] [source] [destination]
```

## Common Options
- `-i`: 在覆蓋檔案之前提示使用者確認。
- `-u`: 只在源檔案比目標檔案新時才進行移動。
- `-v`: 顯示詳細的操作過程，讓使用者知道正在發生什麼。

## Common Examples
1. **移動檔案**
   ```bash
   mv file.txt /path/to/destination/
   ```
   這會將 `file.txt` 移動到指定的目的地目錄。

2. **重新命名檔案**
   ```bash
   mv oldname.txt newname.txt
   ```
   這會將 `oldname.txt` 重新命名為 `newname.txt`。

3. **使用提示選項**
   ```bash
   mv -i file.txt /path/to/destination/
   ```
   如果目的地已經有同名檔案，這個命令會提示使用者確認是否要覆蓋。

4. **更新檔案**
   ```bash
   mv -u file.txt /path/to/destination/
   ```
   這會將 `file.txt` 移動到目的地，但只有當 `file.txt` 比目的地的同名檔案更新時才會進行。

5. **顯示詳細過程**
   ```bash
   mv -v file.txt /path/to/destination/
   ```
   這會在移動檔案的過程中顯示詳細信息。

## Tips
- 在使用 `mv` 命令時，建議使用 `-i` 選項來避免意外覆蓋重要檔案。
- 確保在執行命令之前檢查檔案和目錄的路徑，以避免錯誤。
- 使用 `-v` 選項可以幫助你追蹤檔案的移動過程，特別是在處理大量檔案時。