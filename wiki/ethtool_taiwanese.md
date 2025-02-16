# [Linux] Bash ethtool 使用法: 網路介面卡設定與查詢

## Overview
`ethtool` 是一個用於查詢和設定網路介面卡（NIC）參數的命令行工具。它可以顯示網路設備的狀態、速度、雙工模式等資訊，並允許用戶調整一些設定。

## Usage
基本語法如下：
```
ethtool [options] [arguments]
```

## Common Options
- `-s` : 設定網路介面卡的參數。
- `-i` : 顯示網路介面卡的驅動程式資訊。
- `-p` : 使指定的網路介面卡閃爍，以便識別。
- `-d` : 顯示網路介面卡的診斷資訊。
- `-S` : 顯示網路介面卡的統計資訊。

## Common Examples
1. 查詢網路介面卡的基本資訊：
   ```bash
   ethtool eth0
   ```

2. 顯示網路介面卡的驅動程式資訊：
   ```bash
   ethtool -i eth0
   ```

3. 設定網路介面卡的速度和雙工模式：
   ```bash
   ethtool -s eth0 speed 100 duplex full
   ```

4. 使網路介面卡閃爍以便識別：
   ```bash
   ethtool -p eth0
   ```

5. 顯示網路介面卡的統計資訊：
   ```bash
   ethtool -S eth0
   ```

## Tips
- 在使用 `ethtool` 之前，確保你有足夠的權限（通常需要 root 權限）。
- 使用 `man ethtool` 可以查看完整的手冊頁，了解更多選項和功能。
- 當調整網路介面卡的設定時，請小心操作，以免影響網路連接。