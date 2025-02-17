# [Linux] Bash groupmod Usage: Modify existing groups

## Overview
The `groupmod` command in Bash is used to modify existing groups on a Linux system. It allows administrators to change the group name, group ID, and other attributes of a specified group.

## Usage
The basic syntax of the `groupmod` command is as follows:

```bash
groupmod [options] [arguments]
```

## Common Options
- `-n, --new-name NEW_GROUP`: Change the name of the group to `NEW_GROUP`.
- `-g, --gid GID`: Change the group ID to `GID`.
- `-h, --help`: Display help information about the command.
- `-o, --non-unique`: Allow the group ID to be non-unique (not recommended).

## Common Examples

1. **Change the name of a group:**
   To rename a group from `oldgroup` to `newgroup`, use:
   ```bash
   groupmod -n newgroup oldgroup
   ```

2. **Change the group ID:**
   To change the group ID of `mygroup` to `1001`, use:
   ```bash
   groupmod -g 1001 mygroup
   ```

3. **Change both the name and ID of a group:**
   To rename `examplegroup` to `newexample` and change its ID to `2002`, use:
   ```bash
   groupmod -n newexample -g 2002 examplegroup
   ```

4. **Display help information:**
   To see the help information for `groupmod`, simply run:
   ```bash
   groupmod --help
   ```

## Tips
- Always ensure that no users are currently using the group you want to modify, as this may cause issues.
- Use the `-o` option with caution, as allowing non-unique group IDs can lead to conflicts.
- After modifying a group, verify the changes by checking the `/etc/group` file or using the `getent group` command.