# [Linux] Bash wget Uso: Download files from the web

## Overview
The `wget` command is a powerful utility in Linux used for downloading files from the web. It supports HTTP, HTTPS, and FTP protocols, allowing users to retrieve content from the internet easily.

## Usage
The basic syntax of the `wget` command is as follows:

```bash
wget [options] [arguments]
```

## Common Options
Here are some common options you can use with `wget`:

- `-O [file]`: Save the downloaded content to a specified file instead of the default filename.
- `-q`: Run in quiet mode, suppressing output.
- `-c`: Continue an incomplete download from where it left off.
- `--limit-rate=[rate]`: Limit the download speed to a specified rate.
- `-r`: Enable recursive downloading, allowing you to download entire websites.

## Common Examples

1. **Download a single file:**
   ```bash
   wget https://example.com/file.zip
   ```

2. **Download a file and save it with a specific name:**
   ```bash
   wget -O myfile.zip https://example.com/file.zip
   ```

3. **Continue an interrupted download:**
   ```bash
   wget -c https://example.com/largefile.zip
   ```

4. **Download a website recursively:**
   ```bash
   wget -r https://example.com
   ```

5. **Limit the download speed:**
   ```bash
   wget --limit-rate=200k https://example.com/largefile.zip
   ```

## Tips
- Always check the website's terms of service before downloading large amounts of data to ensure compliance.
- Use the `-q` option for scripts to avoid cluttering the output.
- Combine options for more complex tasks, such as `wget -c -r -np https://example.com` to continue a recursive download without parent directories.