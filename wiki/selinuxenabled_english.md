# [Linux] Bash selinuxenabled Uso: Check SELinux status

## Overview
The `selinuxenabled` command is a simple utility that checks whether SELinux (Security-Enhanced Linux) is enabled on the system. It returns an exit status of 0 if SELinux is enabled and 1 if it is not. This command is useful for scripts and system administration tasks where you need to verify the SELinux status.

## Usage
The basic syntax of the `selinuxenabled` command is as follows:

```bash
selinuxenabled [options]
```

## Common Options
The `selinuxenabled` command does not have any options. It is a straightforward command that simply checks the SELinux status.

## Common Examples

### Check if SELinux is enabled
To check if SELinux is enabled on your system, you can run:

```bash
selinuxenabled
```

If SELinux is enabled, the command will exit with a status of 0. You can check the exit status using:

```bash
echo $?
```

### Using in a script
You can use `selinuxenabled` in a shell script to perform actions based on the SELinux status. For example:

```bash
if selinuxenabled; then
    echo "SELinux is enabled."
else
    echo "SELinux is not enabled."
fi
```

### Conditional execution
You can also use `selinuxenabled` in a one-liner for conditional execution:

```bash
selinuxenabled && echo "SELinux is enabled." || echo "SELinux is not enabled."
```

## Tips
- Use `selinuxenabled` in scripts to ensure that your script behaves correctly depending on the SELinux status.
- Remember that the exit status can be checked using `echo $?` immediately after running the command.
- For more detailed SELinux status information, consider using the `sestatus` command, which provides additional context and configuration details.