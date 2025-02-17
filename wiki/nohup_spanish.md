# [Linux] Bash nohup uso equivalente: Ejecutar comandos sin interrupciones

## Overview
El comando `nohup` se utiliza en sistemas Unix y Linux para ejecutar procesos que no se detendrán incluso si la sesión de terminal se cierra. Esto es especialmente útil para ejecutar tareas largas o scripts que deben continuar funcionando en segundo plano.

## Usage
La sintaxis básica del comando `nohup` es la siguiente:

```bash
nohup [opciones] [argumentos]
```

## Common Options
- `&`: Ejecuta el comando en segundo plano.
- `-h`: Muestra la ayuda del comando.
- `-v`: Muestra la versión del comando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `nohup`:

1. Ejecutar un script en segundo plano:
   ```bash
   nohup ./mi_script.sh &
   ```

2. Ejecutar un comando y redirigir la salida a un archivo:
   ```bash
   nohup ls -l > salida.txt &
   ```

3. Ejecutar un proceso de larga duración:
   ```bash
   nohup python mi_programa.py &
   ```

4. Ejecutar un comando y asegurarse de que se ejecute incluso si se cierra la terminal:
   ```bash
   nohup ping google.com &
   ```

## Tips
- Siempre redirige la salida estándar y de error a un archivo para evitar que se pierda información.
- Usa `jobs` para ver los procesos en segundo plano y `fg` para traerlos de vuelta al primer plano si es necesario.
- Considera usar `disown` después de ejecutar un comando con `nohup` para desvincularlo de la terminal.