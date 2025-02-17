# [Linux] Bash chmod Uso: Cambiar permisos de archivos y directorios

## Overview
El comando `chmod` se utiliza en sistemas Unix y Linux para cambiar los permisos de acceso a archivos y directorios. Permite a los usuarios definir quién puede leer, escribir o ejecutar un archivo.

## Usage
La sintaxis básica del comando `chmod` es la siguiente:

```bash
chmod [opciones] [argumentos]
```

## Common Options
- `-R`: Cambia los permisos de forma recursiva en todos los archivos y subdirectorios.
- `-v`: Muestra información detallada sobre los cambios realizados.
- `-c`: Solo muestra los cambios que se han realizado.

## Common Examples
1. **Cambiar permisos a un archivo específico**:
   ```bash
   chmod 755 archivo.txt
   ```
   Esto establece permisos de lectura, escritura y ejecución para el propietario, y solo lectura y ejecución para el grupo y otros.

2. **Cambiar permisos de forma recursiva**:
   ```bash
   chmod -R 644 /ruta/al/directorio
   ```
   Esto cambia los permisos de todos los archivos en el directorio especificado a lectura y escritura para el propietario, y solo lectura para el grupo y otros.

3. **Agregar permisos de ejecución a un archivo**:
   ```bash
   chmod +x script.sh
   ```
   Esto permite que el archivo `script.sh` se ejecute como un programa.

4. **Eliminar permisos de escritura para otros**:
   ```bash
   chmod o-w documento.txt
   ```
   Esto quita el permiso de escritura para otros usuarios en el archivo `documento.txt`.

## Tips
- Siempre verifica los permisos actuales de un archivo con `ls -l` antes de realizar cambios.
- Usa `chmod` con cuidado, especialmente al aplicar la opción `-R`, ya que puede afectar a muchos archivos y directorios.
- Familiarízate con la notación octal y simbólica para un uso más efectivo del comando.