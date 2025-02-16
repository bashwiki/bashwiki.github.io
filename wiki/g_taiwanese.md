# [Linux] Bash g++ 使用方法: 編譯 C++ 程式

## Overview
g++ 是 GNU Compiler Collection (GCC) 的一部分，專門用來編譯 C++ 程式碼。它將 C++ 源碼轉換為可執行的二進制檔案，讓開發者能夠運行他們的程式。

## Usage
基本語法如下：
```bash
g++ [options] [arguments]
```

## Common Options
- `-o <file>`: 指定輸出的可執行檔名稱。
- `-Wall`: 啟用所有警告訊息，幫助開發者發現潛在的問題。
- `-g`: 生成調試資訊，便於使用調試工具進行除錯。
- `-std=<standard>`: 指定 C++ 標準，例如 `-std=c++11`。

## Common Examples
1. 編譯單一 C++ 檔案：
   ```bash
   g++ main.cpp -o main
   ```

2. 編譯並啟用所有警告：
   ```bash
   g++ -Wall main.cpp -o main
   ```

3. 編譯多個 C++ 檔案：
   ```bash
   g++ file1.cpp file2.cpp -o program
   ```

4. 編譯並生成調試資訊：
   ```bash
   g++ -g main.cpp -o main
   ```

5. 使用特定的 C++ 標準：
   ```bash
   g++ -std=c++11 main.cpp -o main
   ```

## Tips
- 在編譯大型專案時，考慮使用 Makefile 來管理編譯過程，這樣可以簡化命令並提高效率。
- 定期使用 `-Wall` 選項來檢查程式碼中的潛在問題。
- 如果遇到編譯錯誤，仔細檢查錯誤訊息，通常會提供有用的提示來修正問題。