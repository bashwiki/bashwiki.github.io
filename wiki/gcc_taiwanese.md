# [台灣] Bash gcc 使用方法: 編譯 C/C++ 程式

## Overview
`gcc` 是 GNU Compiler Collection 的縮寫，主要用來編譯 C 和 C++ 程式。它能將原始碼轉換成可執行的程式，並支援多種編譯選項，讓開發者能夠優化和調整編譯過程。

## Usage
基本語法如下：
```bash
gcc [options] [arguments]
```

## Common Options
- `-o <file>`: 指定輸出的檔案名稱。
- `-Wall`: 啟用所有警告訊息，幫助找出潛在的問題。
- `-g`: 生成包含除錯資訊的可執行檔。
- `-O <level>`: 開啟優化，`<level>` 可以是 0 到 3，數字越高優化程度越高。
- `-I <directory>`: 指定額外的包含檔案目錄。
- `-L <directory>`: 指定額外的庫檔案目錄。
- `-l <library>`: 連結指定的庫。

## Common Examples
以下是一些常見的使用範例：

1. 編譯單一 C 檔案：
   ```bash
   gcc hello.c -o hello
   ```

2. 編譯並啟用所有警告：
   ```bash
   gcc -Wall hello.c -o hello
   ```

3. 編譯 C++ 檔案：
   ```bash
   g++ hello.cpp -o hello
   ```

4. 編譯並生成除錯資訊：
   ```bash
   gcc -g hello.c -o hello
   ```

5. 使用優化選項：
   ```bash
   gcc -O2 hello.c -o hello
   ```

## Tips
- 在編譯大型專案時，可以考慮使用 Makefile 來管理編譯過程。
- 定期使用 `-Wall` 選項來檢查程式碼中的潛在問題。
- 在開發過程中，使用 `-g` 來生成除錯資訊，方便使用除錯工具進行調試。
- 當需要使用外部庫時，記得使用 `-I` 和 `-L` 來指定包含檔案和庫的目錄。