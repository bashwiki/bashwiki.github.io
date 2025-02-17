# [Linux] Bash podman uso: Gestión de contenedores sin daemon

## Overview
Podman es una herramienta de línea de comandos que permite a los usuarios gestionar contenedores y pods de manera eficiente. A diferencia de Docker, Podman no requiere un daemon en ejecución, lo que permite ejecutar contenedores como procesos de usuario.

## Usage
La sintaxis básica del comando podman es la siguiente:

```bash
podman [opciones] [argumentos]
```

## Common Options
- `run`: Ejecuta un nuevo contenedor.
- `ps`: Muestra los contenedores en ejecución.
- `images`: Lista las imágenes disponibles en el sistema.
- `rm`: Elimina uno o más contenedores.
- `rmi`: Elimina una o más imágenes.

## Common Examples
Aquí hay algunos ejemplos prácticos de cómo usar podman:

1. **Ejecutar un contenedor simple**:
   ```bash
   podman run hello-world
   ```

2. **Listar contenedores en ejecución**:
   ```bash
   podman ps
   ```

3. **Listar todas las imágenes disponibles**:
   ```bash
   podman images
   ```

4. **Eliminar un contenedor**:
   ```bash
   podman rm nombre_del_contenedor
   ```

5. **Eliminar una imagen**:
   ```bash
   podman rmi nombre_de_la_imagen
   ```

## Tips
- Utiliza `podman --help` para obtener información sobre las opciones disponibles y su uso.
- Considera usar `podman-compose` para gestionar aplicaciones que requieren múltiples contenedores.
- Recuerda que Podman permite ejecutar contenedores sin privilegios, lo que mejora la seguridad en comparación con otras herramientas.