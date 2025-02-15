# [리눅스] Bash top 사용법

## Overview
El comando `top` es una herramienta de monitorización en tiempo real que muestra los procesos que se están ejecutando en el sistema. Su propósito principal es proporcionar una vista dinámica y actualizada del uso de la CPU, la memoria y otros recursos del sistema, permitiendo a los usuarios identificar procesos que consumen muchos recursos y gestionar el rendimiento del sistema de manera efectiva.

## Usage
La sintaxis básica del comando `top` es la siguiente:

```bash
top [opciones]
```

Algunas de las opciones más comunes que se pueden utilizar con `top` son:

- `-d <segundos>`: Establece el intervalo de actualización en segundos. Por defecto, `top` se actualiza cada 3 segundos.
- `-p <PID>`: Muestra solo el proceso con el identificador de proceso (PID) especificado.
- `-u <usuario>`: Filtra y muestra solo los procesos que pertenecen al usuario especificado.

## Examples
Aquí hay algunos ejemplos prácticos de cómo usar el comando `top`:

1. Para iniciar `top` con la actualización cada 5 segundos:

   ```bash
   top -d 5
   ```

2. Para mostrar solo los procesos de un usuario específico, por ejemplo, "john":

   ```bash
   top -u john
   ```

3. Para monitorear un proceso específico, por ejemplo, con PID 1234:

   ```bash
   top -p 1234
   ```

## Tips
- Para salir de la interfaz de `top`, simplemente presiona `q`.
- Puedes ordenar los procesos por diferentes columnas presionando las teclas correspondientes mientras `top` está en ejecución (por ejemplo, `M` para ordenar por uso de memoria).
- Utiliza la tecla `h` dentro de `top` para acceder a la ayuda y ver una lista de comandos y atajos disponibles.
- Considera usar `htop`, una versión mejorada de `top`, que ofrece una interfaz más amigable y opciones de navegación más intuitivas.