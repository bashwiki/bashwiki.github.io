# [Linux] Bash zip uso: Comprimir archivos y directorios

## Overview
El comando `zip` se utiliza para comprimir archivos y directorios en un archivo ZIP. Esto es útil para reducir el tamaño de los archivos y facilitar su almacenamiento o transferencia.

## Usage
La sintaxis básica del comando `zip` es la siguiente:

```bash
zip [opciones] [archivo_zip] [archivos]
```

## Common Options
- `-r`: Comprime directorios de forma recursiva.
- `-e`: Crea un archivo ZIP encriptado.
- `-u`: Actualiza los archivos en un archivo ZIP existente.
- `-d`: Elimina archivos de un archivo ZIP.
- `-l`: Muestra el contenido de un archivo ZIP.

## Common Examples
1. **Comprimir un solo archivo:**

   ```bash
   zip archivo.zip documento.txt
   ```

2. **Comprimir varios archivos:**

   ```bash
   zip archivos.zip documento.txt imagen.png video.mp4
   ```

3. **Comprimir un directorio de forma recursiva:**

   ```bash
   zip -r carpeta.zip /ruta/a/carpeta
   ```

4. **Crear un archivo ZIP encriptado:**

   ```bash
   zip -e archivo_encriptado.zip documento.txt
   ```

5. **Actualizar un archivo ZIP existente:**

   ```bash
   zip -u archivo.zip nuevo_documento.txt
   ```

6. **Eliminar un archivo de un archivo ZIP:**

   ```bash
   zip -d archivo.zip documento.txt
   ```

## Tips
- Siempre verifica el contenido de un archivo ZIP utilizando `zip -l archivo.zip` antes de descomprimirlo.
- Utiliza la opción `-r` con precaución, ya que puede incluir archivos no deseados si no se especifica correctamente el directorio.
- Considera usar la encriptación para archivos sensibles, especialmente si se van a transferir por internet.