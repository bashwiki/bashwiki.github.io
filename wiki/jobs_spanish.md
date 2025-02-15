# [리눅스] Bash jobs 사용법

## Overview
El comando `jobs` en Bash se utiliza para mostrar el estado de los trabajos en segundo plano y en primer plano que se están ejecutando en la sesión actual del terminal. Este comando es especialmente útil para los desarrolladores y administradores de sistemas que necesitan gestionar múltiples procesos simultáneamente. Proporciona información sobre los trabajos que se han iniciado en la sesión actual, permitiendo a los usuarios identificar cuáles están en ejecución, detenidos o finalizados.

## Usage
La sintaxis básica del comando `jobs` es la siguiente:

```bash
jobs [options]
```

### Opciones Comunes
- `-l`: Muestra el número de proceso (PID) junto con el estado del trabajo.
- `-n`: Muestra solo los trabajos que han cambiado de estado desde la última vez que se ejecutó el comando.
- `-p`: Muestra solo los números de proceso de los trabajos.

## Examples
### Ejemplo 1: Listar trabajos en segundo plano
Para ver todos los trabajos en segundo plano y su estado, simplemente puedes ejecutar:

```bash
jobs
```

Esto mostrará una lista de trabajos con su número de trabajo y su estado (ejecutándose, detenido, etc.).

### Ejemplo 2: Listar trabajos con PID
Si deseas obtener más información, incluyendo el PID de cada trabajo, puedes usar la opción `-l`:

```bash
jobs -l
```

Esto mostrará una lista similar, pero incluirá el PID de cada trabajo, lo que puede ser útil para la gestión de procesos.

## Tips
- Utiliza `jobs` junto con otros comandos como `fg` y `bg` para gestionar trabajos. Por ejemplo, puedes llevar un trabajo al primer plano con `fg %1`, donde `%1` es el número del trabajo que deseas mover.
- Si un trabajo se ha detenido, puedes reanudarlo en segundo plano usando `bg %1`.
- Recuerda que el comando `jobs` solo muestra trabajos de la sesión actual del terminal. Si cierras la terminal, perderás el estado de esos trabajos.

Con estos conocimientos, podrás utilizar el comando `jobs` de manera efectiva para gestionar tus procesos en Bash.