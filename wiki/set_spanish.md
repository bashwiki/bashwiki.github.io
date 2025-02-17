# [Linux] Bash set uso: Configurar opciones de shell

## Overview
El comando `set` en Bash se utiliza para establecer o desactivar opciones del shell. Esto permite modificar el comportamiento del entorno de la línea de comandos, facilitando la personalización de la sesión actual.

## Usage
La sintaxis básica del comando `set` es la siguiente:

```
set [opciones] [argumentos]
```

## Common Options
- `-e`: Termina el script si un comando falla.
- `-u`: Trata las variables no definidas como un error.
- `-x`: Muestra cada comando antes de ejecutarlo, útil para depuración.
- `-o`: Permite establecer opciones específicas del shell, como `-o noclobber` para evitar sobrescribir archivos.

## Common Examples

1. **Activar el modo de error**:
   ```bash
   set -e
   ```

2. **Activar el modo de variable no definida**:
   ```bash
   set -u
   ```

3. **Mostrar comandos en ejecución**:
   ```bash
   set -x
   ```

4. **Desactivar una opción**:
   ```bash
   set +e
   ```

5. **Combinar opciones**:
   ```bash
   set -eu
   ```

## Tips
- Utiliza `set -e` en scripts para evitar que continúen ejecutándose si ocurre un error.
- Activa `set -u` para detectar errores de variables no definidas, lo que puede ayudar a prevenir comportamientos inesperados.
- Usa `set -x` durante la depuración para ver el flujo de ejecución y los valores de las variables.