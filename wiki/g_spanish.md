# [Linux] Bash g++ Uso: Compilar programas en C++

## Overview
El comando `g++` es el compilador de C++ de GNU. Se utiliza para compilar archivos de código fuente escritos en C++ y generar archivos ejecutables. Es una herramienta fundamental para desarrolladores que trabajan en proyectos de software en este lenguaje.

## Usage
La sintaxis básica del comando `g++` es la siguiente:

```bash
g++ [opciones] [archivos]
```

## Common Options
A continuación se presentan algunas opciones comunes que se pueden utilizar con `g++`:

- `-o <archivo>`: Especifica el nombre del archivo ejecutable de salida.
- `-Wall`: Activa todas las advertencias recomendadas.
- `-g`: Genera información de depuración para usar con un depurador.
- `-std=<estándar>`: Especifica el estándar de C++ a utilizar (por ejemplo, `-std=c++11`).
- `-I<directorio>`: Agrega un directorio a la lista de directorios de búsqueda para archivos de encabezado.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `g++`:

1. Compilar un archivo fuente simple:
   ```bash
   g++ programa.cpp
   ```

2. Compilar y especificar un nombre para el archivo ejecutable:
   ```bash
   g++ programa.cpp -o mi_programa
   ```

3. Compilar con advertencias activadas:
   ```bash
   g++ -Wall programa.cpp
   ```

4. Compilar con información de depuración:
   ```bash
   g++ -g programa.cpp -o mi_programa
   ```

5. Compilar utilizando un estándar específico de C++:
   ```bash
   g++ -std=c++17 programa.cpp -o mi_programa
   ```

## Tips
- Siempre utiliza la opción `-Wall` para detectar posibles problemas en tu código.
- Si trabajas en un proyecto grande, considera dividir tu código en múltiples archivos y compílalos juntos.
- Usa la opción `-g` durante el desarrollo para facilitar la depuración.
- Familiarízate con los estándares de C++ y utiliza la opción `-std` para asegurarte de que tu código sea compatible con el estándar deseado.