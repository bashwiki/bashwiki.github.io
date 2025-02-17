# [Linux] Bash dmesg Uso equivalente: Display kernel messages

## Overview
The `dmesg` command is used to print or control the kernel ring buffer, which contains messages related to the system's hardware and drivers. It is particularly useful for diagnosing hardware issues or monitoring system events during boot.

## Usage
The basic syntax of the `dmesg` command is as follows:

```bash
dmesg [options] [arguments]
```

## Common Options
- `-C` : Clear the ring buffer.
- `-c` : Clear the ring buffer after printing its contents.
- `-n level` : Set the level of messages to be printed.
- `-f facility` : Print messages from a specific facility.
- `-T` : Print human-readable timestamps.

## Common Examples
- **Display all kernel messages:**
  ```bash
  dmesg
  ```

- **Clear the kernel ring buffer:**
  ```bash
  dmesg -C
  ```

- **Display messages with human-readable timestamps:**
  ```bash
  dmesg -T
  ```

- **Filter messages by a specific level (e.g., warning and above):**
  ```bash
  dmesg -n 4
  ```

- **Display messages related to a specific facility (e.g., kernel):**
  ```bash
  dmesg -f kernel
  ```

## Tips
- Use `dmesg | less` to scroll through the output easily.
- Combine `dmesg` with `grep` to search for specific keywords, like this:
  ```bash
  dmesg | grep error
  ```
- Regularly check `dmesg` after system boot to catch any hardware-related issues early.