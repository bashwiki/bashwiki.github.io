# [리눅스] Bash docker 사용법

## Overview
El comando `docker` es una herramienta de línea de comandos que permite a los desarrolladores y administradores de sistemas gestionar contenedores de aplicaciones. Docker utiliza contenedores para empaquetar aplicaciones y sus dependencias en un solo objeto, lo que facilita la implementación y escalabilidad en diferentes entornos. Su principal propósito es simplificar el proceso de creación, despliegue y ejecución de aplicaciones en contenedores, proporcionando un entorno consistente y aislado.

## Usage
La sintaxis básica del comando `docker` es la siguiente:

```bash
docker [opciones] [comando] [argumentos]
```

### Comandos Comunes
- `docker run`: Ejecuta un contenedor a partir de una imagen.
- `docker ps`: Muestra los contenedores en ejecución.
- `docker images`: Lista las imágenes disponibles en el sistema.
- `docker stop`: Detiene uno o más contenedores en ejecución.
- `docker rm`: Elimina uno o más contenedores.

### Opciones Comunes
- `-d`: Ejecuta el contenedor en segundo plano (modo "detached").
- `--name`: Asigna un nombre al contenedor.
- `-p`: Mapea puertos entre el contenedor y el host.
- `-v`: Monta volúmenes para persistencia de datos.

## Examples
### Ejemplo 1: Ejecutar un contenedor de Nginx
Para ejecutar un contenedor de Nginx en segundo plano y mapear el puerto 80 del contenedor al puerto 8080 del host, puedes usar el siguiente comando:

```bash
docker run -d --name mi-nginx -p 8080:80 nginx
```

### Ejemplo 2: Listar contenedores en ejecución
Para ver todos los contenedores que están actualmente en ejecución, utiliza:

```bash
docker ps
```

## Tips
- Siempre utiliza nombres descriptivos para tus contenedores con la opción `--name` para facilitar la gestión.
- Aprovecha los volúmenes (`-v`) para mantener los datos persistentes, especialmente en bases de datos.
- Utiliza `docker-compose` para gestionar aplicaciones multi-contenedor de manera más sencilla.
- Mantén tus imágenes actualizadas y elimina las que no necesites para liberar espacio en disco.

Con estos conceptos y ejemplos, estarás mejor preparado para utilizar el comando `docker` en tus proyectos de desarrollo y administración de sistemas.