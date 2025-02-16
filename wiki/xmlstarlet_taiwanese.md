# [Linux] Bash xmlstarlet 使用方法: 用於處理 XML 文件的命令行工具

## Overview
xmlstarlet 是一個強大的命令行工具，用於處理和轉換 XML 文件。它可以用來查詢、修改、格式化和轉換 XML 數據，對於需要自動化 XML 操作的開發者和系統管理員來說非常有用。

## Usage
基本語法如下：
```bash
xmlstarlet [options] [arguments]
```

## Common Options
- `sel`: 選擇 XML 文件中的特定節點。
- `ed`: 編輯 XML 文件，添加、刪除或修改節點。
- `val`: 驗證 XML 文件是否符合 DTD 或 XSD。
- `fo`: 格式化輸出，使 XML 更易讀。
- `tr`: 轉換 XML 文件，使用 XSLT 樣式表。

## Common Examples
以下是一些常見的使用範例：

1. **選擇節點**
   ```bash
   xmlstarlet sel -t -m "//book" -v "title" -n books.xml
   ```
   這個命令會從 `books.xml` 文件中選擇所有 `book` 節點並顯示其 `title`。

2. **編輯 XML 文件**
   ```bash
   xmlstarlet ed -u "//book/title" -v "新書名" books.xml
   ```
   這個命令會將 `books.xml` 中所有 `book` 節點的 `title` 更新為 "新書名"。

3. **驗證 XML 文件**
   ```bash
   xmlstarlet val -e books.xml
   ```
   這個命令會驗證 `books.xml` 文件的結構是否正確。

4. **格式化輸出**
   ```bash
   xmlstarlet fo books.xml
   ```
   這個命令會將 `books.xml` 文件格式化並輸出到終端。

5. **轉換 XML 文件**
   ```bash
   xmlstarlet tr style.xsl input.xml > output.xml
   ```
   這個命令會使用 `style.xsl` 樣式表轉換 `input.xml`，並將結果輸出到 `output.xml`。

## Tips
- 在使用 `xmlstarlet` 進行編輯時，建議先備份原始 XML 文件，以防不小心刪除重要數據。
- 使用 `-o` 選項可以指定輸出格式，這對於生成特定格式的 XML 文件非常有用。
- 熟悉 XPath 語法可以幫助你更有效地使用 `xmlstarlet` 進行查詢和選擇操作。