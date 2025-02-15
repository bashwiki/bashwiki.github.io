# [리눅스] Bash systemctl 사용법

## Overview
The `systemctl` command is a fundamental utility in Linux systems that use systemd as their init system. Its primary purpose is to control the systemd system and service manager, allowing users to manage services, check their status, and configure system states. With `systemctl`, you can start, stop, restart, enable, or disable services, as well as manage system states such as rebooting or shutting down the system.

## Usage
The basic syntax of the `systemctl` command is as follows:

```bash
systemctl [OPTIONS] COMMAND [NAME]
```

### Common Options
- `start`: Starts a specified service.
- `stop`: Stops a specified service.
- `restart`: Restarts a specified service.
- `reload`: Reloads the configuration of a specified service without interrupting its operation.
- `status`: Displays the status of a specified service.
- `enable`: Enables a service to start automatically at boot.
- `disable`: Prevents a service from starting automatically at boot.
- `list-units`: Lists all loaded units (services, sockets, etc.).
- `is-active`: Checks if a specified service is currently active.

## Examples
### Example 1: Starting a Service
To start the Apache web server service, you would use the following command:

```bash
sudo systemctl start apache2
```

### Example 2: Checking the Status of a Service
To check the status of the same Apache service, you can run:

```bash
sudo systemctl status apache2
```

This command will provide detailed information about the service, including whether it is active, any recent logs, and its process ID.

## Tips
- Always use `sudo` with `systemctl` commands that require administrative privileges, such as starting or stopping services.
- Use `systemctl list-units --type=service` to get a quick overview of all active services and their statuses.
- To ensure a service starts on boot, remember to use the `enable` command after starting it.
- For troubleshooting, the `status` command is invaluable as it provides logs and error messages that can help diagnose issues with services.
- Consider using `systemctl daemon-reload` after making changes to service unit files to ensure that systemd recognizes the changes. 

By mastering `systemctl`, you can effectively manage services and system states in a Linux environment, enhancing your ability to maintain and troubleshoot systems.