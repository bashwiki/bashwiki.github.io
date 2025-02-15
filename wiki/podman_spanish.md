# [리눅스] Bash podman 사용법

## Overview
`podman` es una herramienta de línea de comandos que permite a los usuarios gestionar contenedores y pods de forma similar a Docker, pero sin necesidad de un demonio en segundo plano. Su principal propósito es facilitar la creación, ejecución y gestión de contenedores de aplicaciones, ofreciendo una alternativa ligera y segura para el desarrollo y despliegue de aplicaciones en entornos de contenedores.

## Usage
La sintaxis básica del comando `podman` es la siguiente:

```
podman [opciones] comando [argumentos]
```

Algunas de las opciones más comunes incluyen:

- `run`: Crea y ejecuta un contenedor.
- `ps`: Muestra los contenedores en ejecución.
- `pull`: Descarga una imagen de contenedor desde un registro.
- `build`: Construye una imagen a partir de un Dockerfile.
- `rm`: Elimina uno o más contenedores.

## Examples
### Ejemplo 1: Ejecutar un contenedor
Para ejecutar un contenedor de Nginx, puedes usar el siguiente comando:

```bash
podman run -d -p 8080:80 nginx
```
Este comando ejecuta un contenedor de Nginx en segundo plano (`-d`) y mapea el puerto 80 del contenedor al puerto 8080 de la máquina host.

### Ejemplo 2: Listar contenedores en ejecución
Para ver todos los contenedores que están actualmente en ejecución, utiliza:

```bash
podman ps
```
Este comando mostrará una lista de los contenedores activos, incluyendo su ID, nombre y estado.

## Tips
- **Usa `podman-compose`**: Si trabajas con múltiples contenedores, considera usar `podman-compose`, que permite gestionar aplicaciones multi-contenedor de manera similar a `docker-compose`.
- **Verifica imágenes locales**: Antes de descargar una nueva imagen, verifica las imágenes que ya tienes en tu sistema con `podman images`.
- **Limpieza de contenedores**: Utiliza `podman rm` para eliminar contenedores detenidos y `podman rmi` para eliminar imágenes no utilizadas, ayudando a mantener tu entorno limpio y ordenado.
- **Seguridad**: `podman` ejecuta contenedores sin necesidad de privilegios de root, lo que mejora la seguridad al reducir el riesgo de vulnerabilidades.

Con estos conceptos y ejemplos, podrás comenzar a utilizar `podman` de manera efectiva en tus proyectos de desarrollo y despliegue de aplicaciones en contenedores.