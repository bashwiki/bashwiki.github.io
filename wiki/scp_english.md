# [리눅스] Bash scp 사용법

## Overview
The `scp` (Secure Copy Protocol) command is a secure file transfer utility that allows users to copy files and directories between hosts on a network. It uses SSH (Secure Shell) for data transfer, providing the same authentication and security as SSH. The primary purpose of `scp` is to securely transfer files between local and remote systems, making it an essential tool for engineers and developers who need to manage files across different machines.

## Usage
The basic syntax of the `scp` command is as follows:

```
scp [options] [source] [destination]
```

### Common Options
- `-r`: Recursively copy entire directories.
- `-P port`: Specify the port to connect to on the remote host (note that it's an uppercase 'P').
- `-i identity_file`: Select the file from which the identity (private key) for public key authentication is read.
- `-v`: Enable verbose mode, which provides detailed information about the transfer process.
- `-q`: Suppress the progress meter and non-error messages.

## Examples

### Example 1: Copying a File from Local to Remote
To copy a file named `example.txt` from your local machine to a remote server, you can use the following command:

```bash
scp example.txt username@remote_host:/path/to/destination/
```
In this command:
- `example.txt` is the file you want to copy.
- `username` is your user account on the remote server.
- `remote_host` is the IP address or hostname of the remote server.
- `/path/to/destination/` is the directory on the remote server where the file will be copied.

### Example 2: Copying a Directory from Remote to Local
To copy a directory named `project` from a remote server to your local machine, use the `-r` option:

```bash
scp -r username@remote_host:/path/to/project /local/destination/
```
In this command:
- `-r` indicates that you are copying a directory.
- `/local/destination/` is the local directory where the `project` directory will be copied.

## Tips
- Always ensure that you have the necessary permissions to read the source files and write to the destination directory.
- When transferring large files or directories, consider using the `-v` option to monitor the progress and diagnose any issues that may arise during the transfer.
- If you frequently connect to the same remote server, consider setting up SSH keys for passwordless authentication, which can streamline the use of `scp`.
- Be cautious when using `scp` to overwrite files, as it will replace existing files without prompting for confirmation.