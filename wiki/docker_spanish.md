# [Linux] Bash docker uso: Gestión de contenedores

## Overview
El comando `docker` se utiliza para gestionar contenedores de aplicaciones. Permite crear, ejecutar y administrar contenedores que encapsulan aplicaciones y sus dependencias, facilitando la portabilidad y escalabilidad.

## Usage
La sintaxis básica del comando `docker` es la siguiente:

```bash
docker [opciones] [argumentos]
```

## Common Options
- `run`: Crea y ejecuta un contenedor a partir de una imagen.
- `ps`: Lista los contenedores en ejecución.
- `images`: Muestra las imágenes disponibles en el sistema.
- `rm`: Elimina uno o más contenedores.
- `rmi`: Elimina una o más imágenes.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `docker`:

1. **Ejecutar un contenedor de Ubuntu:**
   ```bash
   docker run -it ubuntu
   ```

2. **Listar contenedores en ejecución:**
   ```bash
   docker ps
   ```

3. **Mostrar todas las imágenes disponibles:**
   ```bash
   docker images
   ```

4. **Eliminar un contenedor específico:**
   ```bash
   docker rm nombre_del_contenedor
   ```

5. **Eliminar una imagen específica:**
   ```bash
   docker rmi nombre_de_la_imagen
   ```

## Tips
- Siempre utiliza la opción `-it` al ejecutar contenedores interactivos para acceder a la terminal.
- Usa `docker-compose` para gestionar aplicaciones multicontenedor de manera más sencilla.
- Mantén tus imágenes actualizadas para evitar vulnerabilidades de seguridad.
- Considera etiquetar tus imágenes con versiones para un mejor control de versiones.