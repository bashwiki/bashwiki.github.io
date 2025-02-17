# [Linux] Bash lsusb Usage: List USB devices

## Overview
The `lsusb` command is used in Linux to display information about USB (Universal Serial Bus) devices connected to the system. It provides details such as the device ID, vendor ID, and device class, making it a useful tool for troubleshooting and managing USB hardware.

## Usage
The basic syntax of the `lsusb` command is as follows:

```bash
lsusb [options] [arguments]
```

## Common Options
- `-v`: Verbose output. Displays detailed information about each USB device.
- `-t`: Displays the USB device hierarchy in a tree format.
- `-s <bus>:<device>`: Show only the specified device on the given bus.
- `-d <vendor>:<product>`: Show only devices with the specified vendor and product ID.
- `-h`: Display help information about the command and its options.

## Common Examples
Here are some practical examples of using the `lsusb` command:

1. **List all USB devices:**
   ```bash
   lsusb
   ```

2. **Get detailed information about all USB devices:**
   ```bash
   lsusb -v
   ```

3. **Display USB device hierarchy:**
   ```bash
   lsusb -t
   ```

4. **Show information for a specific device (e.g., bus 001, device 002):**
   ```bash
   lsusb -s 001:002
   ```

5. **Filter devices by vendor and product ID (e.g., vendor ID 1234 and product ID 5678):**
   ```bash
   lsusb -d 1234:5678
   ```

## Tips
- Use `lsusb -v` for a comprehensive view of device capabilities, especially useful for debugging.
- Combine `lsusb` with other commands like `grep` to filter results based on specific criteria.
- Regularly check connected devices with `lsusb` when troubleshooting USB-related issues to ensure proper recognition by the system.