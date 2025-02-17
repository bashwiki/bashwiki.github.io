# [Linux] Bash watch uso: Muestra la salida de un comando periódicamente

## Overview
El comando `watch` en Bash se utiliza para ejecutar un comando de forma repetida y mostrar su salida en la terminal. Esto es útil para monitorear cambios en la salida de un comando específico en intervalos regulares.

## Usage
La sintaxis básica del comando `watch` es la siguiente:

```bash
watch [opciones] [comando]
```

## Common Options
- `-n, --interval`: Especifica el intervalo en segundos entre cada ejecución del comando. Por defecto, es de 2 segundos.
- `-d, --differences`: Resalta las diferencias entre la salida anterior y la nueva.
- `-t, --no-title`: Suprime la línea de título que muestra la hora y el comando que se está ejecutando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `watch`:

1. **Monitorear el uso de memoria:**
   ```bash
   watch free -h
   ```

2. **Ver el contenido de un directorio:**
   ```bash
   watch ls -l
   ```

3. **Monitorear cambios en un archivo de log:**
   ```bash
   watch tail -n 10 /var/log/syslog
   ```

4. **Ver el uso de disco:**
   ```bash
   watch df -h
   ```

5. **Resaltar cambios en el uso de CPU:**
   ```bash
   watch -d top -b -n 1 | head -n 20
   ```

## Tips
- Utiliza la opción `-n` para ajustar el intervalo de tiempo según tus necesidades. Por ejemplo, `watch -n 5 ls` ejecutará el comando cada 5 segundos.
- La opción `-d` es muy útil para identificar rápidamente los cambios en la salida, especialmente cuando se monitorean datos que cambian frecuentemente.
- Si deseas detener la ejecución de `watch`, simplemente presiona `Ctrl + C`.