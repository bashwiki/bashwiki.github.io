# [Linux] Bash shopt Uso: Configuración de opciones de shell

## Overview
El comando `shopt` en Bash se utiliza para habilitar o deshabilitar opciones específicas del shell. Estas opciones pueden modificar el comportamiento del shell y personalizar la experiencia del usuario en la línea de comandos.

## Usage
La sintaxis básica del comando `shopt` es la siguiente:

```bash
shopt [options] [arguments]
```

## Common Options
- `-s`: Habilita una opción.
- `-u`: Deshabilita una opción.
- `-p`: Muestra las opciones actuales y su estado (habilitada o deshabilitada).

## Common Examples
1. **Habilitar la opción de globbing extendido:**
   ```bash
   shopt -s extglob
   ```
   Esto permite el uso de patrones de coincidencia más complejos en los comandos de globbing.

2. **Deshabilitar la opción de globbing extendido:**
   ```bash
   shopt -u extglob
   ```

3. **Mostrar el estado de todas las opciones:**
   ```bash
   shopt -p
   ```
   Este comando lista todas las opciones de `shopt` junto con su estado actual.

4. **Habilitar la opción de autocd:**
   ```bash
   shopt -s autocd
   ```
   Con esta opción habilitada, puedes cambiar a un directorio simplemente escribiendo su nombre sin necesidad de usar el comando `cd`.

## Tips
- Revisa las opciones disponibles con `shopt -p` para conocer qué configuraciones puedes ajustar.
- Considera crear un archivo de configuración (como `.bashrc`) para habilitar opciones que desees utilizar de manera constante.
- Experimenta con las opciones en un entorno de prueba antes de aplicarlas en tu entorno de trabajo habitual para evitar comportamientos inesperados.