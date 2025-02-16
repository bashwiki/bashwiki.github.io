# [Linux] Bash wget 使用法: 下載檔案的工具

## Overview
`wget` 是一個用於從網路上下載檔案的命令行工具。它支援 HTTP、HTTPS 和 FTP 協議，並且可以在不需要使用者介入的情況下進行下載。

## Usage
基本語法如下：
```
wget [選項] [網址]
```

## Common Options
- `-O <檔名>`: 指定下載後的檔案名稱。
- `-c`: 繼續未完成的下載。
- `-q`: 靜默模式，不顯示下載過程。
- `--limit-rate=<速率>`: 限制下載速度。
- `-r`: 遞迴下載，適合下載整個網站。

## Common Examples
以下是一些常見的使用範例：

1. 下載單一檔案：
   ```bash
   wget https://example.com/file.zip
   ```

2. 指定檔案名稱：
   ```bash
   wget -O myfile.zip https://example.com/file.zip
   ```

3. 繼續未完成的下載：
   ```bash
   wget -c https://example.com/largefile.zip
   ```

4. 限制下載速度：
   ```bash
   wget --limit-rate=200k https://example.com/file.zip
   ```

5. 遞迴下載整個網站：
   ```bash
   wget -r https://example.com/
   ```

## Tips
- 使用 `-q` 選項可以讓你在腳本中使用 wget 時不顯示任何輸出，讓輸出更整潔。
- 當下載大檔案時，使用 `-c` 選項可以避免重新下載已經下載的部分，節省時間和帶寬。
- 如果需要下載多個檔案，可以將網址放在一個文本檔中，然後使用 `-i` 選項來批量下載：
   ```bash
   wget -i urls.txt
   ```