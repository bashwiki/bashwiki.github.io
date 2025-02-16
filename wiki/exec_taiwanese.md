# [Linux] Bash exec 使用法: 執行命令並替換當前進程

## Overview
`exec` 命令用於在當前的 shell 環境中執行指定的命令，並用該命令替換當前的 shell 進程。這意味著當命令執行完畢後，原本的 shell 將不再存在。

## Usage
基本語法如下：
```bash
exec [options] [arguments]
```

## Common Options
- `-a name`: 指定執行命令時的名稱。
- `-l`: 使命令以 login shell 的方式執行。
- `-p`: 以受限的方式執行命令，避免環境變數的影響。

## Common Examples
1. **替換當前 shell 為新的命令**
   ```bash
   exec /bin/bash
   ```
   這會用新的 bash shell 替換當前的 shell。

2. **執行一個腳本並替換當前 shell**
   ```bash
   exec ./myscript.sh
   ```
   這會執行 `myscript.sh`，並替換當前的 shell 進程。

3. **以特定名稱執行命令**
   ```bash
   exec -a mycustomname /usr/bin/python3
   ```
   這會將 Python 解釋器的名稱設置為 `mycustomname`。

4. **以 login shell 方式執行命令**
   ```bash
   exec -l /bin/zsh
   ```
   這會以 login shell 的方式啟動 zsh。

## Tips
- 使用 `exec` 時，請注意這會終止當前的 shell 進程，因此在執行之前確保不需要返回到原本的 shell。
- `exec` 常用於腳本中，以提高效率，因為它不會創建新的進程。
- 如果需要保留當前 shell，考慮使用其他命令而不是 `exec`。