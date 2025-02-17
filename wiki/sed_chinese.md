# [Linux] Bash sed 用法: 文本流编辑器

## 概述
`sed` 是一个强大的流编辑器，用于对文本进行基本的处理和转换。它可以在文件或标准输入中查找、替换、插入和删除文本行。

## 用法
基本语法如下：
```bash
sed [options] [arguments]
```

## 常用选项
- `-e`：允许在命令行中指定多个编辑命令。
- `-i`：直接在文件中修改，而不是输出到标准输出。
- `-n`：抑制自动输出，通常与 `p` 命令结合使用以输出特定行。
- `s`：替换命令，用于查找和替换文本。

## 常见示例
1. **替换文本**
   将文件中的 "apple" 替换为 "orange"：
   ```bash
   sed 's/apple/orange/g' filename.txt
   ```

2. **在文件中直接替换**
   直接在文件中将 "apple" 替换为 "orange"：
   ```bash
   sed -i 's/apple/orange/g' filename.txt
   ```

3. **删除特定行**
   删除文件中的第2行：
   ```bash
   sed '2d' filename.txt
   ```

4. **打印特定行**
   仅打印文件中的第1和第3行：
   ```bash
   sed -n '1p; 3p' filename.txt
   ```

5. **插入文本**
   在第2行之前插入 "Hello World"：
   ```bash
   sed '2i Hello World' filename.txt
   ```

## 小贴士
- 使用 `-i` 选项时，请务必备份原始文件，以防不小心丢失数据。
- 在使用 `s` 命令时，确保使用 `g` 选项以替换行中的所有匹配项。
- 可以使用正则表达式增强 `sed` 的查找和替换功能，使其更加灵活。