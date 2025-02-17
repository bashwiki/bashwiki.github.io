# [Linux] Bash 7z uso: Comprimir y descomprimir archivos

## Overview
El comando `7z` es una herramienta de línea de comandos utilizada para comprimir y descomprimir archivos. Forma parte del programa 7-Zip, que es conocido por su alta relación de compresión y soporte para múltiples formatos de archivo.

## Usage
La sintaxis básica del comando `7z` es la siguiente:

```
7z [opciones] [argumentos]
```

## Common Options
- `a`: Agregar archivos a un archivo comprimido.
- `x`: Extraer archivos de un archivo comprimido.
- `l`: Listar el contenido de un archivo comprimido.
- `d`: Eliminar archivos de un archivo comprimido.
- `t`: Especificar el tipo de archivo (por ejemplo, zip, 7z, etc.).

## Common Examples
- **Comprimir un archivo:**
  ```bash
  7z a archivo_comprimido.7z archivo.txt
  ```
  Este comando crea un archivo comprimido llamado `archivo_comprimido.7z` que contiene `archivo.txt`.

- **Descomprimir un archivo:**
  ```bash
  7z x archivo_comprimido.7z
  ```
  Este comando extrae el contenido de `archivo_comprimido.7z` en el directorio actual.

- **Listar el contenido de un archivo comprimido:**
  ```bash
  7z l archivo_comprimido.7z
  ```
  Este comando muestra los archivos contenidos en `archivo_comprimido.7z`.

- **Eliminar un archivo de un archivo comprimido:**
  ```bash
  7z d archivo_comprimido.7z archivo.txt
  ```
  Este comando elimina `archivo.txt` del archivo comprimido `archivo_comprimido.7z`.

## Tips
- Siempre verifica el contenido de un archivo comprimido con `7z l` antes de extraerlo para asegurarte de que contiene lo que esperas.
- Utiliza la opción `-p` para proteger con contraseña tus archivos comprimidos, por ejemplo: `7z a -pMiContraseña archivo_comprimido.7z archivo.txt`.
- Para mejorar la compresión, puedes experimentar con diferentes niveles de compresión usando la opción `-mx`, donde `x` puede ser un número del 0 al 9, siendo 9 el máximo.