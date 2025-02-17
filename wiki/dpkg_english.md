# [Linux] Bash dpkg Uso: Manage Debian packages

## Overview
The `dpkg` command is a low-level package manager for Debian-based systems. It is used to install, remove, and manage `.deb` packages, which are the standard package format for Debian and its derivatives, such as Ubuntu. Unlike higher-level package managers like `apt`, `dpkg` does not resolve dependencies automatically.

## Usage
The basic syntax of the `dpkg` command is as follows:

```bash
dpkg [options] [arguments]
```

## Common Options
- `-i`, `--install`: Install a package from a `.deb` file.
- `-r`, `--remove`: Remove an installed package.
- `-P`, `--purge`: Remove a package and its configuration files.
- `-l`, `--list`: List all installed packages.
- `-s`, `--status`: Show the status of a package.
- `-L`, `--listfiles`: List files installed by a package.
- `-S`, `--search`: Search for a package that owns a specific file.

## Common Examples
Here are some practical examples of using the `dpkg` command:

### Install a Package
To install a package from a `.deb` file:
```bash
dpkg -i package_name.deb
```

### Remove a Package
To remove an installed package:
```bash
dpkg -r package_name
```

### Purge a Package
To remove a package along with its configuration files:
```bash
dpkg -P package_name
```

### List Installed Packages
To list all installed packages on the system:
```bash
dpkg -l
```

### Check Package Status
To check the status of a specific package:
```bash
dpkg -s package_name
```

### List Files of a Package
To list all files installed by a specific package:
```bash
dpkg -L package_name
```

### Search for a Package
To find which package owns a specific file:
```bash
dpkg -S /path/to/file
```

## Tips
- Always check for dependencies before installing a package with `dpkg`, as it does not handle them automatically.
- Use `apt` or `apt-get` for higher-level package management tasks that require dependency resolution.
- When removing packages, consider using the `--purge` option if you want to clean up configuration files as well.