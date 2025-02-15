# [리눅스] Bash dpkg 사용법

## Overview
`dpkg` is a low-level package management tool for Debian-based systems, including Ubuntu. Its primary purpose is to install, remove, and manage `.deb` packages. Unlike higher-level package managers like `apt`, which handle dependencies and repositories, `dpkg` operates directly on individual package files, making it a powerful tool for developers and system administrators who need granular control over package management.

## Usage
The basic syntax of the `dpkg` command is as follows:

```bash
dpkg [options] <command>
```

### Common Options
- `-i`, `--install`: Install a package from a `.deb` file.
- `-r`, `--remove`: Remove an installed package but keep its configuration files.
- `-P`, `--purge`: Remove an installed package along with its configuration files.
- `-l`, `--list`: List all installed packages.
- `-s`, `--status`: Show the status of a specified package.
- `-L`, `--listfiles`: List files installed by a specified package.
- `-S`, `--search`: Search for a package that owns a specific file.

## Examples

### Example 1: Installing a Package
To install a package from a `.deb` file, use the `-i` option:

```bash
sudo dpkg -i package_name.deb
```

This command installs the specified package. If there are missing dependencies, you may need to resolve them manually or use `apt-get install -f` to fix broken dependencies.

### Example 2: Listing Installed Packages
To list all installed packages on your system, use the `-l` option:

```bash
dpkg -l
```

This command displays a list of all installed packages along with their versions and descriptions.

## Tips
- Always check for missing dependencies after using `dpkg` to install a package. You can do this by running `sudo apt-get install -f`.
- Use the `-L` option to find out what files are installed by a specific package, which can help in troubleshooting or when you need to locate specific files.
- When removing packages, consider using the `--purge` option if you want to clean up configuration files as well.
- For a more user-friendly experience, consider using `apt` or `apt-get` for package management, as they handle dependencies automatically and provide a higher-level interface. However, `dpkg` is invaluable for specific tasks that require direct manipulation of `.deb` files.