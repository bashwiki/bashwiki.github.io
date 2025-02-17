# [Linux] Bash pwd uso equivalente: Muestra el directorio de trabajo actual

## Overview
El comando `pwd` (print working directory) se utiliza en Bash para mostrar la ruta del directorio de trabajo actual en el que se encuentra el usuario. Es una herramienta fundamental para navegar por el sistema de archivos, ya que permite saber en qué ubicación se está trabajando en un momento dado.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
pwd [opciones] [argumentos]
```

## Common Options
- `-L`: Muestra la ruta lógica del directorio de trabajo actual, que puede incluir enlaces simbólicos.
- `-P`: Muestra la ruta física del directorio de trabajo actual, resolviendo todos los enlaces simbólicos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `pwd`:

1. **Mostrar el directorio actual**:
   ```bash
   pwd
   ```

2. **Mostrar la ruta lógica**:
   ```bash
   pwd -L
   ```

3. **Mostrar la ruta física**:
   ```bash
   pwd -P
   ```

4. **Usar pwd en un script**:
   ```bash
   #!/bin/bash
   echo "El directorio de trabajo actual es: $(pwd)"
   ```

## Tips
- Utiliza `pwd` frecuentemente para confirmar tu ubicación en el sistema de archivos, especialmente antes de ejecutar comandos que afectan archivos o directorios.
- Combina `pwd` con otros comandos, como `cd`, para verificar que has cambiado correctamente de directorio.
- Recuerda que `pwd` es útil en scripts para obtener la ubicación actual y usarla en operaciones posteriores.