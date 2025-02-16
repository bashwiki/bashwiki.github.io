# [Linux] Bash virsh 使用法: 管理虛擬機器

## Overview
`virsh` 是一個用於管理虛擬機器的命令行工具，通常與 KVM 和其他虛擬化技術一起使用。它允許用戶創建、刪除、啟動和停止虛擬機器，並執行其他管理任務。

## Usage
基本語法如下：
```
virsh [options] [arguments]
```

## Common Options
- `list`：列出當前運行的虛擬機器。
- `start <domain>`：啟動指定的虛擬機器。
- `shutdown <domain>`：關閉指定的虛擬機器。
- `destroy <domain>`：強制停止指定的虛擬機器。
- `create <filename>`：根據 XML 文件創建虛擬機器。
- `define <filename>`：定義虛擬機器但不啟動它。

## Common Examples
- 列出所有運行中的虛擬機器：
  ```bash
  virsh list
  ```

- 啟動名為 `myvm` 的虛擬機器：
  ```bash
  virsh start myvm
  ```

- 關閉名為 `myvm` 的虛擬機器：
  ```bash
  virsh shutdown myvm
  ```

- 強制停止名為 `myvm` 的虛擬機器：
  ```bash
  virsh destroy myvm
  ```

- 根據 `myvm.xml` 文件創建虛擬機器：
  ```bash
  virsh create myvm.xml
  ```

- 定義虛擬機器但不啟動：
  ```bash
  virsh define myvm.xml
  ```

## Tips
- 在使用 `virsh` 之前，確保您有適當的權限來管理虛擬機器。
- 使用 `virsh help` 獲取更多命令和選項的詳細資訊。
- 定期備份虛擬機器的配置文件，以防止數據丟失。