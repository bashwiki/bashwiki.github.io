# [리눅스] Bash last 사용법

## Overview
The `last` command in Bash is used to display a list of the most recent login sessions for users on the system. It reads from the `/var/log/wtmp` file, which records all logins and logouts, providing a historical record of user activity. This command is particularly useful for system administrators and developers who need to monitor user access and troubleshoot login issues.

## Usage
The basic syntax of the `last` command is as follows:

```bash
last [options] [username]
```

### Common Options
- `-n [number]`: Limits the output to the specified number of entries. For example, `last -n 5` will show the last 5 login sessions.
- `-R`: Suppresses the display of the hostname in the output.
- `-F`: Displays the full login and logout times, including the year.
- `-x`: Shows system shutdown entries and run level changes in addition to user logins.

## Examples
1. **Display the last 10 login sessions:**
   ```bash
   last -n 10
   ```
   This command will show the last 10 users who logged into the system, along with their login times and durations.

2. **Show login sessions for a specific user:**
   ```bash
   last username
   ```
   Replace `username` with the actual username to see the login history for that specific user.

## Tips
- Use the `-F` option to get a more detailed view of login times, which can be helpful for auditing purposes.
- Combine the `-n` option with `-x` to get a concise view of both user logins and system events, which can aid in understanding system usage patterns.
- Regularly check the output of `last` to monitor unauthorized access attempts or unusual login times, which can indicate potential security issues.