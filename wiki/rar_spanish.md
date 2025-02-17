# [Linux] Bash rar uso: Comprimir y descomprimir archivos

## Overview
El comando `rar` se utiliza para crear y gestionar archivos comprimidos en formato RAR. Este formato es conocido por su alta tasa de compresión y es ampliamente utilizado para agrupar y reducir el tamaño de archivos y carpetas.

## Usage
La sintaxis básica del comando `rar` es la siguiente:

```bash
rar [opciones] [argumentos]
```

## Common Options
- `a`: Añadir archivos a un archivo RAR existente.
- `x`: Extraer archivos de un archivo RAR.
- `t`: Probar la integridad de un archivo RAR.
- `v`: Mostrar el progreso de la compresión o extracción.
- `r`: Comprimir archivos de forma recursiva en directorios.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `rar`:

1. **Crear un archivo RAR**:
   ```bash
   rar a archivo_comprimido.rar archivo1.txt archivo2.txt
   ```

2. **Extraer un archivo RAR**:
   ```bash
   rar x archivo_comprimido.rar
   ```

3. **Probar la integridad de un archivo RAR**:
   ```bash
   rar t archivo_comprimido.rar
   ```

4. **Comprimir un directorio de forma recursiva**:
   ```bash
   rar a archivo_comprimido.rar /ruta/al/directorio/
   ```

5. **Mostrar el progreso de la compresión**:
   ```bash
   rar av archivo_comprimido.rar archivo1.txt
   ```

## Tips
- Asegúrate de tener suficiente espacio en disco antes de crear archivos RAR grandes.
- Utiliza la opción `-v` para ver el progreso y el estado de la compresión, especialmente en archivos grandes.
- Considera usar contraseñas para proteger tus archivos RAR sensibles utilizando la opción `-p`.