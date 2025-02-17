# [Linux] Bash cd Uso: Cambiar de directorio en el sistema de archivos

## Overview
El comando `cd` (change directory) se utiliza en Bash para cambiar el directorio de trabajo actual. Esto permite a los usuarios navegar a diferentes ubicaciones en el sistema de archivos.

## Usage
La sintaxis básica del comando `cd` es la siguiente:

```bash
cd [opciones] [argumentos]
```

## Common Options
- `-`: Cambia al directorio anterior.
- `..`: Cambia al directorio padre del directorio actual.
- `~`: Cambia al directorio home del usuario actual.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `cd`:

1. Cambiar al directorio padre:
   ```bash
   cd ..
   ```

2. Cambiar al directorio home del usuario:
   ```bash
   cd ~
   ```

3. Cambiar al directorio anterior:
   ```bash
   cd -
   ```

4. Cambiar a un directorio específico:
   ```bash
   cd /ruta/al/directorio
   ```

5. Cambiar a un directorio relativo:
   ```bash
   cd subdirectorio
   ```

## Tips
- Usa `cd -` para volver rápidamente al directorio anterior en el que estabas.
- Puedes usar `cd` sin argumentos para volver directamente a tu directorio home.
- Asegúrate de que la ruta que estás intentando acceder existe para evitar errores.