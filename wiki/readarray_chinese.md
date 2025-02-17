# [Linux] Bash readarray 用法: 从标准输入读取数组

## 概述
`readarray` 命令用于从标准输入读取数据并将其存储到数组中。它可以方便地处理多行输入，将每一行作为数组的一个元素。

## 用法
基本语法如下：
```bash
readarray [options] [array_name]
```

## 常用选项
- `-n`：指定读取的行数。
- `-s`：跳过指定的行数。
- `-t`：去掉每行末尾的换行符。
- `-p`：在读取前打印提示信息。

## 常见示例
以下是一些常见的使用示例：

### 示例 1: 读取文件到数组
将文件中的每一行读取到数组 `my_array` 中：
```bash
readarray my_array < myfile.txt
```

### 示例 2: 读取标准输入
从标准输入读取数据并存储到数组：
```bash
echo -e "line1\nline2\nline3" | readarray my_array
```

### 示例 3: 去掉换行符
读取文件并去掉每行末尾的换行符：
```bash
readarray -t my_array < myfile.txt
```

### 示例 4: 读取指定行数
只读取文件中的前两行：
```bash
readarray -n 2 my_array < myfile.txt
```

## 提示
- 使用 `-t` 选项可以避免在数组元素中出现多余的换行符，便于后续处理。
- 在处理大文件时，可以结合 `-s` 选项跳过不需要的行，以提高效率。
- 确保数组名称在脚本中唯一，以避免与其他变量冲突。