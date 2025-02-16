# [Linux] Bash rpm 使用法: 管理 RPM 套件

## Overview
`rpm` 是一個用於管理 RPM 套件的命令行工具。它可以用來安裝、卸載、查詢和驗證 RPM 套件，這些套件通常用於 Red Hat 和其他 Linux 發行版。

## Usage
基本語法如下：
```
rpm [options] [arguments]
```

## Common Options
- `-i`：安裝一個新的 RPM 套件。
- `-e`：卸載已安裝的 RPM 套件。
- `-q`：查詢已安裝的 RPM 套件。
- `-v`：顯示詳細的輸出。
- `-h`：在安裝過程中顯示進度條。

## Common Examples
安裝一個 RPM 套件：
```bash
rpm -i package.rpm
```

卸載一個已安裝的 RPM 套件：
```bash
rpm -e package_name
```

查詢已安裝的 RPM 套件：
```bash
rpm -q package_name
```

顯示已安裝套件的詳細資訊：
```bash
rpm -qi package_name
```

驗證已安裝的 RPM 套件：
```bash
rpm -V package_name
```

## Tips
- 在安裝或卸載套件之前，建議使用 `-q` 來確認該套件是否已經存在。
- 使用 `-v` 和 `-h` 參數可以讓你在安裝過程中獲得更清晰的進度顯示。
- 當遇到依賴問題時，可以考慮使用 `yum` 或 `dnf` 這類工具來自動處理依賴關係。