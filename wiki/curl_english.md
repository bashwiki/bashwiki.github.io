# [리눅스] Bash curl 사용법

## Overview
`curl` is a command-line tool used for transferring data to or from a server using various protocols, including HTTP, HTTPS, FTP, and more. Its primary purpose is to enable users to interact with web services and APIs, download files, and perform network diagnostics. `curl` is widely used in scripting and automation due to its versatility and support for a wide range of protocols.

## Usage
The basic syntax of the `curl` command is as follows:

```bash
curl [options] [URL]
```

### Common Options
- `-X, --request <command>`: Specify a custom request method to use when communicating with the server (e.g., GET, POST, PUT).
- `-d, --data <data>`: Send specified data in a POST request.
- `-H, --header <header>`: Pass custom header(s) to the server.
- `-o, --output <file>`: Write output to a specified file instead of stdout.
- `-I, --head`: Fetch the HTTP headers only.
- `-L, --location`: Follow redirects if the server responds with a redirect status code.
- `-u, --user <user:password>`: Specify user credentials for server authentication.

## Examples

### Example 1: Fetching a Web Page
To retrieve the HTML content of a web page, you can use the following command:

```bash
curl https://www.example.com
```

This command will output the HTML content of the specified URL directly to the terminal.

### Example 2: Sending a POST Request
To send data to a server using a POST request, you can use the `-d` option. Here’s an example of sending JSON data:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"John", "age":30}' https://api.example.com/users
```

In this command, we specify the request method as POST, set the content type to JSON, and send a JSON object as data to the specified API endpoint.

## Tips
- Use the `-o` option to save the output to a file, which is especially useful for downloading large files.
- Combine the `-L` option with requests to automatically follow redirects, ensuring you reach the final destination.
- For debugging, add the `-v` (verbose) option to see detailed information about the request and response, which can help troubleshoot issues.
- When working with APIs, always check the documentation for required headers and authentication methods to ensure successful requests.