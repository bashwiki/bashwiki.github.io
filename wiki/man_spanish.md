# [Linux] Bash man uso: Muestra la documentación de comandos

## Overview
El comando `man` en Bash se utiliza para mostrar el manual de otros comandos del sistema. Proporciona información detallada sobre cómo usar un comando específico, sus opciones y ejemplos de uso.

## Usage
La sintaxis básica del comando `man` es la siguiente:

```bash
man [opciones] [argumentos]
```

## Common Options
- `-k`: Busca en las páginas del manual por una palabra clave.
- `-f`: Muestra una breve descripción de un comando.
- `-a`: Muestra todas las páginas del manual disponibles para un comando, en lugar de solo la primera.

## Common Examples
Aquí hay algunos ejemplos prácticos de cómo usar el comando `man`:

1. Para ver la página del manual del comando `ls`:
   ```bash
   man ls
   ```

2. Para buscar una palabra clave, por ejemplo, "copy":
   ```bash
   man -k copy
   ```

3. Para obtener una breve descripción del comando `cp`:
   ```bash
   man -f cp
   ```

4. Para ver todas las páginas del manual relacionadas con `tar`:
   ```bash
   man -a tar
   ```

## Tips
- Usa la tecla `q` para salir de la página del manual.
- Puedes navegar por el manual usando las teclas de flecha o `Page Up` y `Page Down`.
- Si no estás seguro de cómo se escribe un comando, puedes usar `man -k` para buscarlo por palabra clave.