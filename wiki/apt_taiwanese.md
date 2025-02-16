# [Linux] Bash apt 使用法: 管理軟體包的工具

## Overview
`apt` 是一個用於 Debian 和 Ubuntu 系統的命令行工具，主要用來管理軟體包。它可以用來安裝、更新和移除軟體包，讓使用者輕鬆地管理系統中的應用程式。

## Usage
基本語法如下：
```
apt [options] [arguments]
```

## Common Options
- `install`：安裝指定的軟體包。
- `remove`：移除指定的軟體包。
- `update`：更新可用軟體包的列表。
- `upgrade`：升級已安裝的所有軟體包。
- `search`：搜尋可用的軟體包。

## Common Examples
- 安裝軟體包：
  ```bash
  sudo apt install package-name
  ```
- 移除軟體包：
  ```bash
  sudo apt remove package-name
  ```
- 更新可用軟體包列表：
  ```bash
  sudo apt update
  ```
- 升級所有已安裝的軟體包：
  ```bash
  sudo apt upgrade
  ```
- 搜尋軟體包：
  ```bash
  apt search package-name
  ```

## Tips
- 在執行 `install` 或 `remove` 命令時，建議使用 `sudo` 以獲得管理員權限。
- 定期執行 `apt update` 和 `apt upgrade` 以保持系統的安全性和穩定性。
- 使用 `apt list --upgradable` 可以查看哪些軟體包可以升級。