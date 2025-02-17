# [Linux] Bash jq 用法: 处理JSON数据的强大工具

## 概述
`jq` 是一个轻量级且灵活的命令行工具，用于处理和操作JSON数据。它能够解析JSON格式的数据，并允许用户进行过滤、转换和格式化输出，特别适合在脚本中使用。

## 用法
基本语法如下：
```bash
jq [options] [arguments]
```

## 常用选项
- `-c`：以紧凑格式输出结果。
- `-r`：输出原始字符串，而不是JSON格式。
- `-f <file>`：从指定的文件中读取jq程序。
- `--arg <name> <value>`：定义一个变量并在jq表达式中使用。

## 常见示例
1. **读取JSON文件**
   ```bash
   jq '.' data.json
   ```
   这个命令将读取 `data.json` 文件并输出其内容。

2. **提取特定字段**
   ```bash
   jq '.name' data.json
   ```
   该命令将提取JSON对象中的 `name` 字段。

3. **过滤数组**
   ```bash
   jq '.users[] | select(.age > 30)' data.json
   ```
   这个命令将从 `users` 数组中筛选出年龄大于30的用户。

4. **修改JSON数据**
   ```bash
   jq '.name = "新名字"' data.json
   ```
   该命令将 `name` 字段的值修改为 "新名字"。

5. **以紧凑格式输出**
   ```bash
   jq -c '.' data.json
   ```
   这个命令将以紧凑格式输出 `data.json` 的内容。

## 小贴士
- 使用 `-r` 选项可以避免输出多余的引号，方便在其他命令中使用。
- 在处理大型JSON文件时，可以使用 `--slurp` 选项将多个JSON对象合并为一个数组。
- 结合其他命令（如 `curl`）使用 `jq` 可以方便地处理API返回的JSON数据。