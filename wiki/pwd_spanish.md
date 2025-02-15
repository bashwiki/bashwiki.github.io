# [리눅스] Bash pwd 사용법

## Overview
El comando `pwd` (Print Working Directory) se utiliza en Bash para mostrar la ruta completa del directorio de trabajo actual en el que se encuentra el usuario. Su propósito principal es ayudar a los usuarios a identificar su ubicación dentro del sistema de archivos, lo que es especialmente útil cuando se navega a través de múltiples directorios.

## Usage
La sintaxis básica del comando `pwd` es la siguiente:

```bash
pwd [opciones]
```

### Opciones Comunes
- `-L`: Muestra la ruta lógica del directorio de trabajo actual. Esto es útil si se han utilizado enlaces simbólicos.
- `-P`: Muestra la ruta física del directorio de trabajo actual, resolviendo cualquier enlace simbólico.

Por defecto, `pwd` se ejecuta sin opciones y muestra la ruta lógica.

## Examples
### Ejemplo 1: Uso básico de pwd
Para mostrar la ruta del directorio actual, simplemente ejecuta:

```bash
pwd
```

**Salida esperada:**
```
/home/usuario/proyecto
```

### Ejemplo 2: Uso de opciones
Si deseas ver la ruta física del directorio actual, puedes usar la opción `-P`:

```bash
pwd -P
```

**Salida esperada (dependiendo de la estructura de directorios):**
```
/home/usuario/proyecto
```

## Tips
- Utiliza `pwd` antes de ejecutar comandos que dependan de la ubicación del directorio para asegurarte de que estás en el lugar correcto.
- Combina `pwd` con otros comandos, como `cd`, para verificar tu ubicación después de cambiar de directorio.
- Recuerda que el uso de `pwd -L` es útil cuando trabajas con enlaces simbólicos, ya que te permite ver la ruta que se presenta al usuario, mientras que `pwd -P` te muestra la ruta real en el sistema de archivos.