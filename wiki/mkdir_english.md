# [리눅스] Bash mkdir 사용법

## Overview
The `mkdir` command in Bash is used to create new directories (folders) within the filesystem. Its primary purpose is to allow users to organize files and directories in a structured manner. This command is essential for managing file systems effectively, enabling users to create a hierarchy of directories for better organization.

## Usage
The basic syntax of the `mkdir` command is as follows:

```bash
mkdir [options] directory_name
```

### Common Options:
- `-p`: This option allows the creation of parent directories as needed. If the specified parent directory does not exist, it will be created automatically.
- `-v`: This option enables verbose mode, which provides detailed output about the directories being created.
- `-m mode`: This option allows you to set the permissions for the new directory at the time of creation, using the specified mode.

## Examples
Here are a couple of practical examples demonstrating how to use the `mkdir` command:

1. **Creating a Single Directory**:
   To create a directory named `projects`, you would use the following command:

   ```bash
   mkdir projects
   ```

2. **Creating Nested Directories**:
   If you want to create a directory structure like `2023/January/Projects`, you can use the `-p` option:

   ```bash
   mkdir -p 2023/January/Projects
   ```

   This command will create the `2023` directory, then the `January` directory inside it, and finally the `Projects` directory.

## Tips
- Always use the `-p` option when creating nested directories to avoid errors if the parent directories do not exist.
- Utilize the `-v` option for scripts or when running commands in a terminal to confirm that directories were created successfully.
- Consider setting appropriate permissions with the `-m` option if you need specific access controls for the new directories right from the start.
- Regularly organize your directories to maintain a clean and efficient file system, which can improve productivity and ease of access to files.