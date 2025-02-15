# [리눅스] Bash hash 사용법

## Overview
El comando `hash` en Bash se utiliza para gestionar la tabla de búsqueda de comandos. Su propósito principal es almacenar la ubicación de los comandos ejecutados para acelerar su búsqueda en futuras invocaciones. Cuando ejecutas un comando, Bash lo busca en los directorios especificados en la variable de entorno `PATH`. Al usar `hash`, puedes evitar que Bash vuelva a buscar la ubicación de un comando si ya ha sido ejecutado anteriormente, lo que mejora la eficiencia.

## Usage
La sintaxis básica del comando `hash` es la siguiente:

```bash
hash [opciones] [comando]
```

### Opciones comunes:
- `-r`: Borra la tabla de hash, lo que obliga a Bash a volver a buscar la ubicación de todos los comandos la próxima vez que se ejecuten.
- `-p`: Permite especificar una ruta para un comando. Esto agrega o actualiza la entrada en la tabla de hash con la ruta proporcionada.
- `-l`: Muestra la tabla de hash actual, listando los comandos y sus ubicaciones.

## Examples

### Ejemplo 1: Mostrar la tabla de hash
Para ver la tabla de hash actual, simplemente ejecuta:

```bash
hash -l
```

Este comando mostrará todos los comandos que han sido almacenados en la tabla de hash junto con sus rutas.

### Ejemplo 2: Limpiar la tabla de hash
Si deseas limpiar la tabla de hash para que Bash vuelva a buscar los comandos, utiliza:

```bash
hash -r
```

Este comando eliminará todas las entradas de la tabla de hash, lo que puede ser útil si has cambiado la ubicación de un comando o si deseas asegurarte de que estás utilizando la versión más reciente de un comando.

## Tips
- Utiliza `hash -l` regularmente para verificar qué comandos están almacenados en la tabla de hash, especialmente si trabajas con múltiples versiones de herramientas.
- Si cambias la ubicación de un comando o instalas una nueva versión, recuerda ejecutar `hash -r` para asegurarte de que estás utilizando la versión correcta.
- La gestión de la tabla de hash puede ser especialmente útil en entornos de desarrollo donde se instalan y desinstalan frecuentemente herramientas y comandos.