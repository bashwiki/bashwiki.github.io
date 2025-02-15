# [리눅스] Bash hash 사용법

## Overview
The `hash` command in Bash is used to manage the command hash table, which stores the locations of commands that have been executed. This helps to speed up command execution by avoiding the need to search for the command in the file system each time it is called. The primary purpose of the `hash` command is to provide a way to view and manipulate the cached locations of commands, ensuring efficient command lookup.

## Usage
The basic syntax of the `hash` command is as follows:

```bash
hash [-r] [-p pathname] [name ...]
```

### Common Options:
- `-r`: This option clears the entire hash table, forcing Bash to rehash all commands the next time they are executed.
- `-p pathname`: This option allows you to specify a pathname for a command, which will be added to the hash table.
- `name`: You can specify one or more command names to display their hashed locations.

## Examples

### Example 1: Displaying the Hash Table
To display the current contents of the hash table, simply run:

```bash
hash
```

This will list all the commands that have been hashed along with their corresponding paths.

### Example 2: Adding a Command to the Hash Table
If you want to add a specific command to the hash table, you can use the `-p` option. For example:

```bash
hash -p /usr/local/bin/mycommand mycommand
```

This command adds `mycommand` to the hash table with the specified path `/usr/local/bin/mycommand`.

## Tips
- Use `hash -r` if you have made changes to your PATH or installed new software and want to refresh the hash table.
- Regularly check the hash table with `hash` to ensure that commands are pointing to the correct locations, especially after system updates or modifications.
- Remember that the hash table is session-specific; if you start a new terminal session, the hash table will be empty until commands are executed again.

By utilizing the `hash` command effectively, you can enhance your command-line efficiency and streamline your workflow in Bash.