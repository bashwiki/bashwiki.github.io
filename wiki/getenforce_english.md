# [리눅스] Bash getenforce 사용법

## Overview
The `getenforce` command is a utility in Linux that is used to retrieve the current mode of SELinux (Security-Enhanced Linux). SELinux is a security architecture for Linux that provides a mechanism for supporting access control security policies. The `getenforce` command helps system administrators and developers quickly check whether SELinux is enforcing, permissive, or disabled, which is crucial for understanding the security context of the system.

## Usage
The basic syntax of the `getenforce` command is as follows:

```bash
getenforce
```

This command does not require any additional options or arguments. It simply outputs the current SELinux mode.

### Common Output Values
- **Enforcing**: SELinux security policy is enforced. Access is denied based on the policy.
- **Permissive**: SELinux is not enforcing the policy but will log actions that would have been denied if it were enforcing.
- **Disabled**: SELinux is turned off entirely.

## Examples

### Example 1: Check SELinux Status
To check the current status of SELinux, simply run:

```bash
getenforce
```

**Output:**
```
Enforcing
```

This output indicates that SELinux is currently enforcing its security policies.

### Example 2: Use in a Script
You can use `getenforce` in a script to make decisions based on the SELinux status. For example:

```bash
#!/bin/bash

if [ "$(getenforce)" == "Enforcing" ]; then
    echo "SELinux is enforcing. Proceed with caution."
else
    echo "SELinux is not enforcing. You may have more flexibility."
fi
```

This script checks the SELinux mode and provides a message based on its status.

## Tips
- Regularly check the SELinux status on production systems to ensure that security policies are being enforced as intended.
- Use `getenforce` in scripts to automate security checks and ensure compliance with security policies.
- If you need to change the SELinux mode, use the `setenforce` command, but be cautious and understand the implications of changing SELinux settings.

By understanding and utilizing the `getenforce` command, you can effectively monitor and manage the security posture of your Linux systems.