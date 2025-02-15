# [리눅스] Bash w 사용법

## Overview
The `w` command in Bash is a utility that displays information about the users currently logged into the system and their activity. It provides a summary of who is logged in, what they are doing, and how long they have been idle. This command is particularly useful for system administrators and developers who need to monitor user activity on a multi-user system.

## Usage
The basic syntax of the `w` command is as follows:

```bash
w [options] [user]
```

### Common Options
- `-h`: Suppresses the header line that normally appears at the top of the output.
- `-s`: Displays the output in a short format, omitting the idle time and other details.
- `-u`: Displays the user name of the logged-in users (this is the default behavior).
- `-f`: Displays the full login name of the users.

## Examples
### Example 1: Basic Usage
To display a list of currently logged-in users along with their activity, simply run:

```bash
w
```

This command will output details such as the username, terminal, login time, idle time, JCPU (time used by all processes attached to the terminal), PCPU (time used by the current process), and the command being executed.

### Example 2: Using Options
To view the logged-in users without the header and in a short format, you can use:

```bash
w -hs
```

This will provide a cleaner output, focusing on the essential information about the users currently logged in.

## Tips
- Use the `w` command regularly to monitor user activity, especially on shared systems, to ensure that resources are being used efficiently.
- Combine `w` with other commands like `grep` to filter results for specific users. For example, to check if a user named "alice" is logged in, you can run:

```bash
w | grep alice
```
- Familiarize yourself with the output format of `w` to quickly interpret user activity and system load, which can help in troubleshooting performance issues.