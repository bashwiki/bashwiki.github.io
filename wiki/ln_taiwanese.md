# [Linux] Bash ln 使用法: 創建檔案的連結

## Overview
`ln` 命令用於在 Linux 系統中創建檔案的連結。這些連結可以是硬連結或符號連結，讓使用者能夠在不同的位置訪問同一個檔案。

## Usage
基本的語法如下：
```
ln [options] [arguments]
```

## Common Options
- `-s`: 創建符號連結（symlink），這是一種指向原始檔案的快捷方式。
- `-f`: 強制創建連結，若目標檔案已存在則覆蓋。
- `-n`: 如果目標檔案已存在且是符號連結，則不進行操作。

## Common Examples
1. **創建硬連結**
   ```bash
   ln original.txt link_to_original.txt
   ```
   這將在當前目錄中創建一個名為 `link_to_original.txt` 的硬連結，指向 `original.txt`。

2. **創建符號連結**
   ```bash
   ln -s original.txt symlink_to_original.txt
   ```
   這將創建一個名為 `symlink_to_original.txt` 的符號連結，指向 `original.txt`。

3. **強制創建連結**
   ```bash
   ln -f original.txt existing_link.txt
   ```
   如果 `existing_link.txt` 已存在，這將強制覆蓋它並創建一個新的硬連結。

4. **創建符號連結到目錄**
   ```bash
   ln -s /path/to/directory symlink_to_directory
   ```
   這將創建一個指向指定目錄的符號連結。

## Tips
- 使用符號連結可以節省空間，因為它們不會複製檔案內容。
- 硬連結無法跨不同的檔案系統使用，因此在使用時請注意。
- 當你需要指向一個檔案的多個位置時，符號連結是非常有用的選擇。