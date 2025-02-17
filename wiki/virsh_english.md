# [Linux] Bash virsh uso: Manage virtual machines

## Overview
The `virsh` command is a command-line interface for managing virtual machines through the libvirt API. It allows users to create, manage, and interact with virtual machines and their resources, making it an essential tool for virtualization on Linux systems.

## Usage
The basic syntax of the `virsh` command is as follows:

```bash
virsh [options] [arguments]
```

## Common Options
- `list`: Displays a list of currently running virtual machines.
- `start <domain>`: Starts a specified virtual machine.
- `shutdown <domain>`: Gracefully shuts down a specified virtual machine.
- `destroy <domain>`: Forcefully stops a specified virtual machine.
- `create <xml-file>`: Creates a new virtual machine from an XML configuration file.
- `define <xml-file>`: Defines a new virtual machine without starting it.

## Common Examples
Here are some practical examples of using the `virsh` command:

1. **List all running virtual machines:**
   ```bash
   virsh list
   ```

2. **Start a virtual machine named "myvm":**
   ```bash
   virsh start myvm
   ```

3. **Shut down a virtual machine named "myvm":**
   ```bash
   virsh shutdown myvm
   ```

4. **Forcefully stop a virtual machine named "myvm":**
   ```bash
   virsh destroy myvm
   ```

5. **Create a new virtual machine from an XML file called "myvm.xml":**
   ```bash
   virsh create myvm.xml
   ```

6. **Define a new virtual machine from an XML file without starting it:**
   ```bash
   virsh define myvm.xml
   ```

## Tips
- Always use `virsh list --all` to see both running and shut down virtual machines.
- Use `virsh dominfo <domain>` to get detailed information about a specific virtual machine.
- Consider using `virsh console <domain>` to access the console of a running virtual machine directly.
- Regularly back up your XML configuration files to avoid losing your virtual machine settings.