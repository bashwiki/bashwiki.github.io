# [Linux] Bash bg Uso equivalente: Mover trabajos a segundo plano

## Overview
El comando `bg` en Bash se utiliza para reanudar trabajos detenidos y moverlos al segundo plano. Esto permite que los procesos continúen ejecutándose sin ocupar la terminal, lo que es útil para realizar múltiples tareas simultáneamente.

## Usage
La sintaxis básica del comando `bg` es la siguiente:

```bash
bg [opciones] [número de trabajo]
```

## Common Options
- `-l`: Muestra la lista de trabajos en segundo plano con sus números de trabajo.
- `-n`: No muestra mensajes de estado al mover trabajos al segundo plano.

## Common Examples

1. **Mover un trabajo detenido al segundo plano**
   Supongamos que tienes un trabajo detenido (por ejemplo, un proceso de edición de texto). Puedes moverlo al segundo plano con:
   ```bash
   bg %1
   ```
   Aquí, `%1` representa el número del trabajo que deseas mover.

2. **Reanudar el último trabajo detenido en segundo plano**
   Si solo deseas reanudar el último trabajo que detuviste, puedes usar:
   ```bash
   bg
   ```

3. **Listar trabajos en segundo plano**
   Para ver todos los trabajos en segundo plano, puedes usar:
   ```bash
   jobs
   ```

4. **Mover un trabajo específico al segundo plano**
   Si tienes varios trabajos y deseas mover uno específico, primero verifica la lista de trabajos con `jobs`, luego usa `bg` con el número correspondiente:
   ```bash
   bg %2
   ```

## Tips
- Siempre verifica el estado de tus trabajos con el comando `jobs` antes de usar `bg`.
- Puedes combinar `bg` con `disown` para desvincular un trabajo del terminal, permitiendo que continúe ejecutándose incluso si cierras la sesión.
- Utiliza `fg` si necesitas llevar un trabajo de nuevo al primer plano para interactuar con él.