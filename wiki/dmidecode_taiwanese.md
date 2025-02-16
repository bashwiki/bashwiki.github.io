# [Linux] Bash dmidecode 使用法: 獲取系統硬體資訊

## Overview
`dmidecode` 是一個用於提取系統硬體資訊的命令行工具。它從系統的 DMI（桌面管理界面）表中讀取資料，提供有關硬體組件的詳細資訊，如處理器、記憶體、主機板等。

## Usage
基本語法如下：
```
dmidecode [options] [arguments]
```

## Common Options
- `-t <type>`: 指定要顯示的 DMI 類型，例如 `-t memory` 只顯示記憶體資訊。
- `-q`: 啟用安靜模式，僅顯示必要的輸出。
- `-s <string>`: 顯示特定的 DMI 字串，例如 `-s system-product-name` 來顯示系統產品名稱。

## Common Examples
1. 顯示所有 DMI 資訊：
   ```bash
   dmidecode
   ```

2. 顯示特定類型的資訊，例如記憶體：
   ```bash
   dmidecode -t memory
   ```

3. 顯示系統製造商名稱：
   ```bash
   dmidecode -s system-manufacturer
   ```

4. 顯示處理器資訊：
   ```bash
   dmidecode -t processor
   ```

## Tips
- 在使用 `dmidecode` 時，通常需要以 root 權限執行，因此可以使用 `sudo`。
- 若要快速查找特定資訊，使用 `-s` 選項是非常有效的。
- 了解 DMI 類型可以幫助你更精確地獲取所需的硬體資訊。