# [리눅스] Bash rpm 사용법

## Overview
The `rpm` command stands for Red Hat Package Manager. It is a powerful tool used primarily in Red Hat-based Linux distributions (like Fedora, CentOS, and RHEL) for managing software packages. The primary purpose of `rpm` is to install, uninstall, query, and verify software packages in the RPM format. It allows users to manage software installations efficiently and ensures that all dependencies are met.

## Usage
The basic syntax for the `rpm` command is as follows:

```
rpm [OPTION] [PACKAGE]
```

### Common Options
- `-i` : Install a package.
- `-e` : Erase (uninstall) a package.
- `-q` : Query a package.
- `-v` : Verbose output.
- `-h` : Print hash marks as the package installs (progress indicator).
- `--nodeps` : Ignore dependency checks when installing or uninstalling.
- `-U` : Upgrade a package, installing it if it is not already installed.

## Examples

### Example 1: Installing a Package
To install a package named `example.rpm`, you would use the following command:

```bash
rpm -i example.rpm
```

This command installs the specified RPM package. If there are any missing dependencies, the installation will fail unless you use the `--nodeps` option.

### Example 2: Querying a Package
To check if a package named `example` is installed and to retrieve its version information, you can use:

```bash
rpm -q example
```

This command will return the version of the installed package or indicate that the package is not installed.

## Tips
- Always check for dependencies before installing a package. You can use the `yum` or `dnf` package managers for automatic dependency resolution.
- Use the `-v` option for more detailed output when installing or uninstalling packages, which can help in troubleshooting.
- Regularly verify installed packages with the command `rpm -V package_name` to ensure that they have not been altered or corrupted.
- When upgrading packages, consider using the `-U` option, which will upgrade the package if it exists or install it if it does not.

By mastering the `rpm` command, you can effectively manage software packages on Red Hat-based systems, ensuring a smooth and efficient development environment.