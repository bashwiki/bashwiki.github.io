# [Linux] Bash egrep uso equivalente: búsqueda de patrones en texto

## Overview
El comando `egrep` es una variante de `grep` que permite buscar patrones en texto utilizando expresiones regulares extendidas. Es útil para filtrar líneas que coinciden con un patrón específico en archivos o en la salida de otros comandos.

## Usage
La sintaxis básica del comando `egrep` es la siguiente:

```bash
egrep [opciones] [argumentos]
```

## Common Options
- `-i`: Ignora la distinción entre mayúsculas y minúsculas.
- `-v`: Muestra las líneas que no coinciden con el patrón.
- `-c`: Cuenta el número de líneas que coinciden con el patrón.
- `-n`: Muestra el número de línea junto con las líneas coincidentes.
- `-r`: Busca recursivamente en directorios.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `egrep`:

1. **Buscar un patrón en un archivo:**
   ```bash
   egrep "error" archivo.log
   ```

2. **Buscar ignorando mayúsculas y minúsculas:**
   ```bash
   egrep -i "advertencia" archivo.txt
   ```

3. **Contar el número de coincidencias:**
   ```bash
   egrep -c "éxito" archivo.txt
   ```

4. **Mostrar líneas que no coinciden con el patrón:**
   ```bash
   egrep -v "debug" archivo.log
   ```

5. **Buscar recursivamente en un directorio:**
   ```bash
   egrep -r "configuración" /ruta/al/directorio
   ```

## Tips
- Utiliza `-n` para obtener el contexto de las coincidencias, lo que puede ser útil para identificar la ubicación exacta en el archivo.
- Combina `egrep` con otros comandos utilizando tuberías (`|`) para filtrar la salida de otros procesos.
- Familiarízate con las expresiones regulares para aprovechar al máximo las capacidades de búsqueda de `egrep`.