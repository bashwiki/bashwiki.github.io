# [Linux] Bash umask Uso: Controlando permisos de archivos por defecto

## Overview
The `umask` command in Bash is used to set default file permissions for newly created files and directories. It defines the permissions that will be masked (or removed) when a new file or directory is created, ensuring that they do not have more permissions than intended.

## Usage
The basic syntax of the `umask` command is as follows:

```bash
umask [options] [arguments]
```

## Common Options
- `-S`: Display the current umask value in symbolic notation.
- `-p`: Print the current umask value in a format that can be reused in scripts.

## Common Examples

1. **Check Current umask Value**
   To see the current umask setting, simply run:
   ```bash
   umask
   ```

2. **Set a New umask Value**
   To set a umask value of `027`, which allows the owner to read and write, the group to read, and no permissions for others:
   ```bash
   umask 027
   ```

3. **Set umask in Symbolic Notation**
   To set the umask using symbolic notation, which is more readable:
   ```bash
   umask u=rwx,g=rx,o=
   ```

4. **Display umask in Symbolic Format**
   To display the current umask in symbolic format:
   ```bash
   umask -S
   ```

5. **Set umask Temporarily**
   To temporarily change the umask for a single command:
   ```bash
   (umask 007; touch newfile)
   ```

## Tips
- Always check your current umask before setting a new one to avoid unintended permission issues.
- Consider setting a stricter umask in shared environments to enhance security.
- Remember that umask values are subtracted from the default permissions (666 for files and 777 for directories).
- You can add your umask settings to your shell's configuration file (like `~/.bashrc`) to make them persistent across sessions.