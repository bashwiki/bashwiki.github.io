# [Linux] Bash uname用法: 显示系统信息

## Overview
The `uname` command is used in Unix-like operating systems to display system information. It provides details about the operating system, kernel version, and hardware architecture, making it a useful tool for system administrators and users who need to gather information about their system.

## Usage
The basic syntax of the `uname` command is as follows:

```
uname [options] [arguments]
```

## Common Options
- `-a`: Displays all available system information.
- `-s`: Shows the kernel name.
- `-n`: Displays the network node hostname.
- `-r`: Shows the kernel release.
- `-v`: Displays the kernel version.
- `-m`: Shows the machine hardware name.
- `-p`: Displays the processor type (if available).
- `-i`: Shows the hardware platform (if available).
- `-o`: Displays the operating system name.

## Common Examples
Here are some practical examples of using the `uname` command:

1. **Display all system information:**
   ```bash
   uname -a
   ```

2. **Show the kernel name:**
   ```bash
   uname -s
   ```

3. **Display the kernel release:**
   ```bash
   uname -r
   ```

4. **Get the machine hardware name:**
   ```bash
   uname -m
   ```

5. **Show the operating system name:**
   ```bash
   uname -o
   ```

## Tips
- Use `uname -a` for a quick overview of your system's information in one command.
- Combine `uname` with other commands, like `grep`, to filter specific information.
- Familiarize yourself with the options to better understand your system's architecture and configuration.