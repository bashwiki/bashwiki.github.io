# [Linux] Bash docker uso: Manage containerized applications

## Overview
The `docker` command is a powerful tool used to manage containerized applications. It allows users to create, deploy, and run applications in containers, which are lightweight, portable, and self-sufficient environments that include everything needed to run a piece of software.

## Usage
The basic syntax of the `docker` command is as follows:

```bash
docker [options] [arguments]
```

## Common Options
Here are some common options you can use with the `docker` command:

- `run`: Create and start a container.
- `ps`: List running containers.
- `images`: List available images on the local machine.
- `pull`: Download an image from a Docker registry.
- `build`: Build an image from a Dockerfile.
- `exec`: Run a command in a running container.
- `stop`: Stop a running container.

## Common Examples

1. **Running a Container**
   To run a simple web server using an Nginx image:
   ```bash
   docker run -d -p 80:80 nginx
   ```

2. **Listing Running Containers**
   To see all currently running containers:
   ```bash
   docker ps
   ```

3. **Pulling an Image**
   To download the latest Ubuntu image from Docker Hub:
   ```bash
   docker pull ubuntu
   ```

4. **Building an Image**
   To build an image from a Dockerfile in the current directory:
   ```bash
   docker build -t my-image .
   ```

5. **Executing a Command in a Container**
   To open a bash shell in a running container:
   ```bash
   docker exec -it <container_id> bash
   ```

6. **Stopping a Container**
   To stop a running container:
   ```bash
   docker stop <container_id>
   ```

## Tips
- Always use the `-d` option with `run` to run containers in detached mode for background execution.
- Use `docker-compose` for managing multi-container applications more easily.
- Regularly clean up unused images and containers with `docker system prune` to free up space.
- Tag your images with meaningful names and versions to keep track of different builds.