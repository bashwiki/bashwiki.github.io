# [리눅스] Bash make 사용법

## Overview
El comando `make` es una herramienta de automatización de compilación que se utiliza principalmente para gestionar la construcción de proyectos de software. Su propósito principal es leer un archivo llamado `Makefile`, que contiene reglas y dependencias, y ejecutar las instrucciones necesarias para compilar y enlazar los archivos de un proyecto. Esto permite a los desarrolladores simplificar el proceso de construcción y asegurarse de que solo se recompilan los archivos que han cambiado.

## Usage
La sintaxis básica del comando `make` es la siguiente:

```bash
make [opciones] [objetivo]
```

### Opciones comunes:
- `-f <archivo>`: Especifica un archivo `Makefile` diferente al predeterminado (que es `Makefile` o `makefile`).
- `-j <n>`: Permite la ejecución paralela de tareas, donde `<n>` es el número de procesos que se ejecutarán simultáneamente.
- `-B`: Fuerza la recompilación de todos los objetivos, independientemente de si han cambiado o no.
- `-n`: Muestra las acciones que se llevarían a cabo sin ejecutarlas realmente (modo de prueba).
- `-s`: Suprime la salida de comandos, mostrando solo los errores.

## Examples
### Ejemplo 1: Compilación básica
Supongamos que tienes un proyecto con un archivo `Makefile` que define cómo compilar un programa llamado `mi_programa`. Para compilar el programa, simplemente ejecutas:

```bash
make
```

Esto ejecutará las instrucciones definidas en el `Makefile` para compilar `mi_programa`.

### Ejemplo 2: Compilación paralela
Si deseas acelerar el proceso de compilación utilizando múltiples núcleos de CPU, puedes usar la opción `-j`. Por ejemplo, para usar 4 núcleos, puedes ejecutar:

```bash
make -j4
```

Esto permitirá que `make` ejecute varias tareas de compilación al mismo tiempo.

## Tips
- Asegúrate de que tu `Makefile` esté bien estructurado y documentado para facilitar la comprensión y el mantenimiento.
- Utiliza la opción `-n` para verificar qué comandos se ejecutarían sin realizar cambios, lo que es útil para la depuración.
- Si trabajas en un entorno de desarrollo colaborativo, considera incluir un `Makefile` en tu repositorio para que otros desarrolladores puedan compilar el proyecto fácilmente.
- Mantén tus dependencias actualizadas en el `Makefile` para evitar recompilaciones innecesarias y mejorar la eficiencia del proceso de construcción.