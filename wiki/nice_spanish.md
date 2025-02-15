# [리눅스] Bash nice 사용법

## Overview
El comando `nice` en Bash se utiliza para ejecutar procesos con una prioridad ajustada. Su propósito principal es permitir que los usuarios especifiquen la prioridad de un proceso al momento de ejecutarlo, lo que puede ser útil en sistemas multitarea para gestionar el uso de recursos. Los procesos con una prioridad más baja (valores más altos) recibirán menos tiempo de CPU en comparación con los procesos de mayor prioridad (valores más bajos).

## Usage
La sintaxis básica del comando `nice` es la siguiente:

```bash
nice [opciones] [comando]
```

### Opciones comunes:
- `-n, --adjustment=N`: Establece el valor de ajuste de la prioridad. El valor por defecto es 10. Un valor negativo aumenta la prioridad, mientras que un valor positivo la disminuye.
- `-h, --help`: Muestra la ayuda sobre el uso del comando.
- `--version`: Muestra la versión del comando.

## Examples
### Ejemplo 1: Ejecutar un proceso con prioridad baja
Para ejecutar un script llamado `mi_script.sh` con una prioridad baja, puedes usar el siguiente comando:

```bash
nice -n 19 ./mi_script.sh
```

En este caso, `mi_script.sh` se ejecutará con una prioridad de 19, lo que significa que tendrá menos acceso a la CPU en comparación con otros procesos.

### Ejemplo 2: Ajustar la prioridad de un comando existente
Si deseas ejecutar un comando como `gzip` con una prioridad más alta, puedes hacerlo de la siguiente manera:

```bash
nice -n -5 gzip archivo.txt
```

Aquí, el comando `gzip` se ejecutará con una prioridad de -5, lo que le dará preferencia sobre otros procesos de menor prioridad.

## Tips
- Utiliza `nice` para evitar que procesos intensivos en recursos afecten el rendimiento de otros procesos críticos en el sistema.
- Puedes verificar la prioridad de los procesos en ejecución utilizando el comando `ps` junto con la opción `-o` para mostrar la columna de prioridad.
- Recuerda que solo los usuarios con privilegios adecuados pueden establecer prioridades negativas (mayor prioridad).