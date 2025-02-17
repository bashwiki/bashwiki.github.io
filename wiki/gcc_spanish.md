# [Linux] Bash gcc Uso: Compilar código fuente en C y C++

## Overview
El comando `gcc` (GNU Compiler Collection) es un compilador utilizado para convertir código fuente escrito en lenguajes como C y C++ en código ejecutable. Es una herramienta fundamental en el desarrollo de software en sistemas operativos basados en Unix.

## Usage
La sintaxis básica del comando `gcc` es la siguiente:

```bash
gcc [opciones] [archivos]
```

## Common Options
Aquí hay algunas opciones comunes que se pueden utilizar con `gcc`:

- `-o nombre`: Especifica el nombre del archivo de salida.
- `-Wall`: Activa todas las advertencias recomendadas.
- `-g`: Incluye información de depuración en el archivo ejecutable.
- `-O`: Activa optimizaciones para mejorar el rendimiento del código.
- `-I ruta`: Añade una ruta de búsqueda para archivos de encabezado.

## Common Examples
A continuación, se presentan algunos ejemplos prácticos del uso de `gcc`:

1. Compilar un archivo fuente simple:
   ```bash
   gcc programa.c -o programa
   ```

2. Compilar con advertencias activadas:
   ```bash
   gcc -Wall programa.c -o programa
   ```

3. Compilar y generar un archivo de depuración:
   ```bash
   gcc -g programa.c -o programa
   ```

4. Compilar múltiples archivos fuente:
   ```bash
   gcc archivo1.c archivo2.c -o programa
   ```

5. Usar optimización al compilar:
   ```bash
   gcc -O2 programa.c -o programa
   ```

## Tips
- Siempre utiliza la opción `-Wall` para detectar posibles problemas en el código.
- Si estás depurando, no olvides incluir la opción `-g` para facilitar el uso de herramientas de depuración como `gdb`.
- Organiza tu código en múltiples archivos y compílalos juntos para mantener una estructura limpia y modular.