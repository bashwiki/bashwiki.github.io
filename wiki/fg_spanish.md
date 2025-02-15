# [리눅스] Bash fg 사용법

## Overview
El comando `fg` en Bash se utiliza para reanudar un trabajo que se está ejecutando en segundo plano y llevarlo al primer plano. Esto es especialmente útil cuando se ha suspendido un proceso o se ha enviado a segundo plano y se desea interactuar con él nuevamente. El comando permite a los usuarios gestionar sus trabajos en la terminal de manera más eficiente.

## Usage
La sintaxis básica del comando `fg` es la siguiente:

```bash
fg [job_spec]
```

- `job_spec`: Este argumento es opcional y se utiliza para especificar el trabajo que se desea traer al primer plano. Puede ser el número de trabajo (precedido por un signo de porcentaje, por ejemplo, `%1`) o el nombre del proceso.

Si no se proporciona `job_spec`, `fg` reanuda el último trabajo que se ejecutó en segundo plano.

## Examples
### Ejemplo 1: Traer el último trabajo al primer plano
Supongamos que has ejecutado un comando que se está ejecutando en segundo plano, como un script de Python. Para llevarlo al primer plano, simplemente puedes usar:

```bash
fg
```

### Ejemplo 2: Traer un trabajo específico al primer plano
Si tienes varios trabajos en segundo plano y deseas reanudar uno específico, primero puedes listar los trabajos con el comando `jobs`:

```bash
jobs
```

Esto podría mostrar algo como:

```
[1]+  12345 Stopped    python script.py
[2]-  12346 Stopped    sleep 100
```

Para llevar el primer trabajo al primer plano, usarías:

```bash
fg %1
```

## Tips
- Utiliza el comando `jobs` para ver todos los trabajos en segundo plano y sus estados antes de usar `fg`. Esto te ayudará a identificar cuál trabajo deseas reanudar.
- Si un trabajo se ha suspendido (por ejemplo, presionando `Ctrl+Z`), puedes usar `fg` para reanudarlo sin perder su estado.
- Recuerda que `fg` solo funciona con trabajos que han sido iniciados en la misma sesión de terminal. Si cierras la terminal, los trabajos en segundo plano se perderán.