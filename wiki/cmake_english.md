# [리눅스] Bash cmake 사용법

## Overview
`cmake` is a cross-platform build system generator that is widely used in software development. Its primary purpose is to control the software compilation process using simple platform and compiler-independent configuration files. By generating native makefiles or project files for various IDEs, `cmake` simplifies the process of building and managing complex software projects.

## Usage
The basic syntax for the `cmake` command is as follows:

```bash
cmake [options] <path-to-source>
```

### Common Options:
- `-B <path>`: Specify the build directory. If not provided, it defaults to the current directory.
- `-S <path>`: Specify the source directory. If not provided, it defaults to the current directory.
- `-G <generator-name>`: Specify the build system generator to use (e.g., "Unix Makefiles", "Ninja", "Visual Studio").
- `-D <var>=<value>`: Define a variable for the configuration. This is useful for setting options that control the build process.
- `--build <path>`: Build the project in the specified directory. This can be used after configuring the project.

## Examples

### Example 1: Basic Configuration
To configure a project located in the `my_project` directory and generate makefiles in a `build` directory, you would use:

```bash
mkdir build
cd build
cmake -S ../my_project -B .
```

### Example 2: Building the Project
After configuring the project, you can build it using:

```bash
cmake --build .
```

This command will compile the project using the generated makefiles in the current directory.

## Tips
- Always create a separate build directory to keep your source directory clean. This helps in managing different build configurations easily.
- Use the `-D` option to customize build options, such as enabling or disabling features in your project.
- Familiarize yourself with the available generators by running `cmake --help` to choose the most suitable one for your environment.
- If you encounter issues during the build process, check the `CMakeCache.txt` file in the build directory for configuration settings and paths.