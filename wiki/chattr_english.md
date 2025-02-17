# [Linux] Bash chattr Uso: Change file attributes on a Linux filesystem

## Overview
The `chattr` command in Linux is used to change file attributes on a filesystem. It allows users to set or remove certain attributes that can affect how files are accessed or modified, providing an additional layer of security and control over file management.

## Usage
The basic syntax of the `chattr` command is as follows:

```bash
chattr [options] [arguments]
```

## Common Options
- `+a`: Append-only. Files can only be opened in append mode for writing.
- `+i`: Immutable. The file cannot be modified, deleted, or renamed.
- `-a`: Remove append-only attribute.
- `-i`: Remove immutable attribute.
- `+e`: Allow the file to be used for extents (for filesystems that support it).
- `-e`: Remove extent support.

## Common Examples
1. **Set a file as immutable:**
   ```bash
   chattr +i myfile.txt
   ```
   This command makes `myfile.txt` immutable, preventing any changes to it.

2. **Remove the immutable attribute:**
   ```bash
   chattr -i myfile.txt
   ```
   This command allows modifications to `myfile.txt` again.

3. **Set a file to append-only:**
   ```bash
   chattr +a mylogfile.log
   ```
   This command allows `mylogfile.log` to be opened only in append mode.

4. **Check current attributes of a file:**
   ```bash
   lsattr myfile.txt
   ```
   This command displays the current attributes of `myfile.txt`.

5. **Set multiple attributes at once:**
   ```bash
   chattr +i +a myfile.txt
   ```
   This command makes `myfile.txt` both immutable and append-only.

## Tips
- Use `lsattr` to check the current attributes of files before making changes.
- Be cautious when setting the immutable attribute, as it can prevent all modifications, including deletions.
- Consider using these attributes on critical system files to prevent accidental changes or deletions.