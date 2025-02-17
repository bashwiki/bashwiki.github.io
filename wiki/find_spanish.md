# [Linux] Bash find uso: Buscar nombres de archivos

## Overview
El comando `find` en Bash se utiliza para buscar archivos y directorios en una jerarquía de directorios. Permite a los usuarios localizar archivos basándose en criterios específicos como el nombre, el tipo, el tamaño, la fecha de modificación, entre otros.

## Usage
La sintaxis básica del comando `find` es la siguiente:

```bash
find [ruta] [opciones] [expresión]
```

- **ruta**: Especifica el directorio donde se comenzará la búsqueda.
- **opciones**: Modifican el comportamiento de la búsqueda.
- **expresión**: Define los criterios de búsqueda.

## Common Options
Aquí hay algunas opciones comunes que se pueden usar con el comando `find`:

- `-name`: Busca archivos que coincidan con un nombre específico.
- `-type`: Filtra los resultados por tipo de archivo (por ejemplo, `f` para archivos regulares, `d` para directorios).
- `-size`: Busca archivos de un tamaño específico (por ejemplo, `+100M` para archivos mayores a 100 MB).
- `-mtime`: Busca archivos modificados en un período de tiempo específico (por ejemplo, `-7` para archivos modificados en los últimos 7 días).
- `-exec`: Permite ejecutar un comando en cada archivo encontrado.

## Common Examples
A continuación, se presentan algunos ejemplos prácticos del uso del comando `find`:

1. **Buscar un archivo por nombre**:
   ```bash
   find /ruta/al/directorio -name "archivo.txt"
   ```

2. **Buscar todos los archivos de tipo directorio**:
   ```bash
   find /ruta/al/directorio -type d
   ```

3. **Buscar archivos mayores a 50 MB**:
   ```bash
   find /ruta/al/directorio -size +50M
   ```

4. **Buscar archivos modificados en los últimos 30 días**:
   ```bash
   find /ruta/al/directorio -mtime -30
   ```

5. **Eliminar archivos temporales**:
   ```bash
   find /ruta/al/directorio -name "*.tmp" -exec rm {} \;
   ```

## Tips
- Utiliza `-iname` en lugar de `-name` si deseas que la búsqueda no distinga entre mayúsculas y minúsculas.
- Para evitar que `find` busque en directorios específicos, puedes usar la opción `-prune`.
- Siempre prueba tus comandos con `-print` antes de ejecutar acciones destructivas como `-exec rm` para asegurarte de que estás seleccionando los archivos correctos.