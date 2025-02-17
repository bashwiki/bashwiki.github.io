# [Linux] Bash cmake Uso: Configure and generate build files

## Overview
The `cmake` command is a powerful tool used for managing the build process of software projects. It generates makefiles or project files for various build systems based on the configuration specified in the `CMakeLists.txt` file found in the project directory. This allows developers to easily compile and link their code across different platforms and environments.

## Usage
The basic syntax of the `cmake` command is as follows:

```bash
cmake [options] [arguments]
```

## Common Options
- `-S <path>`: Specify the source directory containing the `CMakeLists.txt` file.
- `-B <path>`: Specify the build directory where the generated files will be placed.
- `-D <var>=<value>`: Define a variable to be used in the configuration process.
- `-G <generator>`: Specify the build system generator (e.g., `Unix Makefiles`, `Ninja`).
- `--build <path>`: Build the project in the specified directory.

## Common Examples
Here are some practical examples of using `cmake`:

1. **Basic Configuration**
   To configure a project located in the current directory and generate makefiles:
   ```bash
   cmake .
   ```

2. **Specify Source and Build Directories**
   To configure a project with a specific source and build directory:
   ```bash
   cmake -S /path/to/source -B /path/to/build
   ```

3. **Define Variables**
   To define a variable during the configuration process:
   ```bash
   cmake -D CMAKE_BUILD_TYPE=Release -S . -B build
   ```

4. **Using a Specific Generator**
   To specify a build system generator:
   ```bash
   cmake -G "Ninja" -S . -B build
   ```

5. **Building the Project**
   To build the project after configuration:
   ```bash
   cmake --build build
   ```

## Tips
- Always create a separate build directory to keep your source directory clean.
- Use `cmake-gui` for a graphical interface if you prefer a visual approach to configuring your project.
- Check the output of `cmake` for any warnings or errors to ensure a successful configuration.
- Familiarize yourself with the `CMakeLists.txt` file syntax to customize your build process effectively.