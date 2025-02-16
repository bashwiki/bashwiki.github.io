# [Linux] Bash lspci 使用方法: 列出所有 PCI 裝置

## Overview
`lspci` 命令用於列出系統中所有的 PCI (Peripheral Component Interconnect) 裝置。這個命令能夠幫助用戶檢視硬體設備的詳細資訊，對於系統管理和故障排除非常有用。

## Usage
基本語法如下：
```
lspci [options] [arguments]
```

## Common Options
- `-v`：顯示詳細資訊。
- `-vv`：顯示更詳細的資訊。
- `-k`：顯示與每個裝置相關的驅動程式資訊。
- `-n`：顯示裝置的數字 ID，而不是名稱。
- `-s <slot>`：僅顯示指定插槽的裝置。

## Common Examples
- 列出所有 PCI 裝置：
    ```bash
    lspci
    ```

- 顯示詳細資訊：
    ```bash
    lspci -v
    ```

- 顯示驅動程式資訊：
    ```bash
    lspci -k
    ```

- 僅顯示特定插槽的裝置：
    ```bash
    lspci -s 00:1f.0
    ```

- 顯示數字 ID：
    ```bash
    lspci -n
    ```

## Tips
- 使用 `lspci | less` 可以方便地瀏覽長列表。
- 結合 `grep` 使用可以快速查找特定裝置，例如：
    ```bash
    lspci | grep -i network
    ```
- 定期檢查 PCI 裝置資訊有助於保持系統的穩定性和性能。