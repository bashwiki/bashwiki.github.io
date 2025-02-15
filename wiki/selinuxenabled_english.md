# [리눅스] Bash selinuxenabled 사용법

## Overview
The `selinuxenabled` command is a utility in Linux that checks whether SELinux (Security-Enhanced Linux) is enabled on the system. SELinux is a security architecture for Linux that provides a mechanism for supporting access control security policies. The primary purpose of `selinuxenabled` is to return an exit status indicating the status of SELinux, which can be useful in scripts and system administration tasks.

## Usage
The basic syntax of the `selinuxenabled` command is as follows:

```bash
selinuxenabled
```

This command does not take any options or arguments. It simply checks the SELinux status and returns an exit code:

- **Exit Code 0**: SELinux is enabled.
- **Exit Code 1**: SELinux is not enabled.

## Examples

### Example 1: Check if SELinux is enabled
You can use the `selinuxenabled` command in a terminal to check if SELinux is active:

```bash
selinuxenabled
```

If SELinux is enabled, you will see no output, and the command will return an exit status of 0. You can check the exit status by running:

```bash
echo $?
```

If the output is `0`, SELinux is enabled. If it is `1`, SELinux is not enabled.

### Example 2: Using in a script
You can incorporate `selinuxenabled` in a shell script to conditionally execute commands based on the SELinux status:

```bash
#!/bin/bash

if selinuxenabled; then
    echo "SELinux is enabled."
    # Additional commands for when SELinux is enabled
else
    echo "SELinux is not enabled."
    # Additional commands for when SELinux is not enabled
fi
```

## Tips
- Use `selinuxenabled` in scripts to ensure that your commands are executed only when SELinux is enabled, which can help in maintaining security compliance.
- Combine `selinuxenabled` with other commands to create more complex logic in your scripts, such as logging or alerting when SELinux is not enabled.
- Always check the exit status immediately after running `selinuxenabled` to ensure you are capturing the correct state of SELinux.