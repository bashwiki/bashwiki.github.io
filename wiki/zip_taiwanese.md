# [台灣] Bash zip 使用法: 壓縮檔案

## Overview
`zip` 命令用於將一個或多個檔案壓縮成一個 ZIP 檔案，這樣可以節省磁碟空間並方便檔案傳輸。

## Usage
基本語法如下：
```bash
zip [options] [arguments]
```

## Common Options
- `-r`：遞迴壓縮目錄及其內容。
- `-e`：加密壓縮檔案。
- `-9`：使用最佳壓縮率。
- `-u`：更新已存在的 ZIP 檔案中的檔案。

## Common Examples
- 壓縮單個檔案：
  ```bash
  zip myarchive.zip file1.txt
  ```

- 壓縮多個檔案：
  ```bash
  zip myarchive.zip file1.txt file2.txt file3.txt
  ```

- 遞迴壓縮目錄：
  ```bash
  zip -r myarchive.zip myfolder/
  ```

- 加密壓縮檔案：
  ```bash
  zip -e myarchive.zip file1.txt
  ```

- 更新已存在的 ZIP 檔案：
  ```bash
  zip -u myarchive.zip file2.txt
  ```

## Tips
- 使用 `-9` 選項可以獲得最佳壓縮效果，但可能會增加壓縮時間。
- 定期更新 ZIP 檔案中的內容，使用 `-u` 選項可以避免重複壓縮相同的檔案。
- 為了安全起見，使用 `-e` 選項加密重要檔案。