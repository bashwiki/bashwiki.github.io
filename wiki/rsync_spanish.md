# [리눅스] Bash rsync 사용법

## Overview
`rsync` es una herramienta de línea de comandos utilizada para sincronizar archivos y directorios entre dos ubicaciones. Su principal propósito es transferir y sincronizar archivos de manera eficiente, minimizando la cantidad de datos que se copian al solo transferir las diferencias entre el origen y el destino. Esto lo convierte en una opción ideal para copias de seguridad y replicación de datos.

## Usage
La sintaxis básica del comando `rsync` es la siguiente:

```bash
rsync [opciones] origen destino
```

### Opciones Comunes
- `-a`: Modo archivo; permite la sincronización recursiva y preserva atributos como permisos, tiempos de modificación y enlaces simbólicos.
- `-v`: Muestra la salida detallada del proceso de sincronización.
- `-z`: Comprime los datos durante la transferencia para reducir el uso del ancho de banda.
- `-r`: Sincroniza directorios de forma recursiva.
- `--delete`: Elimina archivos en el destino que ya no están en el origen.
- `-e`: Especifica el método de conexión remoto, como SSH.

## Examples
### Ejemplo 1: Sincronizar un directorio local a otro directorio local
Para sincronizar un directorio llamado `carpeta_origen` a `carpeta_destino`, puedes usar el siguiente comando:

```bash
rsync -av carpeta_origen/ carpeta_destino/
```

Este comando copiará todos los archivos y subdirectorios de `carpeta_origen` a `carpeta_destino`, preservando los atributos de los archivos.

### Ejemplo 2: Sincronizar archivos a un servidor remoto
Para sincronizar un directorio local a un servidor remoto utilizando SSH, puedes usar el siguiente comando:

```bash
rsync -avz -e ssh carpeta_origen/ usuario@servidor:/ruta/destino/
```

Este comando transferirá los archivos de `carpeta_origen` al servidor remoto, comprimiendo los datos durante la transferencia.

## Tips
- Siempre es recomendable realizar pruebas con la opción `--dry-run` (simulación) para ver qué archivos se transferirían sin realizar cambios reales. Por ejemplo:

```bash
rsync -av --dry-run carpeta_origen/ carpeta_destino/
```

- Utiliza la opción `--delete` con precaución, ya que eliminará archivos en el destino que no estén presentes en el origen.
- Considera usar `rsync` en scripts de automatización para copias de seguridad programadas, lo que puede ayudar a mantener tus datos seguros y actualizados.