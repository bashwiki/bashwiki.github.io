# [리눅스] Bash tee 사용법

## Overview
El comando `tee` en Bash se utiliza para leer desde la entrada estándar y escribir simultáneamente en la salida estándar y en uno o más archivos. Su propósito principal es permitir que los datos fluyan a través de una tubería mientras se guardan en un archivo, lo que es especialmente útil para registrar la salida de otros comandos sin interrumpir el flujo de datos.

## Usage
La sintaxis básica del comando `tee` es la siguiente:

```bash
tee [opciones] [archivo...]
```

### Opciones comunes:
- `-a`, `--append`: Añade la salida al final del archivo en lugar de sobrescribirlo.
- `-i`, `--ignore-interrupts`: Ignora las señales de interrupción.
- `--help`: Muestra la ayuda sobre el uso del comando.
- `--version`: Muestra la versión del comando `tee`.

## Examples
### Ejemplo 1: Guardar la salida de un comando en un archivo
Supongamos que deseas listar los archivos en un directorio y guardar esa lista en un archivo llamado `lista.txt`. Puedes hacerlo de la siguiente manera:

```bash
ls -l | tee lista.txt
```

Este comando ejecuta `ls -l`, muestra la salida en la terminal y también la guarda en `lista.txt`.

### Ejemplo 2: Añadir salida a un archivo existente
Si deseas agregar la salida de un comando a un archivo existente en lugar de sobrescribirlo, puedes usar la opción `-a`. Por ejemplo:

```bash
echo "Nueva entrada" | tee -a lista.txt
```

Este comando añade "Nueva entrada" al final de `lista.txt` y también muestra el texto en la terminal.

## Tips
- Utiliza `tee` en combinación con otros comandos en una tubería para registrar la salida mientras continúas procesando los datos.
- Si trabajas con scripts, considera usar `tee` para guardar registros de depuración sin perder la salida en la consola.
- Recuerda que `tee` puede escribir en múltiples archivos al mismo tiempo. Por ejemplo:

```bash
echo "Mensaje importante" | tee archivo1.txt archivo2.txt
```

Esto escribirá "Mensaje importante" tanto en `archivo1.txt` como en `archivo2.txt`.