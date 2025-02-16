# [Linux] Bash lsusb 使用方法: 列出 USB 裝置資訊

## Overview
`lsusb` 是一個用於列出系統中所有 USB 裝置的命令。它能夠顯示每個 USB 裝置的詳細資訊，包括製造商、產品 ID 和版本等。

## Usage
基本語法如下：
```bash
lsusb [options] [arguments]
```

## Common Options
- `-v`: 顯示詳細資訊，包括所有可用的 USB 裝置屬性。
- `-t`: 以樹狀結構顯示 USB 裝置的層級。
- `-s <bus>:<device>`: 指定要顯示的特定 USB 裝置，使用總線和裝置編號。
- `-d <vendor>:<product>`: 只顯示指定廠商和產品的 USB 裝置。

## Common Examples
1. 列出所有 USB 裝置：
   ```bash
   lsusb
   ```

2. 顯示詳細的 USB 裝置資訊：
   ```bash
   lsusb -v
   ```

3. 以樹狀結構顯示 USB 裝置：
   ```bash
   lsusb -t
   ```

4. 顯示特定 USB 裝置的資訊（例如，總線 001，裝置 002）：
   ```bash
   lsusb -s 001:002
   ```

5. 顯示特定廠商和產品的 USB 裝置（例如，廠商 ID 為 1234，產品 ID 為 5678）：
   ```bash
   lsusb -d 1234:5678
   ```

## Tips
- 在使用 `-v` 選項時，輸出可能會非常詳細，可以使用管道將結果傳送到 `less` 以便於閱讀：
  ```bash
  lsusb -v | less
  ```
- 若要獲取 USB 裝置的即時資訊，考慮與 `dmesg` 命令結合使用，以查看最近的系統訊息。
- 定期檢查 USB 裝置的連接狀態，特別是在進行硬體故障排除時，`lsusb` 是一個非常有用的工具。