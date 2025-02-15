# [리눅스] Bash g++ 사용법

## Overview
El comando `g++` es el compilador de C++ que forma parte del proyecto GNU Compiler Collection (GCC). Su propósito principal es compilar programas escritos en el lenguaje de programación C++. `g++` convierte el código fuente en archivos ejecutables, permitiendo a los desarrolladores ejecutar sus aplicaciones en sistemas operativos compatibles.

## Usage
La sintaxis básica del comando `g++` es la siguiente:

```bash
g++ [opciones] archivo1.cpp archivo2.cpp -o nombre_ejecutable
```

### Opciones Comunes
- `-o nombre_ejecutable`: Especifica el nombre del archivo ejecutable que se generará. Si no se proporciona, el ejecutable se llamará `a.out` por defecto.
- `-Wall`: Activa todas las advertencias recomendadas, lo que ayuda a identificar problemas potenciales en el código.
- `-g`: Incluye información de depuración en el ejecutable, útil para el uso con depuradores como `gdb`.
- `-std=c++11`: Especifica la versión del estándar de C++ que se utilizará. Puedes cambiar `c++11` por `c++14`, `c++17`, etc., según sea necesario.

## Examples
### Ejemplo 1: Compilar un solo archivo
Para compilar un archivo llamado `programa.cpp` y generar un ejecutable llamado `programa`, puedes usar el siguiente comando:

```bash
g++ programa.cpp -o programa
```

### Ejemplo 2: Compilar múltiples archivos
Si tienes varios archivos de código fuente, como `main.cpp` y `funciones.cpp`, puedes compilarlos juntos de la siguiente manera:

```bash
g++ main.cpp funciones.cpp -o mi_programa -Wall
```

Este comando generará un ejecutable llamado `mi_programa` y activará las advertencias recomendadas.

## Tips
- Siempre utiliza la opción `-Wall` para asegurarte de que estás al tanto de posibles problemas en tu código.
- Si estás trabajando en un proyecto grande, considera usar un sistema de construcción como `Makefile` para gestionar la compilación de múltiples archivos de manera más eficiente.
- Aprovecha la opción `-g` durante el desarrollo para facilitar la depuración de tu código.
- Mantén tu código bien organizado y documentado para facilitar la identificación de errores y la colaboración con otros desarrolladores.