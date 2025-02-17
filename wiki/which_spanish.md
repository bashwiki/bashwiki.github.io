# [Linux] Bash which uso: Localiza el ejecutable de un comando

## Overview
El comando `which` se utiliza en sistemas Unix y Linux para localizar la ruta completa del ejecutable de un comando específico. Esto es útil para saber qué versión de un programa se está utilizando o para verificar si un comando está instalado en el sistema.

## Usage
La sintaxis básica del comando `which` es la siguiente:

```
which [opciones] [argumentos]
```

## Common Options
- `-a`: Muestra todas las ubicaciones del ejecutable en el PATH.
- `-s`: No muestra salida; solo devuelve el estado de salida.
- `--version`: Muestra la versión del comando `which`.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `which`:

1. **Encontrar la ubicación de un comando:**
   ```bash
   which python
   ```

2. **Ver todas las ubicaciones de un comando:**
   ```bash
   which -a python
   ```

3. **Verificar si un comando está instalado sin salida:**
   ```bash
   which -s git
   ```

4. **Mostrar la versión del comando `which`:**
   ```bash
   which --version
   ```

## Tips
- Utiliza `which -a` para encontrar todas las versiones de un comando si tienes múltiples instalaciones.
- Si `which` no devuelve nada, es posible que el comando no esté instalado o no esté en tu PATH.
- Recuerda que `which` solo busca en el PATH, así que asegúrate de que el comando que buscas esté en una de las rutas especificadas.