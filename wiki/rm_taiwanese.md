# [台灣] Bash rm 使用方式: 刪除檔案或目錄

## Overview
`rm` 命令用於刪除檔案或目錄。這是一個強大的工具，使用時需謹慎，因為刪除的檔案無法輕易恢復。

## Usage
基本語法如下：
```
rm [options] [arguments]
```

## Common Options
- `-f`：強制刪除，不會顯示提示。
- `-i`：在刪除每個檔案之前顯示提示，要求確認。
- `-r`：遞迴刪除目錄及其內容。
- `-v`：顯示刪除的檔案名稱。

## Common Examples
- 刪除單個檔案：
  ```bash
  rm file.txt
  ```

- 強制刪除檔案，不顯示提示：
  ```bash
  rm -f file.txt
  ```

- 刪除目錄及其所有內容：
  ```bash
  rm -r directory_name
  ```

- 在刪除檔案之前要求確認：
  ```bash
  rm -i file.txt
  ```

- 刪除多個檔案：
  ```bash
  rm file1.txt file2.txt file3.txt
  ```

## Tips
- 在使用 `rm` 命令之前，建議先使用 `ls` 確認要刪除的檔案或目錄。
- 使用 `-i` 選項可以避免意外刪除重要檔案。
- 考慮使用 `trash-cli` 工具來代替 `rm`，這樣可以將檔案移至回收站，而不是永久刪除。