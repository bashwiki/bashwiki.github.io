# [리눅스] Bash ethtool 사용법

## Overview
The `ethtool` command is a Linux utility used for querying and controlling network device driver and hardware settings. Its primary purpose is to provide information about Ethernet devices, such as link status, speed, duplex settings, and other parameters. Additionally, `ethtool` allows users to configure various aspects of network interfaces, making it a vital tool for network administrators and engineers.

## Usage
The basic syntax of the `ethtool` command is as follows:

```bash
ethtool [options] <interface>
```

Where `<interface>` is the name of the network interface you want to query or configure (e.g., `eth0`, `enp3s0`, etc.).

### Common Options
- `-i`, `--driver`: Display driver information for the specified interface.
- `-s`, `--set`: Set various parameters for the specified interface. This option requires additional arguments.
- `-p`, `--identify`: Blink the LED on the specified interface for a specified duration.
- `-S`, `--statistics`: Display statistics for the specified interface.
- `-a`, `--show-advertised`: Show the advertised link modes for the specified interface.
- `-d`, `--show-diagnostics`: Show diagnostic information for the specified interface.

## Examples

### Example 1: Displaying Interface Information
To display detailed information about a network interface, you can use the following command:

```bash
ethtool eth0
```

This command will provide information such as speed, duplex mode, link status, and supported features of the `eth0` interface.

### Example 2: Changing Speed and Duplex Settings
To change the speed and duplex settings of a network interface, you can use the `-s` option. For example, to set the `eth0` interface to 100 Mbps full duplex, you would run:

```bash
ethtool -s eth0 speed 100 duplex full
```

This command configures the `eth0` interface to operate at 100 Mbps with full duplex communication.

## Tips
- Always check the current settings of your network interface before making changes to avoid misconfiguration.
- Use the `-S` option to monitor statistics for troubleshooting network issues.
- When changing settings, ensure that the network device supports the desired configurations to prevent connectivity problems.
- For persistent changes, consider modifying network configuration files or using network management tools, as changes made with `ethtool` may not survive a reboot.