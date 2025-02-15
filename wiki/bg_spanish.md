# [리눅스] Bash bg 사용법

## Overview
El comando `bg` en Bash se utiliza para reanudar un trabajo que se ha detenido (suspendido) y ejecutarlo en segundo plano. Esto es útil cuando un proceso necesita continuar ejecutándose sin ocupar la terminal, permitiendo al usuario seguir trabajando en otras tareas en la línea de comandos.

## Usage
La sintaxis básica del comando `bg` es la siguiente:

```bash
bg [job_spec]
```

- `job_spec`: Especifica el trabajo que se desea reanudar. Puede ser el número del trabajo (precedido por un signo de porcentaje, por ejemplo, `%1` para el primer trabajo) o el identificador del proceso.

Si no se proporciona `job_spec`, `bg` reanudará el último trabajo suspendido.

## Examples

### Ejemplo 1: Reanudar el último trabajo suspendido
Supongamos que has ejecutado un comando que se ha suspendido (por ejemplo, presionando `Ctrl+Z`):

```bash
$ sleep 100
^Z
[1]+  Stopped                 sleep 100
```

Para reanudar este trabajo en segundo plano, simplemente ejecuta:

```bash
$ bg
[1]+ sleep 100 &
```

### Ejemplo 2: Reanudar un trabajo específico
Si tienes múltiples trabajos suspendidos, puedes reanudar uno específico. Primero, lista los trabajos activos:

```bash
$ jobs
[1]+  Stopped                 sleep 100
[2]-  Stopped                 nano
```

Para reanudar el segundo trabajo (en este caso, `nano`), utiliza:

```bash
$ bg %2
[2]- nano &
```

## Tips
- Utiliza el comando `jobs` para ver una lista de trabajos suspendidos y sus estados antes de usar `bg`.
- Recuerda que los trabajos en segundo plano pueden seguir ejecutándose incluso si cierras la terminal, pero si deseas que continúen ejecutándose después de cerrar la sesión, considera usar `nohup` o `disown`.
- Puedes combinar `bg` con otros comandos como `fg` para alternar entre trabajos en primer plano y en segundo plano según sea necesario.