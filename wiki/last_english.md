# [Linux] Bash last command: Display login history

## Overview
The `last` command in Bash is used to display a list of the most recent logins to the system. It reads from the `/var/log/wtmp` file, which records all logins and logouts, allowing users to track who accessed the system and when.

## Usage
The basic syntax of the `last` command is as follows:

```bash
last [options] [username]
```

## Common Options
- `-a`: Show the hostname on the last line.
- `-n [number]`: Limit the output to the specified number of entries.
- `-x`: Show system shutdown entries and run level changes.
- `-R`: Suppress the display of the hostname.
- `-F`: Display the full login and logout times.

## Common Examples

1. **Display all login history:**
   ```bash
   last
   ```

2. **Limit the output to the last 5 logins:**
   ```bash
   last -n 5
   ```

3. **Show login history for a specific user:**
   ```bash
   last username
   ```

4. **Include hostname in the output:**
   ```bash
   last -a
   ```

5. **Display full login and logout times:**
   ```bash
   last -F
   ```

6. **Show login history including system shutdowns:**
   ```bash
   last -x
   ```

## Tips
- Use `last -n 10` to quickly check the last 10 login attempts, which is useful for a quick security review.
- Combine options for more tailored output, such as `last -a -n 5` to see the last 5 logins with hostnames.
- Regularly check the login history to monitor for any unauthorized access attempts to the system.