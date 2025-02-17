# [Linux] Bash free uso: Muestra información sobre la memoria del sistema

## Overview
El comando `free` en Bash se utiliza para mostrar la cantidad de memoria libre y utilizada en el sistema, incluyendo la memoria física y la memoria de intercambio (swap). Es una herramienta útil para monitorear el uso de memoria en tiempo real.

## Usage
La sintaxis básica del comando `free` es la siguiente:

```bash
free [opciones] [argumentos]
```

## Common Options
- `-h`: Muestra la memoria en un formato legible para humanos (por ejemplo, en MB o GB).
- `-m`: Muestra la memoria en megabytes.
- `-g`: Muestra la memoria en gigabytes.
- `-s <segundos>`: Actualiza la información cada <segundos> especificados.
- `-t`: Muestra un total de la memoria utilizada y libre.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `free`:

1. **Mostrar memoria en formato legible para humanos:**
   ```bash
   free -h
   ```

2. **Mostrar memoria en megabytes:**
   ```bash
   free -m
   ```

3. **Mostrar memoria en gigabytes:**
   ```bash
   free -g
   ```

4. **Actualizar la información cada 5 segundos:**
   ```bash
   free -s 5
   ```

5. **Mostrar total de memoria utilizada y libre:**
   ```bash
   free -t
   ```

## Tips
- Utiliza la opción `-h` para facilitar la lectura de los resultados, especialmente en sistemas con grandes cantidades de memoria.
- Combina `free` con otros comandos como `watch` para monitorear el uso de memoria en tiempo real:
  ```bash
  watch free -h
  ```
- Revisa la memoria de intercambio (swap) para asegurarte de que el sistema no esté utilizando demasiado, lo que podría afectar el rendimiento.