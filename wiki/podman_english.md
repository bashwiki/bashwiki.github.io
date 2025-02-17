# [Linux] Bash podman uso: Manage containers without a daemon

## Overview
Podman is a container management tool that allows users to create, manage, and run containers and images. It is designed to be a drop-in replacement for Docker, but unlike Docker, Podman does not require a daemon to run, making it more lightweight and secure.

## Usage
The basic syntax for using the podman command is as follows:

```bash
podman [options] [arguments]
```

## Common Options
- `run`: Create and start a container.
- `ps`: List running containers.
- `images`: List available images.
- `pull`: Download an image from a container registry.
- `rm`: Remove one or more containers.
- `rmi`: Remove one or more images.
- `exec`: Run a command in a running container.

## Common Examples

### Running a Container
To run a simple container using the `alpine` image, you can use:

```bash
podman run -it alpine /bin/sh
```

### Listing Running Containers
To see all currently running containers, use:

```bash
podman ps
```

### Pulling an Image
To download an image from a registry, such as `nginx`, you can execute:

```bash
podman pull nginx
```

### Removing a Container
To remove a stopped container, use the following command, replacing `container_id` with the actual ID:

```bash
podman rm container_id
```

### Listing Available Images
To view all images available on your system, run:

```bash
podman images
```

## Tips
- Always check the status of your containers with `podman ps` to ensure they are running as expected.
- Use `podman logs container_id` to view the logs of a specific container for troubleshooting.
- Consider using `podman-compose` for managing multi-container applications easily.
- Regularly clean up unused containers and images with `podman rm` and `podman rmi` to free up space.