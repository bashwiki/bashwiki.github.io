# [Linux] Bash ln Uso: Crear enlaces a archivos y directorios

## Overview
El comando `ln` se utiliza en sistemas Unix y Linux para crear enlaces a archivos y directorios. Existen dos tipos de enlaces: los enlaces duros y los enlaces simbólicos. Los enlaces duros apuntan al mismo inode que el archivo original, mientras que los enlaces simbólicos son referencias a la ruta del archivo.

## Usage
La sintaxis básica del comando `ln` es la siguiente:

```bash
ln [opciones] [origen] [destino]
```

## Common Options
- `-s`: Crea un enlace simbólico en lugar de un enlace duro.
- `-f`: Fuerza la creación del enlace, sobrescribiendo cualquier archivo existente en el destino.
- `-n`: No desreferencia el destino si es un enlace simbólico existente.
- `-v`: Muestra información detallada sobre lo que está haciendo el comando.

## Common Examples
1. **Crear un enlace duro:**
   ```bash
   ln archivo.txt enlace.txt
   ```
   Este comando crea un enlace duro llamado `enlace.txt` que apunta a `archivo.txt`.

2. **Crear un enlace simbólico:**
   ```bash
   ln -s archivo.txt enlace_simbólico.txt
   ```
   Aquí se crea un enlace simbólico llamado `enlace_simbólico.txt` que apunta a `archivo.txt`.

3. **Forzar la creación de un enlace:**
   ```bash
   ln -f archivo.txt enlace.txt
   ```
   Este comando sobrescribirá `enlace.txt` si ya existe.

4. **Crear un enlace simbólico a un directorio:**
   ```bash
   ln -s /ruta/al/directorio enlace_directorio
   ```
   Esto crea un enlace simbólico a un directorio.

## Tips
- Utiliza enlaces simbólicos para crear accesos directos a archivos o directorios en ubicaciones diferentes sin duplicar el contenido.
- Los enlaces duros no se pueden crear para directorios (a menos que seas superusuario) y no pueden cruzar sistemas de archivos.
- Recuerda que si eliminas el archivo original, los enlaces duros seguirán funcionando, pero los enlaces simbólicos se romperán.