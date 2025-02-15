# [리눅스] Bash wget 사용법

## Overview
`wget` is a command-line utility for downloading files from the web. It supports HTTP, HTTPS, and FTP protocols, making it a versatile tool for retrieving content from various sources. The primary purpose of `wget` is to facilitate non-interactive downloads, meaning it can work in the background without requiring user input, which is particularly useful for automated scripts and batch downloads.

## Usage
The basic syntax of the `wget` command is as follows:

```bash
wget [options] [URL]
```

### Common Options
- `-O [file]`: Save the downloaded file with the specified name instead of the default name derived from the URL.
- `-c`: Continue an incomplete download. This is useful if a download was interrupted and you want to resume it.
- `-q`: Operate in quiet mode. Suppresses output, which is useful for scripting.
- `--limit-rate=[amount]`: Limit the download speed to the specified amount (e.g., `200k` for 200 KB/s).
- `-r`: Enable recursive downloading, which allows you to download entire directories or websites.
- `-p`: Download all necessary files for displaying a webpage, including images and stylesheets.

## Examples

### Example 1: Basic File Download
To download a file from a URL, you can use the following command:

```bash
wget https://example.com/file.zip
```
This command will download `file.zip` from `https://example.com` and save it in the current directory.

### Example 2: Resume an Interrupted Download
If a download was interrupted, you can resume it using the `-c` option:

```bash
wget -c https://example.com/largefile.zip
```
This command will continue downloading `largefile.zip` from where it left off.

## Tips
- Use the `-q` option when running `wget` in scripts to minimize output and keep logs clean.
- For large downloads, consider using the `--limit-rate` option to avoid consuming too much bandwidth.
- When downloading multiple files, you can create a text file with URLs and use the `-i` option to download all of them at once:

```bash
wget -i urls.txt
```
This command will read URLs from `urls.txt` and download each one sequentially.

By utilizing `wget`, engineers and developers can efficiently manage file downloads directly from the command line, making it an essential tool for automation and scripting tasks.