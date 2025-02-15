# [리눅스] Bash gcc 사용법

## Overview
`gcc`, which stands for GNU Compiler Collection, is a powerful compiler system that supports various programming languages, primarily C and C++. Its primary purpose is to convert source code written in these languages into executable programs. `gcc` is widely used in software development, enabling developers to compile their code efficiently and effectively.

## Usage
The basic syntax for using `gcc` is as follows:

```bash
gcc [options] [source files] [object files] [libraries]
```

### Common Options
- `-o <output_file>`: Specifies the name of the output file. If this option is not provided, the default output file will be named `a.out`.
- `-c`: Compiles the source files into object files without linking.
- `-Wall`: Enables all compiler's warning messages, which is useful for identifying potential issues in the code.
- `-g`: Includes debugging information in the output file, making it easier to debug the program using tools like `gdb`.
- `-I<directory>`: Adds a directory to the list of directories to be searched for header files.
- `-L<directory>`: Adds a directory to the list of directories to be searched for libraries during linking.
- `-l<library>`: Links against the specified library.

## Examples

### Example 1: Compiling a Simple C Program
To compile a simple C program named `hello.c` and create an executable named `hello`, you can use the following command:

```bash
gcc -o hello hello.c
```

### Example 2: Compiling with Debug Information
If you want to compile a C program and include debugging information, you can use the `-g` option:

```bash
gcc -g -o debug_example debug_example.c
```

### Example 3: Compiling Multiple Source Files
To compile multiple source files into a single executable, you can list all the source files:

```bash
gcc -o my_program file1.c file2.c file3.c
```

## Tips
- Always use the `-Wall` option to enable warnings; this helps catch potential issues early in the development process.
- For larger projects, consider using a Makefile to manage the compilation process, which can simplify building your project and managing dependencies.
- Regularly clean up your build directory by removing old object files and executables to avoid confusion and save space.
- Familiarize yourself with additional `gcc` options by checking the manual page using the command `man gcc` for more advanced features and optimizations.