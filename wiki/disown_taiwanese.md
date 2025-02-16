# [台灣] Bash disown 用法: 解除工作與終端的關聯

## Overview
`disown` 命令用於解除當前終端與背景作業的關聯，這樣即使終端關閉，這些作業仍然會繼續運行。

## Usage
基本語法如下：
```bash
disown [options] [arguments]
```

## Common Options
- `-h`：只解除指定作業的掛起狀態。
- `-a`：解除所有作業的關聯。
- `-r`：只解除正在運行的作業。

## Common Examples
1. 解除最近一個背景作業的關聯：
   ```bash
   disown
   ```

2. 解除特定作業（例如作業號 1）的關聯：
   ```bash
   disown %1
   ```

3. 解除所有背景作業的關聯：
   ```bash
   disown -a
   ```

4. 解除所有正在運行的作業：
   ```bash
   disown -r
   ```

## Tips
- 在使用 `disown` 前，確保你已經將作業放到背景中，通常使用 `&` 符號。
- 使用 `jobs` 命令可以查看當前的作業列表，幫助你選擇要解除的作業。
- `disown` 是一個非常有用的命令，特別是在需要長時間運行的任務時，確保它們不會因終端關閉而中斷。