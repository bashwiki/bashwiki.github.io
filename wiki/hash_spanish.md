# [Linux] Bash hash uso: [gestiona el almacenamiento en caché de comandos]

## Overview
El comando `hash` en Bash se utiliza para gestionar el almacenamiento en caché de las ubicaciones de los comandos ejecutados. Esto permite que el intérprete de comandos recuerde las rutas de los comandos, mejorando así la velocidad de búsqueda al evitar búsquedas repetidas en el sistema de archivos.

## Usage
La sintaxis básica del comando `hash` es la siguiente:

```bash
hash [opciones] [argumentos]
```

## Common Options
- `-r`: Borra el caché de comandos, forzando a Bash a buscar de nuevo las ubicaciones de los comandos.
- `-p`: Permite especificar una ruta para un comando en particular, actualizando su ubicación en el caché.
- `-l`: Muestra la lista de comandos en caché junto con sus ubicaciones.

## Common Examples

### Verificar la caché de comandos
Para ver los comandos almacenados en caché, simplemente ejecuta:

```bash
hash
```

### Borrar la caché de comandos
Si deseas limpiar el caché y forzar a Bash a buscar de nuevo, utiliza:

```bash
hash -r
```

### Añadir un comando específico a la caché
Si quieres añadir un comando específico a la caché con su ruta, puedes hacerlo así:

```bash
hash -p /usr/local/bin/mi_comando mi_comando
```

### Listar comandos en caché
Para listar todos los comandos que están en caché junto con sus rutas, usa:

```bash
hash -l
```

## Tips
- Utiliza `hash -r` después de instalar nuevos programas para asegurarte de que Bash reconozca los nuevos comandos.
- Si trabajas con scripts que cambian frecuentemente, considera limpiar la caché regularmente para evitar conflictos.
- Recuerda que el comando `hash` solo afecta a la sesión actual de Bash; si abres una nueva terminal, se restablecerá el caché.