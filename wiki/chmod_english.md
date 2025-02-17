# [Linux] Bash chmod Uso: Change file permissions

## Overview
The `chmod` command in Bash is used to change the file system permissions of files and directories. It allows users to define who can read, write, or execute a file, thereby controlling access to the system's resources.

## Usage
The basic syntax of the `chmod` command is as follows:

```bash
chmod [options] [permissions] [file/directory]
```

## Common Options
- `-R`: Recursively change permissions for all files and directories within the specified directory.
- `-v`: Verbosely show the changes made to the permissions.
- `-c`: Like `-v`, but only reports when a change is made.

## Common Examples

1. **Change permissions to read and write for the owner, and read for the group and others:**
   ```bash
   chmod 644 myfile.txt
   ```

2. **Add execute permission for the owner:**
   ```bash
   chmod u+x myscript.sh
   ```

3. **Remove write permission for the group:**
   ```bash
   chmod g-w myfile.txt
   ```

4. **Recursively change permissions to read, write, and execute for everyone in a directory:**
   ```bash
   chmod -R 777 mydirectory
   ```

5. **Set permissions to read and execute for the owner, and read for the group and others:**
   ```bash
   chmod 555 myfile.txt
   ```

## Tips
- Always double-check the permissions you are setting, especially when using recursive options, to avoid unintentionally exposing sensitive files.
- Use symbolic notation (e.g., `u`, `g`, `o`, `+`, `-`) for more granular control over permissions instead of numeric values.
- Consider using `chmod -v` to see what changes are being made, which can help in troubleshooting permission issues.