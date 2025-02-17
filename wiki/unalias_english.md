# [Linux] Bash unalias uso: Remove aliases in the current shell session

## Overview
The `unalias` command in Bash is used to remove existing aliases from the current shell session. Aliases are shortcuts that allow users to create custom commands or modify existing ones for convenience. When you no longer need an alias, `unalias` helps to clean up your environment.

## Usage
The basic syntax of the `unalias` command is as follows:

```bash
unalias [options] [arguments]
```

## Common Options
- `-a`: Remove all aliases defined in the current shell session.
- `-m`: Remove aliases that match a specified pattern.

## Common Examples

### Remove a Specific Alias
To remove a specific alias, use the alias name as an argument:

```bash
unalias ll
```

### Remove Multiple Aliases
You can remove multiple aliases by listing them:

```bash
unalias ll grep
```

### Remove All Aliases
To remove all aliases at once, use the `-a` option:

```bash
unalias -a
```

### Remove Aliases Matching a Pattern
To remove aliases that match a certain pattern, use the `-m` option:

```bash
unalias -m 'g*'
```

## Tips
- Always check your current aliases with the `alias` command before removing them to avoid accidentally deleting something important.
- Consider using `unalias -a` with caution, as it will remove all aliases and may disrupt your workflow.
- If you want to make sure an alias is removed every time you start a new session, consider adding the `unalias` command to your shell's configuration file (like `.bashrc` or `.bash_profile`).