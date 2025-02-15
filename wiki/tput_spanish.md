# [리눅스] Bash tput 사용법

## Overview
El comando `tput` se utiliza en sistemas Unix y Linux para interactuar con el sistema de control de terminal. Su propósito principal es permitir a los usuarios y desarrolladores manipular las propiedades de la terminal, como el color del texto, el formato y el movimiento del cursor. Esto es especialmente útil para crear interfaces de usuario en la línea de comandos más atractivas y funcionales.

## Usage
La sintaxis básica del comando `tput` es la siguiente:

```bash
tput [opción] [argumento]
```

Algunas de las opciones más comunes incluyen:

- `setaf`: Establece el color del texto (foreground).
- `setab`: Establece el color del fondo (background).
- `clear`: Limpia la pantalla de la terminal.
- `cup`: Mueve el cursor a una posición específica (fila, columna).
- `bold`: Establece el texto en negrita.
- `rev`: Invierte los colores del texto y el fondo.

## Examples
Aquí hay un par de ejemplos prácticos de cómo utilizar `tput` en la línea de comandos:

1. **Cambiar el color del texto a rojo**:
   ```bash
   tput setaf 1
   echo "Este texto es rojo"
   tput sgr0  # Restablece los atributos de la terminal
   ```

2. **Limpiar la pantalla y mover el cursor a la posición (5, 10)**:
   ```bash
   tput clear
   tput cup 5 10
   echo "Texto en la posición (5, 10)"
   ```

## Tips
- Siempre es una buena práctica restablecer los atributos de la terminal después de usar `tput` para evitar que los cambios de formato persistan. Puedes hacerlo utilizando `tput sgr0`.
- Para obtener una lista completa de capacidades que puedes usar con `tput`, puedes ejecutar `man terminfo` o `infocmp` para ver las capacidades de tu terminal específica.
- Experimenta con diferentes combinaciones de colores y formatos para encontrar la mejor apariencia para tus scripts y aplicaciones de terminal.