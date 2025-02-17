# [Linux] Bash g++ Uso: Compilar código C++ 

## Overview
The `g++` command is the GNU C++ Compiler, which is used to compile C++ source code into executable programs. It is part of the GNU Compiler Collection (GCC) and supports various C++ standards, enabling developers to create efficient and portable applications.

## Usage
The basic syntax for the `g++` command is as follows:

```bash
g++ [options] [arguments]
```

## Common Options
Here are some commonly used options with `g++`:

- `-o <file>`: Specifies the name of the output file. If not provided, the default output file is `a.out`.
- `-Wall`: Enables all compiler's warning messages.
- `-g`: Generates debug information to be used by GDB (GNU Debugger).
- `-std=<standard>`: Specifies the C++ standard to use (e.g., `-std=c++11`, `-std=c++14`, `-std=c++17`).
- `-I<directory>`: Adds a directory to the list of directories to be searched for header files.
- `-L<directory>`: Adds a directory to the list of directories to be searched for library files.
- `-l<library>`: Links against the specified library.

## Common Examples

### Compile a Simple C++ Program
To compile a simple C++ program named `hello.cpp`:

```bash
g++ hello.cpp
```

This will create an executable named `a.out`.

### Compile with a Specific Output Name
To compile `hello.cpp` and name the output executable `hello`:

```bash
g++ hello.cpp -o hello
```

### Enable Warnings
To compile `hello.cpp` while enabling all warnings:

```bash
g++ -Wall hello.cpp -o hello
```

### Compile with Debug Information
To compile `hello.cpp` with debug information:

```bash
g++ -g hello.cpp -o hello
```

### Use a Specific C++ Standard
To compile `hello.cpp` using the C++11 standard:

```bash
g++ -std=c++11 hello.cpp -o hello
```

### Link Against a Library
To compile and link against a library, such as `m` for math functions:

```bash
g++ hello.cpp -o hello -lm
```

## Tips
- Always use the `-Wall` option to catch potential issues early in your code.
- If you are debugging, remember to use the `-g` option to include debug symbols.
- Organize your code into multiple files and use `-I` to specify include directories for header files.
- Regularly check for updates to the GCC to take advantage of new features and optimizations.