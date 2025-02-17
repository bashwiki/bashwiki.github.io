# [Linux] Bash cmake 用法: 构建和管理项目

## 概述
`cmake` 是一个跨平台的开源构建系统工具，主要用于管理软件的编译过程。它使用简单的配置文件来生成标准的构建文件（如 Makefile 或 Visual Studio 项目文件），使得软件开发过程更加高效和灵活。

## 用法
基本语法如下：
```bash
cmake [options] [arguments]
```

## 常用选项
- `-S <path>`: 指定源代码目录。
- `-B <path>`: 指定构建目录。
- `-D <var>=<value>`: 设置 CMake 变量。
- `-G <generator>`: 指定生成器类型（如 Makefile、Ninja 等）。
- `--build <dir>`: 构建指定目录中的项目。

## 常见示例
1. **基本构建**
   ```bash
   cmake -S . -B build
   ```
   在当前目录生成构建文件到 `build` 目录。

2. **指定构建类型**
   ```bash
   cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
   ```
   在构建时指定为 Release 模式。

3. **使用特定生成器**
   ```bash
   cmake -S . -B build -G "Ninja"
   ```
   使用 Ninja 作为构建系统生成器。

4. **构建项目**
   ```bash
   cmake --build build
   ```
   在 `build` 目录中执行构建。

5. **清理构建**
   ```bash
   cmake --build build --target clean
   ```
   清理构建目录中的生成文件。

## 提示
- 在使用 `cmake` 时，建议保持源代码和构建目录分离，以便于管理和清理。
- 使用 `-D` 选项可以方便地传递自定义参数，帮助配置项目。
- 定期查看 CMake 的文档和更新，以利用新功能和最佳实践。