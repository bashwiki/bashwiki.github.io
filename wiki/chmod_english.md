# [리눅스] Bash chmod 사용법

## Overview
The `chmod` command in Bash is used to change the file mode bits of a file or directory. This command allows users to define who can read, write, or execute a file. The primary purpose of `chmod` is to manage file permissions, which is crucial for maintaining security and access control in a multi-user environment.

## Usage
The basic syntax of the `chmod` command is as follows:

```bash
chmod [options] mode file
```

### Common Options
- `-R`: Recursively change permissions for all files and directories within the specified directory.
- `-v`: Verbosely output the changes made.
- `-c`: Like `-v`, but only report when a change is made.

### Mode
The `mode` can be specified in two ways:
1. **Symbolic mode**: Using letters to represent the permission changes:
   - `u`: User (owner)
   - `g`: Group
   - `o`: Others
   - `a`: All (user, group, and others)
   - `+`: Add permission
   - `-`: Remove permission
   - `=`: Set permission exactly

   Example: `chmod u+x file.txt` adds execute permission for the user.

2. **Numeric mode**: Using octal numbers to represent permissions:
   - `4`: Read
   - `2`: Write
   - `1`: Execute
   - The permissions are summed for each category (user, group, others).

   Example: `chmod 755 file.txt` sets read, write, and execute for the user, and read and execute for group and others.

## Examples
1. **Adding Execute Permission for User**:
   To add execute permission for the user on a file named `script.sh`, you would use:
   ```bash
   chmod u+x script.sh
   ```

2. **Setting Permissions Using Numeric Mode**:
   To set the permissions of a directory named `myfolder` to read, write, and execute for the user, and read and execute for the group and others, you would use:
   ```bash
   chmod 755 myfolder
   ```

## Tips
- Always check the current permissions using `ls -l filename` before making changes to ensure you are modifying the correct permissions.
- Be cautious when using the `-R` option, as it will apply changes to all files and subdirectories, which may lead to unintended permission changes.
- Use `chmod` in combination with `chown` to manage both ownership and permissions effectively.
- Consider using symbolic mode for clarity when modifying specific permissions, especially in collaborative environments.