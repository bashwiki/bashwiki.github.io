# [리눅스] Bash virsh 사용법

## Overview
The `virsh` command is a command-line interface for managing virtual machines (VMs) through the libvirt virtualization API. It allows users to create, manage, and monitor virtualized environments, supporting various hypervisors such as KVM, QEMU, and Xen. `virsh` provides a wide range of functionalities, making it an essential tool for system administrators and developers working with virtualization technologies.

## Usage
The basic syntax for the `virsh` command is as follows:

```
virsh [options] <command> [<args>]
```

### Common Options
- `--help`: Displays help information for the command.
- `--version`: Shows the version of the `virsh` tool.
- `-c <URI>`: Connects to a specific hypervisor URI. If not specified, it defaults to the local hypervisor.
- `--quiet`: Suppresses output, useful for scripting.

### Commands
`virsh` supports a variety of commands, including but not limited to:
- `list`: Lists running VMs.
- `start <domain>`: Starts a specified VM.
- `shutdown <domain>`: Gracefully shuts down a specified VM.
- `destroy <domain>`: Forces a specified VM to stop.
- `create <xml-file>`: Creates and starts a VM from an XML definition file.

## Examples

### Example 1: Listing Running Virtual Machines
To list all currently running virtual machines, you can use the following command:

```bash
virsh list
```

This command will display a table with the IDs, names, and states of all active VMs.

### Example 2: Starting a Virtual Machine
To start a virtual machine named "my-vm", you can execute:

```bash
virsh start my-vm
```

This command will initiate the specified VM, allowing it to begin running.

## Tips
- Always ensure you have the necessary permissions to manage VMs, as some commands may require elevated privileges.
- Use `virsh --help` to get a comprehensive list of available commands and options.
- For scripting purposes, consider using the `--quiet` option to minimize output and make parsing easier.
- Regularly check the status of your VMs using `virsh list --all` to monitor both running and shut down instances.
- When creating VMs, prepare a well-structured XML definition file to ensure all configurations are correctly set.