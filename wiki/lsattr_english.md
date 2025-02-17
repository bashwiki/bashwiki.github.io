# [Linux] Bash lsattr Usage: List file attributes

## Overview
The `lsattr` command in Linux is used to display the file attributes of files and directories in a specified directory. It provides information about the attributes that affect how files can be manipulated, such as whether they can be deleted or modified.

## Usage
The basic syntax of the `lsattr` command is as follows:

```bash
lsattr [options] [arguments]
```

## Common Options
- `-d`: List attributes of directories only.
- `-R`: Recursively list attributes of files in directories.
- `-a`: Include hidden files in the output.
- `-V`: Display version information.

## Common Examples

1. **List attributes of files in the current directory:**
   ```bash
   lsattr
   ```

2. **List attributes of a specific file:**
   ```bash
   lsattr filename.txt
   ```

3. **Recursively list attributes of all files in a directory:**
   ```bash
   lsattr -R /path/to/directory
   ```

4. **List attributes including hidden files:**
   ```bash
   lsattr -a
   ```

5. **List attributes of directories only:**
   ```bash
   lsattr -d /path/to/directory
   ```

## Tips
- Use `lsattr` in combination with `chattr` to modify file attributes if needed.
- Regularly check file attributes to ensure that important files are protected from accidental deletion or modification.
- Familiarize yourself with the various attributes that can be set using `chattr` to better understand the output of `lsattr`.