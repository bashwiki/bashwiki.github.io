# [Linux] Bash dd Uso: Copiar y convertir datos

## Overview
El comando `dd` en Bash es una herramienta poderosa utilizada para copiar y convertir archivos. Se utiliza comúnmente para crear imágenes de disco, realizar copias de seguridad y transferir datos entre dispositivos.

## Usage
La sintaxis básica del comando `dd` es la siguiente:

```bash
dd [opciones] [argumentos]
```

## Common Options
- `if=`: Especifica el archivo de entrada (input file).
- `of=`: Especifica el archivo de salida (output file).
- `bs=`: Define el tamaño del bloque para la operación de lectura y escritura.
- `count=`: Indica el número de bloques a copiar.
- `status=`: Controla la información que se muestra durante la ejecución (por ejemplo, `none`, `noxfer`, `progress`).

## Common Examples
1. **Crear una imagen de disco**:
   ```bash
   dd if=/dev/sda of=/ruta/a/imagen.img bs=4M
   ```
   Este comando crea una imagen del disco `/dev/sda` y la guarda en `imagen.img`.

2. **Restaurar una imagen de disco**:
   ```bash
   dd if=/ruta/a/imagen.img of=/dev/sda bs=4M
   ```
   Este comando restaura la imagen guardada en `imagen.img` al disco `/dev/sda`.

3. **Copiar un archivo**:
   ```bash
   dd if=archivo.txt of=copia_archivo.txt
   ```
   Este comando copia el contenido de `archivo.txt` a `copia_archivo.txt`.

4. **Crear un archivo de tamaño específico**:
   ```bash
   dd if=/dev/zero of=archivo.bin bs=1M count=10
   ```
   Este comando crea un archivo de 10 MB lleno de ceros.

## Tips
- Siempre verifica el archivo de salida (`of=`) para evitar sobrescribir datos importantes.
- Utiliza `status=progress` para ver el progreso de la operación, especialmente en copias grandes.
- Ten cuidado al usar `dd` con dispositivos de bloque, ya que puede resultar en la pérdida de datos si se usa incorrectamente.