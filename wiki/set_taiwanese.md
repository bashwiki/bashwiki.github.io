# [Linux] Bash set 使用法: 設定Shell環境變數

## Overview
`set` 命令用於設定或顯示Shell的環境變數及選項。它可以幫助用戶調整Shell的行為，並控制腳本的執行方式。

## Usage
基本語法如下：
```
set [options] [arguments]
```

## Common Options
- `-e`：當命令執行失敗時，立即退出Shell。
- `-u`：當使用未設定的變數時，報錯並退出。
- `-x`：顯示執行的每個命令，方便除錯。
- `+o`：用於關閉某些選項，例如 `+o noclobber` 可以關閉防止覆蓋檔案的選項。

## Common Examples
1. **顯示所有環境變數**
   ```bash
   set
   ```

2. **啟用錯誤退出選項**
   ```bash
   set -e
   ```

3. **啟用未設定變數報錯**
   ```bash
   set -u
   ```

4. **顯示執行命令的詳細資訊**
   ```bash
   set -x
   ```

5. **關閉防止覆蓋檔案的選項**
   ```bash
   set +o noclobber
   ```

## Tips
- 在編寫腳本時，建議使用 `set -e` 和 `set -u` 來提高腳本的穩定性。
- 使用 `set -x` 來進行除錯，可以幫助你了解腳本的執行流程。
- 在使用 `set` 命令後，記得檢查變數的設定，以確保它們符合預期的行為。