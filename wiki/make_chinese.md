# [리눅스] Bash make 사용법

## 概述
`make` 是一个自动化构建工具，主要用于管理和维护程序的编译过程。它通过读取一个名为 `Makefile` 的文件，确定如何编译和链接程序的各个部分。`make` 的主要目的是简化和加速软件开发过程，特别是在处理大型项目时。

## 用法
基本语法如下：
```bash
make [选项] [目标]
```
常用选项包括：
- `-f FILE`：指定要使用的 `Makefile` 文件，默认是 `Makefile` 或 `makefile`。
- `-j N`：并行执行 N 个任务，可以加快构建速度。
- `-k`：即使某些目标失败，也继续构建其他目标。
- `clean`：通常在 `Makefile` 中定义，用于清理构建产生的临时文件。

## 示例
### 示例 1：基本使用
假设你有一个简单的 `Makefile`，内容如下：
```makefile
all: hello

hello: hello.o
    gcc -o hello hello.o

hello.o: hello.c
    gcc -c hello.c

clean:
    rm -f hello hello.o
```
你可以在终端中运行以下命令来构建项目：
```bash
make
```
这将编译 `hello.c` 并生成可执行文件 `hello`。

### 示例 2：使用并行构建
如果你的项目有多个独立的目标，可以使用 `-j` 选项来加速构建：
```bash
make -j4
```
这将并行执行最多 4 个构建任务。

## 提示
- 确保 `Makefile` 的语法正确，缩进必须使用制表符而不是空格。
- 定期使用 `make clean` 来清理构建目录，保持环境整洁。
- 在大型项目中，合理组织 `Makefile` 可以提高可维护性和可读性。
- 使用版本控制系统（如 Git）来管理 `Makefile` 的变更，以便追踪历史和协作开发。