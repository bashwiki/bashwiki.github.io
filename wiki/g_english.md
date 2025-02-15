# [리눅스] Bash g++ 사용법

## Overview
`g++` is the GNU C++ Compiler, part of the GNU Compiler Collection (GCC). It is primarily used to compile C++ source code files into executable programs. The command takes C++ source files as input and produces an object file or an executable, depending on the options provided. `g++` supports various C++ standards and provides a range of optimization and debugging options, making it a powerful tool for developers working in C++.

## Usage
The basic syntax for using `g++` is as follows:

```bash
g++ [options] [source files] [object files] -o [output file]
```

### Common Options:
- `-o [output file]`: Specifies the name of the output file. If this option is not provided, the default output file will be named `a.out`.
- `-c`: Compiles the source files into object files without linking. This is useful for compiling multiple source files separately.
- `-Wall`: Enables all compiler's warning messages. This is helpful for identifying potential issues in your code.
- `-std=[standard]`: Specifies the C++ standard to use (e.g., `-std=c++11`, `-std=c++14`, `-std=c++17`, `-std=c++20`).
- `-g`: Generates debug information to be used by GDB (GNU Debugger), which is useful for debugging your program.

## Examples

### Example 1: Compiling a Simple C++ Program
Suppose you have a simple C++ program saved in a file named `hello.cpp`:

```cpp
#include <iostream>
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

You can compile this program using `g++` as follows:

```bash
g++ hello.cpp -o hello
```

This command compiles `hello.cpp` and creates an executable named `hello`. You can then run the program with:

```bash
./hello
```

### Example 2: Compiling Multiple Source Files
If you have multiple C++ source files, such as `file1.cpp` and `file2.cpp`, you can compile them together:

```bash
g++ file1.cpp file2.cpp -o my_program
```

Alternatively, if you want to compile them separately and then link them, you can use the `-c` option:

```bash
g++ -c file1.cpp
g++ -c file2.cpp
g++ file1.o file2.o -o my_program
```

## Tips
- Always use the `-Wall` option to enable warnings. This helps catch potential issues early in the development process.
- Consider using the `-g` option during development to facilitate debugging. You can remove it in the final build for optimization.
- Familiarize yourself with different C++ standards and use the `-std` option to ensure compatibility with the features you want to use.
- For larger projects, consider using a build system like Make or CMake to manage compilation and linking efficiently. This can simplify the process of compiling multiple files and managing dependencies.