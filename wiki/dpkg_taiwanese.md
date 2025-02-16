# [Linux] Bash dpkg 使用方法: 管理 Debian 套件

## Overview
`dpkg` 是一個用於管理 Debian 和 Ubuntu 系統上軟體包的命令行工具。它可以安裝、移除和管理已安裝的軟體包，並且能夠查詢系統中已安裝的軟體包資訊。

## Usage
基本語法如下：
```
dpkg [options] [arguments]
```

## Common Options
- `-i`：安裝指定的 `.deb` 套件檔案。
- `-r`：移除指定的已安裝套件。
- `-l`：列出所有已安裝的套件。
- `-s`：顯示指定套件的狀態資訊。
- `-L`：列出指定套件安裝的所有檔案。

## Common Examples
- 安裝一個 `.deb` 套件：
  ```bash
  dpkg -i package.deb
  ```

- 移除一個已安裝的套件：
  ```bash
  dpkg -r package_name
  ```

- 列出所有已安裝的套件：
  ```bash
  dpkg -l
  ```

- 查詢某個套件的狀態：
  ```bash
  dpkg -s package_name
  ```

- 列出某個套件安裝的所有檔案：
  ```bash
  dpkg -L package_name
  ```

## Tips
- 在安裝套件之前，建議先使用 `apt-get update` 更新套件清單，以確保安裝的版本是最新的。
- 使用 `dpkg` 安裝套件時，若有依賴問題，建議使用 `apt-get install -f` 來修復依賴。
- 定期使用 `dpkg -l` 檢查系統中已安裝的套件，以保持系統的整潔。