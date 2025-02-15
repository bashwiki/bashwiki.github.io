# [리눅스] Bash uname 사용법

## Overview
The `uname` command in Bash is used to display system information. Its primary purpose is to provide details about the operating system and the hardware on which it is running. This can be particularly useful for developers and engineers who need to gather system specifications or troubleshoot compatibility issues.

## Usage
The basic syntax of the `uname` command is as follows:

```bash
uname [OPTION...]
```

### Common Options
- `-a`: Displays all available system information, including the kernel name, network node hostname, kernel release, kernel version, machine hardware name, processor type, hardware platform, and operating system.
- `-s`: Outputs the kernel name (default behavior).
- `-n`: Shows the network node hostname.
- `-r`: Displays the kernel release.
- `-v`: Provides the kernel version.
- `-m`: Outputs the machine hardware name.
- `-p`: Displays the processor type (if known).
- `-i`: Shows the hardware platform (if known).
- `-o`: Outputs the operating system name.

## Examples
### Example 1: Display All System Information
To view all available information about the system, you can use the `-a` option:

```bash
uname -a
```
**Output Example:**
```
Linux myhostname 5.4.0-42-generic #46-Ubuntu SMP Fri Sep 4 00:00:00 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

### Example 2: Display Kernel Version
If you are only interested in the kernel version, you can use the `-r` option:

```bash
uname -r
```
**Output Example:**
```
5.4.0-42-generic
```

## Tips
- Use `uname -a` for a comprehensive overview of your system, especially when diagnosing issues or preparing for software installation.
- Combine `uname` with other commands like `grep` to filter specific information. For example, to check if you are running a 64-bit kernel, you can use:
  
  ```bash
  uname -m | grep x86_64
  ```
- Remember that the output of `uname` can vary depending on the system architecture and the operating system in use, so always verify the information in the context of your specific environment.