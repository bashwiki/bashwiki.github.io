# [Linux] Bash scp Uso: Securely copy files between hosts

## Overview
The `scp` (Secure Copy Protocol) command is used to securely transfer files and directories between two locations over a network. It leverages SSH (Secure Shell) for data transfer, ensuring that the data is encrypted during transmission.

## Usage
The basic syntax of the `scp` command is as follows:

```
scp [options] [source] [destination]
```

## Common Options
- `-r`: Recursively copy entire directories.
- `-P port`: Specify a port number to connect to the remote host.
- `-i identity_file`: Use the specified private key file for authentication.
- `-v`: Enable verbose mode, providing detailed output of the transfer process.
- `-C`: Enable compression to speed up the transfer of large files.

## Common Examples

1. **Copy a file from local to remote host:**
   ```bash
   scp localfile.txt user@remote_host:/path/to/destination/
   ```

2. **Copy a file from remote host to local machine:**
   ```bash
   scp user@remote_host:/path/to/remotefile.txt /local/destination/
   ```

3. **Copy an entire directory from local to remote host:**
   ```bash
   scp -r local_directory/ user@remote_host:/path/to/destination/
   ```

4. **Specify a port while copying a file:**
   ```bash
   scp -P 2222 localfile.txt user@remote_host:/path/to/destination/
   ```

5. **Use a specific private key for authentication:**
   ```bash
   scp -i ~/.ssh/id_rsa localfile.txt user@remote_host:/path/to/destination/
   ```

## Tips
- Always ensure that you have the correct permissions on the remote directory to avoid permission denied errors.
- Use the `-v` option for troubleshooting if you encounter issues during file transfer.
- For large files, consider using the `-C` option to enable compression, which can significantly reduce transfer time.