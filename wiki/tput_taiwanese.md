# [台灣] Bash tput 使用法: 控制終端顯示

## Overview
`tput` 是一個用於控制終端顯示的命令，能夠設置顏色、格式和其他顯示屬性，讓使用者可以自訂終端的外觀。

## Usage
基本語法如下：
```bash
tput [options] [arguments]
```

## Common Options
- `setaf [n]`：設置前景色，`n` 是顏色的編號。
- `setab [n]`：設置背景色，`n` 是顏色的編號。
- `bold`：設置文字為粗體。
- `smso`：啟用反白顯示。
- `rmso`：取消反白顯示。
- `clear`：清除終端屏幕。

## Common Examples
- 設置前景色為紅色：
```bash
tput setaf 1
```
- 設置背景色為藍色：
```bash
tput setab 4
```
- 設置文字為粗體：
```bash
tput bold
```
- 啟用反白顯示：
```bash
tput smso
```
- 清除終端屏幕：
```bash
tput clear
```

## Tips
- 使用 `tput reset` 可以恢復終端到初始狀態。
- 可以將常用的 `tput` 命令寫入腳本，以便快速使用。
- 使用 `tput colors` 可以查看終端支持的顏色數量。