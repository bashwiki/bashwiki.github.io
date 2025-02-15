# [리눅스] Bash times 사용법

## Overview
El comando `times` en Bash se utiliza para mostrar el tiempo de CPU utilizado por el shell y sus procesos hijos. Este comando es útil para los ingenieros y desarrolladores que desean analizar el rendimiento de sus scripts o comandos ejecutados en el entorno de shell. Proporciona información sobre el tiempo total de usuario y el tiempo total del sistema, lo que permite a los usuarios identificar cuántos recursos de CPU han consumido sus procesos.

## Usage
La sintaxis básica del comando `times` es la siguiente:

```bash
times
```

No hay opciones o argumentos adicionales que se puedan pasar al comando `times`. Simplemente se ejecuta tal cual para obtener la información deseada.

## Examples
### Ejemplo 1: Uso básico
Para ver el tiempo de CPU utilizado por el shell actual y sus procesos hijos, simplemente ejecuta el comando:

```bash
times
```

La salida mostrará dos valores: el tiempo de CPU en modo usuario y el tiempo de CPU en modo sistema, en segundos.

### Ejemplo 2: Análisis después de ejecutar un script
Supongamos que tienes un script llamado `mi_script.sh`. Puedes ejecutar el script y luego usar `times` para ver cuánto tiempo de CPU ha utilizado:

```bash
bash mi_script.sh
times
```

Esto te dará una idea clara de los recursos de CPU que ha consumido tu script.

## Tips
- **Uso en scripts**: Considera incluir el comando `times` al final de tus scripts para registrar el tiempo de CPU utilizado. Esto puede ser útil para la optimización y el análisis de rendimiento.
- **Comparación de rendimiento**: Ejecuta diferentes versiones de un script y usa `times` para comparar el tiempo de CPU utilizado, lo que te ayudará a identificar qué cambios mejoran el rendimiento.
- **No olvides el contexto**: Recuerda que `times` solo muestra el tiempo de CPU utilizado por el shell y sus procesos hijos, por lo que no incluirá el tiempo de otros procesos que puedan estar ejecutándose en el sistema.