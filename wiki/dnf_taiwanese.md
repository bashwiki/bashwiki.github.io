# [Linux] Bash dnf 用法: 管理和安裝軟體包

## Overview
`dnf` 是一個用於管理和安裝 Linux 系統中軟體包的命令行工具。它是 `yum` 的下一代版本，提供更快的性能和更好的依賴性解決方案。

## Usage
基本語法如下：
```bash
dnf [options] [arguments]
```

## Common Options
- `install`: 安裝指定的軟體包。
- `remove`: 移除指定的軟體包。
- `update`: 更新已安裝的軟體包到最新版本。
- `search`: 搜尋可用的軟體包。
- `list`: 列出已安裝或可用的軟體包。

## Common Examples
- 安裝一個軟體包：
  ```bash
  dnf install package_name
  ```

- 移除一個軟體包：
  ```bash
  dnf remove package_name
  ```

- 更新所有已安裝的軟體包：
  ```bash
  dnf update
  ```

- 搜尋特定的軟體包：
  ```bash
  dnf search package_name
  ```

- 列出所有已安裝的軟體包：
  ```bash
  dnf list installed
  ```

## Tips
- 在進行大規模更新之前，建議先備份系統，以防止意外問題。
- 使用 `dnf history` 可以查看過去的操作紀錄，方便追蹤變更。
- 定期使用 `dnf clean all` 來清理快取，釋放磁碟空間。