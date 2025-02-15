# [리눅스] Bash history 사용법

## Overview
El comando `history` en Bash se utiliza para mostrar el historial de comandos que se han ejecutado en la sesión actual de la terminal. Su propósito principal es permitir a los usuarios revisar y reutilizar comandos anteriores sin tener que volver a escribirlos. Esto es especialmente útil para ingenieros y desarrolladores que trabajan en la línea de comandos, ya que pueden acceder rápidamente a comandos complejos o repetitivos.

## Usage
La sintaxis básica del comando `history` es la siguiente:

```bash
history [n]
```

Donde `n` es un número opcional que especifica cuántos de los últimos comandos se deben mostrar. Si no se proporciona ningún número, se mostrarán todos los comandos del historial.

### Opciones comunes:
- `-c`: Borra el historial de comandos.
- `-d offset`: Elimina el comando en la posición especificada por `offset`.
- `-a`: Añade los comandos de la sesión actual al archivo de historial.
- `-r`: Lee el historial desde el archivo y lo añade a la sesión actual.

## Examples
### Ejemplo 1: Mostrar el historial completo
Para ver todos los comandos ejecutados en la sesión actual, simplemente escribe:

```bash
history
```

Esto mostrará una lista numerada de todos los comandos que has utilizado.

### Ejemplo 2: Mostrar los últimos 5 comandos
Si solo deseas ver los últimos cinco comandos ejecutados, puedes usar:

```bash
history 5
```

Esto mostrará los cinco comandos más recientes en el historial.

## Tips
- **Reutilización de comandos**: Puedes reutilizar un comando del historial usando `!n`, donde `n` es el número del comando en el historial. Por ejemplo, `!100` ejecutará el comando que está en la posición 100.
- **Búsqueda rápida**: Usa `Ctrl + r` para buscar en el historial de comandos de manera interactiva. Esto te permite encontrar y ejecutar comandos anteriores sin tener que desplazarte manualmente por la lista.
- **Personalización del historial**: Puedes ajustar la cantidad de comandos que se guardan en el historial modificando la variable `HISTSIZE` en tu archivo de configuración de Bash (`~/.bashrc`).

El comando `history` es una herramienta poderosa que puede mejorar significativamente la eficiencia en la línea de comandos, permitiendo a los usuarios acceder rápidamente a sus comandos anteriores.