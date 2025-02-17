# [Linux] Bash tee Uso: Redirigir la salida a archivos y a la consola

## Overview
El comando `tee` en Bash se utiliza para leer de la entrada estándar y escribir simultáneamente en la salida estándar y en uno o más archivos. Esto es útil cuando deseas ver la salida de un comando en la consola mientras también la guardas en un archivo.

## Usage
La sintaxis básica del comando `tee` es la siguiente:

```bash
tee [opciones] [archivos]
```

## Common Options
- `-a`, `--append`: Añade la salida al final del archivo en lugar de sobrescribirlo.
- `-i`, `--ignore-interrupts`: Ignora las señales de interrupción.
- `-p`, `--output-error`: Controla cómo se manejan los errores de escritura en los archivos de salida.

## Common Examples

1. **Guardar la salida de un comando en un archivo:**
   ```bash
   ls -l | tee listado.txt
   ```
   Este comando lista los archivos en el directorio actual y guarda la salida en `listado.txt`.

2. **Añadir la salida a un archivo existente:**
   ```bash
   echo "Nueva entrada" | tee -a listado.txt
   ```
   Aquí, se añade "Nueva entrada" al final de `listado.txt` sin borrar su contenido anterior.

3. **Ver la salida en la consola y en múltiples archivos:**
   ```bash
   echo "Hola, mundo" | tee archivo1.txt archivo2.txt
   ```
   Este comando muestra "Hola, mundo" en la consola y lo guarda en `archivo1.txt` y `archivo2.txt`.

4. **Ignorar interrupciones mientras se escribe en un archivo:**
   ```bash
   cat archivo.txt | tee -i salida.txt
   ```
   Este comando lee `archivo.txt` y escribe en `salida.txt`, ignorando cualquier señal de interrupción.

## Tips
- Utiliza la opción `-a` si deseas conservar el contenido previo de un archivo y agregarle nueva información.
- Recuerda que `tee` puede ser útil en scripts para registrar la salida de comandos mientras se ejecutan.
- Puedes combinar `tee` con otros comandos para crear flujos de trabajo más complejos, como redirigir la salida de un script a un archivo mientras lo visualizas en tiempo real.