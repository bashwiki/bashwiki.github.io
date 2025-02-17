# [Linux] Bash lspci Uso: Listar dispositivos PCI

## Overview
The `lspci` command is used in Linux to display information about all PCI (Peripheral Component Interconnect) devices on the system. This includes details about graphics cards, network adapters, and other hardware components connected via the PCI bus.

## Usage
The basic syntax of the `lspci` command is as follows:

```bash
lspci [options] [arguments]
```

## Common Options
- `-v`: Verbose output. Provides more detailed information about each device.
- `-vv`: Even more verbose output, showing additional details.
- `-k`: Show kernel driver information for each device.
- `-n`: Show numeric IDs instead of names for devices.
- `-s <slot>`: Display information for a specific device identified by its slot number.
- `-t`: Display the devices in a tree format.

## Common Examples
To list all PCI devices:
```bash
lspci
```

To get detailed information about each device:
```bash
lspci -v
```

To show kernel driver information:
```bash
lspci -k
```

To display numeric IDs for devices:
```bash
lspci -n
```

To view a specific device by its slot number (for example, `00:1f.0`):
```bash
lspci -s 00:1f.0
```

To display the devices in a tree format:
```bash
lspci -t
```

## Tips
- Use `lspci | less` to scroll through the output if you have many devices.
- Combine options for more specific output, like `lspci -vv -k` to get verbose information along with driver details.
- If you need to search for a specific device, you can pipe the output to `grep`, for example: `lspci | grep -i network` to find network devices.