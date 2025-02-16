# [Linux] Bash make 使用法: 用於自動化編譯和建構專案

## Overview
`make` 是一個自動化工具，用於管理和編譯大型專案的程式碼。它根據一個稱為 `Makefile` 的檔案來決定如何編譯和鏈接程式，從而簡化了開發過程。

## Usage
基本語法如下：
```
make [options] [arguments]
```

## Common Options
- `-f FILE`：指定使用的 `Makefile` 檔案，預設為 `Makefile` 或 `makefile`。
- `-j N`：同時執行 N 個任務，加快編譯速度。
- `-k`：在遇到錯誤時繼續執行，儘量完成其他任務。
- `-B`：強制重新編譯所有目標，即使它們已經是最新的。

## Common Examples
以下是一些常見的 `make` 使用範例：

### 編譯專案
假設有一個 `Makefile`，可以直接使用：
```bash
make
```

### 指定 Makefile
如果你的 `Makefile` 名稱不同，可以這樣指定：
```bash
make -f MyMakefile
```

### 同時編譯多個任務
使用 `-j` 選項來加速編譯：
```bash
make -j4
```

### 強制重新編譯
如果你想強制重新編譯所有檔案，可以使用：
```bash
make -B
```

## Tips
- 確保 `Makefile` 的語法正確，否則 `make` 可能無法正常運行。
- 使用 `make clean` 來清理編譯產物，保持專案整潔。
- 定期更新 `Makefile`，以反映專案的變更和依賴關係。