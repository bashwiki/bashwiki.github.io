# [리눅스] Bash yum 사용법

## Overview
`yum` (Yellowdog Updater, Modified) is a package management utility for RPM (Red Hat Package Manager) based Linux distributions. It simplifies the process of managing software packages by automating the installation, updating, and removal of software. `yum` resolves dependencies automatically, ensuring that all required packages are installed or updated along with the requested software.

## Usage
The basic syntax of the `yum` command is as follows:

```
yum [options] <command> [package...]
```

### Common Options:
- `install`: Installs the specified package(s).
- `remove`: Uninstalls the specified package(s).
- `update`: Updates all packages to the latest version or a specific package if specified.
- `search`: Searches for a package by name or description.
- `info`: Displays detailed information about a package.
- `list`: Lists all available packages or installed packages.
- `clean`: Cleans up cached files to free up space.

## Examples

### Example 1: Installing a Package
To install a package, such as `httpd` (Apache web server), you would use the following command:

```bash
yum install httpd
```

This command will download and install the `httpd` package along with any necessary dependencies.

### Example 2: Updating a Package
To update the `httpd` package to the latest version, you can run:

```bash
yum update httpd
```

This command checks for the latest version of `httpd` and updates it if a newer version is available.

## Tips
- Always run `yum update` regularly to keep your system and packages up to date, which can help improve security and performance.
- Use `yum search <keyword>` to quickly find packages related to a specific keyword.
- To view detailed information about a package before installing it, use `yum info <package-name>`.
- If you want to remove a package but keep its configuration files, use the `remove` option with the `-y` flag to automatically confirm the action:

```bash
yum remove -y <package-name>
```

By following these guidelines, you can effectively manage software packages on your RPM-based Linux system using `yum`.