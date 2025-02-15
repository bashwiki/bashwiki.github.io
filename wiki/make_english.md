# [리눅스] Bash make 사용법

## Overview
The `make` command is a build automation tool primarily used to compile and manage dependencies in software projects. It reads a file called `Makefile`, which contains rules and instructions on how to build the project, including which files to compile and how to link them together. The primary purpose of `make` is to simplify the process of building and maintaining complex software projects by automating the compilation process and ensuring that only the necessary parts of the project are rebuilt when changes are made.

## Usage
The basic syntax of the `make` command is as follows:

```bash
make [options] [target]
```

### Common Options:
- `-f FILE`, `--file=FILE`: Specify an alternative Makefile instead of the default `Makefile`.
- `-j N`, `--jobs=N`: Allow `make` to run multiple jobs simultaneously, where `N` is the number of jobs to run in parallel.
- `-k`, `--keep-going`: Continue building as much as possible after an error occurs.
- `-n`, `--just-print`: Print the commands that would be executed without actually executing them.
- `-s`, `--silent`: Suppress the output of the commands being executed.

If no target is specified, `make` will build the first target defined in the Makefile.

## Examples

### Example 1: Basic Usage
To compile a project using the default `Makefile`, simply navigate to the project directory and run:

```bash
make
```

This command will execute the first target defined in the `Makefile`, which typically compiles the source code into an executable.

### Example 2: Specifying a Target
If you want to build a specific target defined in the `Makefile`, you can specify it directly:

```bash
make clean
```

In this example, the `clean` target is executed, which usually removes compiled files and cleans up the project directory.

## Tips
- Always ensure your `Makefile` is well-structured and documented. This makes it easier for others (and yourself) to understand the build process.
- Use the `-j` option to speed up the build process, especially for large projects with many independent files.
- Regularly run `make clean` to remove unnecessary files and keep your project directory tidy.
- Utilize comments in your `Makefile` to explain complex rules or dependencies, which can help in maintaining the build process over time.