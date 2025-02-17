# [Linux] Bash gcc 用法: 编译C和C++程序

## 概述
`gcc`（GNU Compiler Collection）是一个强大的编译器，用于将C和C++源代码编译成可执行文件。它是开源软件，广泛用于Linux和其他类Unix操作系统。

## 用法
基本的命令语法如下：
```bash
gcc [选项] [参数]
```

## 常用选项
- `-o <文件名>`: 指定输出文件的名称。
- `-Wall`: 启用所有警告信息，帮助发现潜在问题。
- `-g`: 生成调试信息，便于使用调试器调试程序。
- `-O2`: 启用优化，提升程序的执行效率。
- `-I<目录>`: 指定头文件搜索路径。

## 常见示例
1. 编译一个简单的C程序：
   ```bash
   gcc hello.c -o hello
   ```
   这将把 `hello.c` 编译成可执行文件 `hello`。

2. 启用所有警告并编译：
   ```bash
   gcc -Wall hello.c -o hello
   ```

3. 生成调试信息：
   ```bash
   gcc -g hello.c -o hello
   ```

4. 使用优化选项编译：
   ```bash
   gcc -O2 hello.c -o hello
   ```

5. 指定头文件搜索路径：
   ```bash
   gcc -I/usr/local/include hello.c -o hello
   ```

## 小贴士
- 在编写代码时，建议始终使用 `-Wall` 选项，以便及时发现代码中的潜在问题。
- 对于大型项目，可以考虑使用 `Makefile` 来管理编译过程，简化命令的输入。
- 定期更新 `gcc` 版本，以获得最新的功能和性能改进。