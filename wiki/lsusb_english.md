# [리눅스] Bash lsusb 사용법

## Overview
The `lsusb` command is a utility in Linux that displays information about USB (Universal Serial Bus) devices connected to the system. It provides a list of all USB devices, including their vendor and product IDs, class codes, and other relevant details. This command is particularly useful for engineers and developers who need to troubleshoot USB device issues or gather information about connected hardware.

## Usage
The basic syntax of the `lsusb` command is as follows:

```bash
lsusb [options]
```

### Common Options
- `-v`: Verbose output. This option provides detailed information about each USB device.
- `-t`: Displays the USB device hierarchy in a tree format, which can help visualize the connections between devices.
- `-s <bus>:<device>`: Show information for a specific USB device identified by its bus and device number.
- `-d <vendor>:<product>`: Show information for a specific USB device identified by its vendor and product ID.

## Examples

### Example 1: Basic Usage
To list all USB devices connected to your system, simply run:

```bash
lsusb
```

This command will output a list of USB devices along with their respective IDs and descriptions.

### Example 2: Verbose Output
To get detailed information about all connected USB devices, use the verbose option:

```bash
lsusb -v
```

This command will provide extensive details about each device, including configurations, interfaces, and endpoint descriptors.

## Tips
- Use the `-t` option to visualize the USB device hierarchy, which can be particularly helpful when troubleshooting complex setups with multiple connected devices.
- Combine `lsusb` with other commands like `grep` to filter results. For example, if you are looking for a specific device, you can run:

  ```bash
  lsusb | grep "DeviceName"
  ```

- Regularly check for updates to the `lsusb` command, as newer versions may include additional features or improvements in device detection.