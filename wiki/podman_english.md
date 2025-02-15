# [리눅스] Bash podman 사용법

## Overview
`podman` is a command-line tool designed for managing containers and container images. It allows developers and engineers to create, run, and manage containers without requiring a daemon, making it a lightweight alternative to Docker. Podman is compatible with the Docker CLI, which means that many Docker commands can be used interchangeably with Podman. Its primary purpose is to facilitate container management in a secure and efficient manner, with a focus on rootless container execution.

## Usage
The basic syntax for the `podman` command is as follows:

```
podman [OPTIONS] COMMAND [ARG...]
```

### Common Options
- `--help`: Display help information about the command.
- `--version`: Show the version of Podman installed.
- `-v`, `--verbose`: Enable verbose output for more detailed information during execution.
- `-q`, `--quiet`: Suppress output, showing only container IDs.

### Commands
Some of the most commonly used commands with `podman` include:
- `podman run`: Create and start a container.
- `podman ps`: List running containers.
- `podman images`: List available container images.
- `podman rm`: Remove one or more containers.
- `podman rmi`: Remove one or more images.

## Examples

### Example 1: Running a Simple Container
To run a simple container using the `nginx` image, you can use the following command:

```bash
podman run -d -p 8080:80 nginx
```
This command does the following:
- `-d`: Runs the container in detached mode (in the background).
- `-p 8080:80`: Maps port 8080 on the host to port 80 on the container.

### Example 2: Listing Running Containers
To list all currently running containers, use:

```bash
podman ps
```
This command will display a table of running containers, including their IDs, names, and status.

## Tips
- **Rootless Containers**: Podman allows you to run containers without root privileges, enhancing security. Use the `--user` option to specify a user when running containers.
- **Pod Management**: Podman supports the concept of pods, which are groups of one or more containers sharing the same network namespace. Use `podman pod` commands to manage pods effectively.
- **Image Management**: Regularly clean up unused images and containers to save disk space. Use `podman rmi` and `podman rm` to remove images and containers, respectively.
- **Compatibility with Docker**: If you are transitioning from Docker to Podman, you can often use the same commands with minimal changes, making the switch easier.

By leveraging `podman`, developers can efficiently manage containerized applications while maintaining a focus on security and simplicity.