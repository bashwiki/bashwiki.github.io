# [Linux] Bash who uso equivalente: Muestra quién está conectado al sistema

## Overview
El comando `who` en Bash se utiliza para mostrar una lista de los usuarios que están actualmente conectados al sistema. Proporciona información sobre cada usuario, como su nombre de usuario, la terminal que están utilizando, la fecha y hora de su inicio de sesión, y en algunos casos, la dirección IP desde la que se han conectado.

## Usage
La sintaxis básica del comando `who` es la siguiente:

```
who [opciones] [argumentos]
```

## Common Options
Aquí hay algunas opciones comunes que puedes usar con el comando `who`:

- `-a`: Muestra toda la información disponible, incluyendo usuarios, procesos y más.
- `-b`: Muestra la última vez que el sistema fue iniciado.
- `-q`: Muestra solo los nombres de los usuarios conectados y el número total de usuarios.
- `-H`: Muestra los encabezados de las columnas en la salida.

## Common Examples
A continuación, se presentan algunos ejemplos prácticos del uso del comando `who`:

1. **Mostrar todos los usuarios conectados:**
   ```bash
   who
   ```

2. **Mostrar información detallada sobre los usuarios conectados:**
   ```bash
   who -a
   ```

3. **Mostrar la última vez que se inició el sistema:**
   ```bash
   who -b
   ```

4. **Mostrar solo los nombres de los usuarios conectados:**
   ```bash
   who -q
   ```

5. **Mostrar encabezados de columnas:**
   ```bash
   who -H
   ```

## Tips
- Utiliza `who -q` si solo necesitas saber cuántos usuarios están conectados sin detalles adicionales.
- Combina `who` con otros comandos como `grep` para filtrar resultados específicos, por ejemplo, para encontrar un usuario en particular.
- Recuerda que el comando `who` puede requerir permisos de usuario adecuados para mostrar información completa en sistemas más restringidos.