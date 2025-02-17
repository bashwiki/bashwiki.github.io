# [Linux] Bash tput uso: Controlar la salida de terminal

## Overview
El comando `tput` se utiliza en Bash para controlar la salida en la terminal, permitiendo modificar el formato del texto, cambiar colores y manipular el cursor. Es especialmente útil para crear interfaces de usuario más amigables en la línea de comandos.

## Usage
La sintaxis básica del comando `tput` es la siguiente:

```
tput [opciones] [argumentos]
```

## Common Options
- `setaf [n]`: Establece el color de primer plano (texto) a un color específico, donde `n` es el número del color.
- `setab [n]`: Establece el color de fondo a un color específico.
- `bold`: Activa el texto en negrita.
- `underline`: Activa el subrayado del texto.
- `clear`: Limpia la pantalla de la terminal.
- `cup [y] [x]`: Mueve el cursor a la posición especificada por las coordenadas `y` (línea) y `x` (columna).

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `tput`:

1. **Cambiar el color del texto a rojo:**
   ```bash
   tput setaf 1
   echo "Este texto es rojo"
   ```

2. **Cambiar el color de fondo a azul y el texto a blanco:**
   ```bash
   tput setab 4
   tput setaf 7
   echo "Texto blanco sobre fondo azul"
   ```

3. **Activar negrita y subrayado:**
   ```bash
   tput bold
   tput underline
   echo "Este texto es negrita y subrayado"
   tput sgr0  # Restablecer atributos
   ```

4. **Limpiar la pantalla:**
   ```bash
   tput clear
   ```

5. **Mover el cursor a la posición (5,10):**
   ```bash
   tput cup 5 10
   echo "Texto en la línea 5, columna 10"
   ```

## Tips
- Siempre restablece los atributos de la terminal al final de tu script usando `tput sgr0` para evitar que los cambios persistan.
- Experimenta con diferentes números para los colores, ya que pueden variar según el terminal que estés utilizando.
- Usa `tput` en scripts para mejorar la presentación de la salida y hacerla más interactiva.