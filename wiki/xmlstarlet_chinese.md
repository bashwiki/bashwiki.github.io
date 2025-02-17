# [Linux] Bash xmlstarlet 用法: 处理和转换XML数据

## 概述
xmlstarlet 是一个命令行工具，用于处理和转换 XML 数据。它提供了一系列功能，包括查询、编辑、格式化和验证 XML 文件，使得用户能够高效地操作 XML 格式的数据。

## 用法
基本语法如下：
```bash
xmlstarlet [选项] [参数]
```

## 常用选项
- `sel`：选择 XML 数据。
- `ed`：编辑 XML 数据。
- `val`：验证 XML 文件。
- `fo`：格式化输出。
- `transform`：应用 XSLT 转换。

## 常见示例

### 选择 XML 数据
从 XML 文件中选择特定节点：
```bash
xmlstarlet sel -t -m "/bookstore/book" -v "title" -n books.xml
```

### 编辑 XML 数据
向 XML 文件中添加新节点：
```bash
xmlstarlet ed -s "/bookstore" -t elem -n "book" -v "" books.xml
```

### 验证 XML 文件
验证 XML 文件的格式是否正确：
```bash
xmlstarlet val books.xml
```

### 格式化输出
格式化并美化 XML 文件：
```bash
xmlstarlet fo books.xml
```

### 应用 XSLT 转换
使用 XSLT 文件转换 XML 数据：
```bash
xmlstarlet transform -s stylesheet.xsl -o output.xml input.xml
```

## 小贴士
- 使用 `-o` 选项可以将输出重定向到文件，方便保存结果。
- 结合其他命令（如 `grep` 或 `awk`）可以实现更复杂的数据处理。
- 在处理大文件时，注意内存使用情况，避免系统崩溃。