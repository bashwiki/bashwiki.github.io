# [Linux] Bash cmake Uso: Herramienta para la construcción de proyectos

## Overview
El comando `cmake` es una herramienta de automatización de construcción que utiliza archivos de configuración para generar archivos de construcción específicos de la plataforma. Permite a los desarrolladores compilar y gestionar proyectos de software de manera eficiente, facilitando la configuración de entornos de desarrollo.

## Usage
La sintaxis básica del comando `cmake` es la siguiente:

```bash
cmake [opciones] [argumentos]
```

## Common Options
- `-S <directorio>`: Especifica el directorio fuente donde se encuentra el código fuente del proyecto.
- `-B <directorio>`: Especifica el directorio de construcción donde se generarán los archivos de construcción.
- `-G <generador>`: Especifica el generador de construcción a utilizar (por ejemplo, "Unix Makefiles" o "Ninja").
- `-D <variable>=<valor>`: Define una variable de configuración que puede ser utilizada en el archivo CMakeLists.txt.

## Common Examples
1. **Crear un directorio de construcción y generar archivos de construcción**:
   ```bash
   cmake -S . -B build
   ```

2. **Especificar un generador de construcción**:
   ```bash
   cmake -S . -B build -G "Unix Makefiles"
   ```

3. **Definir una variable de configuración**:
   ```bash
   cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
   ```

4. **Construir el proyecto después de la configuración**:
   ```bash
   cmake --build build
   ```

## Tips
- Siempre es recomendable crear un directorio de construcción separado para mantener el código fuente limpio y organizado.
- Utiliza la opción `-D` para personalizar la configuración de tu proyecto según tus necesidades específicas.
- Revisa el archivo `CMakeLists.txt` de tu proyecto para entender qué variables y opciones puedes configurar.