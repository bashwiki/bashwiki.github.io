# [Linux] Bash fg Uso equivalente: Traer un proceso al primer plano

## Overview
El comando `fg` en Bash se utiliza para llevar un proceso que se está ejecutando en segundo plano al primer plano. Esto es útil cuando deseas interactuar con un proceso que previamente has suspendido o enviado a segundo plano.

## Usage
La sintaxis básica del comando `fg` es la siguiente:

```bash
fg [opciones] [número de trabajo]
```

## Common Options
- **%n**: Especifica el trabajo que deseas llevar al primer plano, donde `n` es el número del trabajo.
- **+**: Lleva el trabajo más reciente al primer plano.
- **-**: Lleva el trabajo anterior al más reciente al primer plano.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `fg`:

1. **Llevar el trabajo más reciente al primer plano**:
   ```bash
   fg
   ```

2. **Llevar un trabajo específico al primer plano** (por ejemplo, el trabajo número 1):
   ```bash
   fg %1
   ```

3. **Llevar el trabajo anterior al más reciente al primer plano**:
   ```bash
   fg -
   ```

4. **Llevar un trabajo específico utilizando su nombre** (si el trabajo se llama `my_script.sh`):
   ```bash
   fg %my_script.sh
   ```

## Tips
- Asegúrate de que el proceso que deseas llevar al primer plano esté en segundo plano; de lo contrario, el comando `fg` no tendrá efecto.
- Puedes ver la lista de trabajos en segundo plano utilizando el comando `jobs`, lo que te ayudará a identificar qué trabajos puedes traer al primer plano.
- Si necesitas detener un proceso en primer plano, puedes usar `Ctrl + Z` para suspenderlo y luego usar `fg` para reanudarlo cuando lo necesites.