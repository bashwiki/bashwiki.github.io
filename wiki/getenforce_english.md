# [Linux] Bash getenforce用法: Check SELinux status

## Overview
The `getenforce` command is used to check the current mode of SELinux (Security-Enhanced Linux) on a system. It returns the status of SELinux, which can be either Enforcing, Permissive, or Disabled. This command is essential for system administrators to understand the security context of their Linux environment.

## Usage
The basic syntax of the `getenforce` command is as follows:

```bash
getenforce [options]
```

## Common Options
The `getenforce` command has no options; it simply returns the current SELinux mode. 

## Common Examples
Here are some practical examples of using the `getenforce` command:

1. **Check SELinux Status**
   To check the current status of SELinux, simply run:
   ```bash
   getenforce
   ```

2. **Using in a Script**
   You can use `getenforce` in a script to take action based on the SELinux status. For example:
   ```bash
   if [ "$(getenforce)" == "Enforcing" ]; then
       echo "SELinux is in Enforcing mode."
   else
       echo "SELinux is not in Enforcing mode."
   fi
   ```

3. **Redirecting Output**
   You can redirect the output to a file for logging purposes:
   ```bash
   getenforce > selinux_status.log
   ```

## Tips
- Always check the SELinux status after making changes to the system configuration to ensure that security policies are being enforced as expected.
- Use `getenforce` in combination with other SELinux management commands like `setenforce` to manage SELinux modes effectively.
- Consider incorporating `getenforce` into your monitoring scripts to alert you if the SELinux status changes unexpectedly.