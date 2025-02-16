# [Linux] Bash yum 使用方法: 管理軟體包

## Overview
`yum` 是一個用於在基於 RPM 的 Linux 發行版上管理軟體包的命令行工具。它可以用來安裝、更新和移除軟體包，並能自動處理依賴關係，確保系統的穩定性和完整性。

## Usage
基本語法如下：
```bash
yum [options] [arguments]
```

## Common Options
- `install`：安裝指定的軟體包。
- `remove`：移除指定的軟體包。
- `update`：更新已安裝的軟體包到最新版本。
- `list`：列出可用或已安裝的軟體包。
- `search`：搜尋指定的軟體包。
- `info`：顯示指定軟體包的詳細資訊。

## Common Examples
- 安裝一個軟體包：
  ```bash
  yum install httpd
  ```
  
- 移除一個軟體包：
  ```bash
  yum remove httpd
  ```

- 更新所有已安裝的軟體包：
  ```bash
  yum update
  ```

- 列出所有可用的軟體包：
  ```bash
  yum list available
  ```

- 搜尋特定的軟體包：
  ```bash
  yum search nginx
  ```

- 顯示特定軟體包的資訊：
  ```bash
  yum info httpd
  ```

## Tips
- 在執行更新或安裝之前，建議先執行 `yum check-update` 來檢查可用的更新。
- 使用 `yum clean all` 來清理快取，釋放磁碟空間。
- 定期更新系統以確保安全性和穩定性。