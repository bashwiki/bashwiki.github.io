# [Linux] Bash cmake 使用法: 用於編譯和生成專案檔案

## Overview
`cmake` 是一個跨平台的開源工具，主要用於自動化編譯過程。它能夠根據使用者的設定生成適合不同平台的建構系統檔案，如 Makefile 或 Visual Studio 專案檔案。

## Usage
基本語法如下：
```bash
cmake [options] [arguments]
```

## Common Options
- `-S <source_dir>`: 指定來源目錄。
- `-B <build_dir>`: 指定建構目錄。
- `-D <var>=<value>`: 設定變數的值。
- `--build <dir>`: 在指定的目錄中執行建構。
- `--target <target>`: 指定要建構的目標。

## Common Examples
1. **生成建構檔案**:
   ```bash
   cmake -S . -B build
   ```
   這個命令會在當前目錄生成一個名為 `build` 的建構目錄。

2. **指定變數**:
   ```bash
   cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
   ```
   在生成建構檔案時，設定建構類型為 Release。

3. **執行建構**:
   ```bash
   cmake --build build
   ```
   這個命令會在 `build` 目錄中執行編譯。

4. **清除建構**:
   ```bash
   cmake --build build --target clean
   ```
   清除 `build` 目錄中的所有建構檔案。

## Tips
- 確保在使用 `cmake` 前，已經安裝了相應的編譯器和工具鏈。
- 使用 `-D` 參數來設定專案的選項，可以使專案更具彈性。
- 定期清理建構目錄，以避免舊檔案影響新的建構過程。