# [리눅스] Bash umask 사용법

## Overview
The `umask` command in Bash is used to set the default file permission mask for newly created files and directories. It defines the permissions that will not be set for new files and directories, effectively controlling the default access rights. By adjusting the umask value, users can ensure that files and directories are created with the desired permissions, enhancing security and collaboration.

## Usage
The basic syntax of the `umask` command is as follows:

```bash
umask [options] [mask]
```

- **mask**: This is an optional argument that specifies the new umask value. It can be provided in either symbolic or octal notation.
- **options**: Common options include:
  - `-S`: Display the current umask value in symbolic format.
  - `-p`: Print the current umask value in a format that can be reused in a script.

## Examples

### Example 1: Display Current Umask Value
To check the current umask value, simply run:

```bash
umask
```

This will output the current umask setting, typically in octal format (e.g., `0022`).

### Example 2: Set a New Umask Value
To set a new umask value, for example, to restrict group and others from writing to new files, you can use:

```bash
umask 027
```

This command sets the umask to `027`, which means:
- Owner: read, write (7)
- Group: read (2)
- Others: no permissions (0)

As a result, new files will have permissions of `640` (read and write for the owner, read for the group, no permissions for others).

## Tips
- Always check your current umask value before changing it to understand the impact on file permissions.
- Use symbolic notation (e.g., `umask u=rwx,g=rx,o=`) for more readable and intuitive permission settings.
- Consider setting your umask in your shell configuration file (like `.bashrc` or `.bash_profile`) to ensure consistent permissions across sessions.
- Be cautious when setting a very permissive umask (like `000`), as it can lead to security vulnerabilities by allowing unrestricted access to files.