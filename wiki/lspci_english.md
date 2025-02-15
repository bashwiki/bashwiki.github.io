# [리눅스] Bash lspci 사용법

## Overview
The `lspci` command is a utility in Linux that displays information about all PCI (Peripheral Component Interconnect) devices on the system. It provides details such as the device's vendor, model, and other relevant attributes. This command is particularly useful for engineers and developers who need to troubleshoot hardware issues, gather system information, or verify the presence of specific hardware components.

## Usage
The basic syntax for the `lspci` command is as follows:

```bash
lspci [options]
```

### Common Options:
- `-v` or `--verbose`: Provides more detailed information about each device.
- `-vv`: Increases the verbosity level, providing even more detailed information.
- `-k` or `--kernel`: Shows the kernel driver in use for each device.
- `-n`: Displays numeric IDs instead of the human-readable names.
- `-s <slot>`: Displays information for a specific device identified by its slot number.
- `-t`: Displays the PCI device hierarchy in a tree format.

## Examples
1. **Basic Usage**: To list all PCI devices on your system, simply run:
   ```bash
   lspci
   ```

2. **Verbose Output**: To get detailed information about each PCI device, use the verbose option:
   ```bash
   lspci -v
   ```

3. **Kernel Driver Information**: To see which kernel driver is being used for each PCI device, you can use:
   ```bash
   lspci -k
   ```

## Tips
- When troubleshooting hardware issues, combining `lspci` with the `-v` and `-k` options can provide comprehensive insights into the devices and their associated drivers.
- If you are looking for a specific device, you can pipe the output to `grep` to filter results. For example, to find information about a network controller, you can use:
  ```bash
  lspci | grep -i network
  ```
- For a clearer view of the device hierarchy, consider using the `-t` option, which can help visualize the relationships between devices.

By utilizing the `lspci` command effectively, engineers and developers can gain valuable insights into the hardware components of their Linux systems.