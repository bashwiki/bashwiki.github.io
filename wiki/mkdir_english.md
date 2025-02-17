# [Linux] Bash mkdir Usage: Create directories in the filesystem

## Overview
The `mkdir` command in Bash is used to create new directories in the filesystem. It allows users to organize files and folders effectively by creating a structured hierarchy.

## Usage
The basic syntax of the `mkdir` command is as follows:

```bash
mkdir [options] [arguments]
```

## Common Options
- `-p`: Create parent directories as needed. If the specified directory path does not exist, it will create all necessary parent directories.
- `-v`: Verbose mode. This option will provide a message for each directory created.
- `-m`: Set the file mode (permissions) for the new directories. This can be specified in octal format.

## Common Examples

1. **Create a single directory:**
   ```bash
   mkdir my_directory
   ```

2. **Create multiple directories at once:**
   ```bash
   mkdir dir1 dir2 dir3
   ```

3. **Create a nested directory structure:**
   ```bash
   mkdir -p parent_dir/child_dir/grandchild_dir
   ```

4. **Create a directory with specific permissions:**
   ```bash
   mkdir -m 755 my_secure_directory
   ```

5. **Verbose output while creating directories:**
   ```bash
   mkdir -v new_folder
   ```

## Tips
- Use the `-p` option when creating nested directories to avoid errors if any parent directories do not exist.
- Always check the permissions of newly created directories with `ls -l` to ensure they meet your security requirements.
- Combine `mkdir` with other commands in scripts to automate directory creation for projects or backups.