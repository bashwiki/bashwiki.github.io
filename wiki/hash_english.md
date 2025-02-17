# [Linux] Bash hash uso: Manage command hash table

## Overview
The `hash` command in Bash is used to manage the hash table of commands. When you execute a command, Bash remembers its location in the filesystem to speed up future executions. The `hash` command allows you to view, add, or remove entries from this hash table.

## Usage
The basic syntax of the `hash` command is as follows:

```bash
hash [options] [arguments]
```

## Common Options
- `-r`: Clears the entire hash table, forcing Bash to rehash the commands the next time they are called.
- `-p`: Specifies a command path to be hashed.
- `-l`: Lists the contents of the hash table.

## Common Examples

### Listing the Hash Table
To view the current contents of the hash table, simply use:

```bash
hash
```

### Clearing the Hash Table
If you want to clear the hash table and force Bash to rehash commands, use:

```bash
hash -r
```

### Hashing a Specific Command
To add a specific command to the hash table, you can specify its path:

```bash
hash -p /usr/local/bin/mycommand mycommand
```

### Listing Hash Table with Details
To see the details of the hash table, including the command paths, use:

```bash
hash -l
```

## Tips
- Use `hash -r` if you have made changes to your PATH or installed new software and want to ensure that Bash uses the updated command locations.
- Regularly check the hash table with `hash` to see which commands are cached, especially if you are troubleshooting command execution issues.
- Remember that the hash table is session-specific; it will reset when you start a new terminal session.