# [Linux] Bash who uso equivalente: Display logged-in users

## Overview
The `who` command in Bash is used to display a list of users currently logged into the system. It provides information such as the username, terminal, login time, and originating IP address or hostname.

## Usage
The basic syntax of the `who` command is as follows:

```bash
who [options] [arguments]
```

## Common Options
- `-a`: Show all available information, including users logged in and their idle time.
- `-b`: Display the last system boot time.
- `-q`: Show only the usernames and the number of users logged in.
- `-H`: Print the column headers for the output.

## Common Examples

1. **Basic Usage**: Display all users currently logged in.
   ```bash
   who
   ```

2. **Show All Information**: Display detailed information about logged-in users.
   ```bash
   who -a
   ```

3. **Last Boot Time**: Show the last time the system was booted.
   ```bash
   who -b
   ```

4. **Count of Logged-in Users**: Display just the usernames and the count of users logged in.
   ```bash
   who -q
   ```

5. **With Headers**: Display logged-in users with column headers.
   ```bash
   who -H
   ```

## Tips
- Use `who -H` for a clearer output when you need to present the information.
- Combine `who` with other commands like `grep` to filter results for specific users.
- Regularly check who is logged in, especially on shared systems, for security purposes.