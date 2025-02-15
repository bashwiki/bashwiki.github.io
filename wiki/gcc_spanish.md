# [리눅스] Bash gcc 사용법

## Overview
El comando `gcc` (GNU Compiler Collection) es un compilador de código abierto que se utiliza para compilar programas escritos en lenguajes como C, C++ y otros. Su propósito principal es transformar el código fuente en un archivo ejecutable que pueda ser ejecutado por el sistema operativo. `gcc` es ampliamente utilizado en el desarrollo de software y es una herramienta fundamental para ingenieros y desarrolladores que trabajan en entornos de programación en C y C++.

## Usage
La sintaxis básica del comando `gcc` es la siguiente:

```bash
gcc [opciones] archivo_fuente.c -o archivo_salida
```

### Opciones Comunes
- `-o archivo_salida`: Especifica el nombre del archivo ejecutable que se generará. Si no se proporciona, el archivo por defecto se llamará `a.out`.
- `-Wall`: Activa todas las advertencias recomendadas. Es útil para detectar posibles problemas en el código.
- `-g`: Incluye información de depuración en el archivo ejecutable, lo que facilita el uso de depuradores como `gdb`.
- `-O`: Activa optimizaciones en el código generado. Se pueden especificar niveles de optimización como `-O1`, `-O2`, o `-O3`.

## Examples
### Ejemplo 1: Compilación básica
Para compilar un archivo fuente llamado `programa.c` y generar un ejecutable llamado `programa`, puedes usar el siguiente comando:

```bash
gcc programa.c -o programa
```

### Ejemplo 2: Compilación con advertencias y depuración
Si deseas compilar `programa.c` con advertencias activadas y con información de depuración, puedes usar:

```bash
gcc -Wall -g programa.c -o programa
```

## Tips
- Siempre es recomendable usar la opción `-Wall` para estar al tanto de posibles problemas en el código.
- Si trabajas en proyectos más grandes, considera usar un sistema de construcción como `Makefile` para gestionar la compilación de múltiples archivos fuente.
- Mantén tu entorno de desarrollo actualizado para aprovechar las últimas mejoras y correcciones de errores en `gcc`.
- Familiarízate con las opciones de optimización, ya que pueden tener un impacto significativo en el rendimiento de tu aplicación.