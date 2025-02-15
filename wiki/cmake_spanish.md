# [리눅스] Bash cmake 사용법

## Overview
El comando `cmake` es una herramienta de construcción de software que utiliza archivos de configuración para generar archivos de construcción en diferentes plataformas. Su propósito principal es simplificar el proceso de compilación de proyectos de software, permitiendo a los desarrolladores definir cómo se debe construir su proyecto de manera portátil y eficiente. `cmake` es especialmente útil para proyectos que necesitan ser compilados en múltiples sistemas operativos y entornos.

## Usage
La sintaxis básica del comando `cmake` es la siguiente:

```bash
cmake [opciones] [ruta]
```

### Opciones Comunes:
- `-S <ruta>`: Especifica la ruta del directorio fuente donde se encuentran los archivos de configuración de CMake.
- `-B <ruta>`: Especifica la ruta del directorio de construcción donde se generarán los archivos de construcción.
- `-G <generador>`: Especifica el generador de construcción a utilizar (por ejemplo, "Unix Makefiles", "Ninja", etc.).
- `-D <variable>=<valor>`: Define una variable de configuración que se puede usar en el archivo CMakeLists.txt.

## Examples
### Ejemplo 1: Construcción básica
Para crear un directorio de construcción y generar los archivos de construcción utilizando el generador de Makefiles, puedes usar el siguiente comando:

```bash
mkdir build
cd build
cmake -S .. -B . -G "Unix Makefiles"
```

En este ejemplo, `cmake` toma los archivos de configuración del directorio padre (`..`) y genera los archivos de construcción en el directorio actual (`.`).

### Ejemplo 2: Definir variables
Si deseas definir una variable durante la configuración, puedes hacerlo de la siguiente manera:

```bash
cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
```

Aquí, se está configurando el proyecto para que se compile en modo "Release".

## Tips
- **Organización de directorios**: Es una buena práctica mantener un directorio de construcción separado del directorio fuente para evitar la mezcla de archivos y facilitar la limpieza.
- **Variables de configuración**: Aprovecha las variables de configuración para personalizar la construcción de tu proyecto sin modificar el archivo CMakeLists.txt.
- **Documentación**: Consulta la documentación oficial de CMake para obtener información detallada sobre las opciones y características avanzadas que pueden ser útiles para tu proyecto.