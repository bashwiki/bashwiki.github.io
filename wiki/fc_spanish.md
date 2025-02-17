# [Linux] Bash fc Uso equivalente: Editar y ejecutar comandos anteriores

## Overview
El comando `fc` en Bash se utiliza para listar, editar y ejecutar comandos anteriores en la historia de la terminal. Permite a los usuarios corregir errores o modificar comandos previos sin tener que volver a escribirlos completamente.

## Usage
La sintaxis básica del comando `fc` es la siguiente:

```bash
fc [opciones] [argumentos]
```

## Common Options
- `-l`: Lista los comandos anteriores en la historia.
- `-r`: Lista los comandos en orden inverso.
- `-s`: Ejecuta el último comando sin abrir un editor.
- `-n`: No muestra el número de línea al listar los comandos.

## Common Examples
1. **Listar los últimos 10 comandos:**
   ```bash
   fc -l -n -10
   ```

2. **Editar el último comando en el editor predeterminado:**
   ```bash
   fc
   ```

3. **Ejecutar el último comando sin editar:**
   ```bash
   fc -s
   ```

4. **Listar los últimos 5 comandos en orden inverso:**
   ```bash
   fc -r -l -5
   ```

5. **Editar un comando específico de la historia (por ejemplo, el número 20):**
   ```bash
   fc 20
   ```

## Tips
- Utiliza `fc` para corregir rápidamente errores en comandos sin necesidad de volver a escribirlos.
- Familiarízate con el uso de editores como `nano` o `vim` para una edición más eficiente de los comandos.
- Recuerda que `fc` solo funciona con los comandos que están en la historia de la sesión actual de Bash.