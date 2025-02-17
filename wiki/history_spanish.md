# [Linux] Bash history uso: Muestra el historial de comandos ejecutados

## Overview
El comando `history` en Bash se utiliza para mostrar el historial de comandos que has ejecutado en la terminal. Esto te permite revisar y reutilizar comandos anteriores, lo que puede aumentar tu eficiencia al trabajar en la línea de comandos.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
history [opciones] [número]
```

## Common Options
- `-c`: Borra el historial actual.
- `-d offset`: Elimina la entrada en la posición especificada por `offset`.
- `n`: Muestra las últimas `n` entradas del historial.

## Common Examples
Aquí hay algunos ejemplos prácticos de cómo usar el comando `history`:

1. **Mostrar todo el historial de comandos:**
   ```bash
   history
   ```

2. **Mostrar las últimas 10 entradas del historial:**
   ```bash
   history 10
   ```

3. **Eliminar una entrada específica del historial (por ejemplo, la entrada en la posición 5):**
   ```bash
   history -d 5
   ```

4. **Borrar todo el historial:**
   ```bash
   history -c
   ```

## Tips
- Utiliza `!n` para ejecutar el comando en la posición `n` del historial. Por ejemplo, `!5` ejecutará el quinto comando de tu historial.
- Puedes buscar en el historial presionando `Ctrl + r` y luego escribiendo parte del comando que buscas.
- Considera mantener tu historial limpio eliminando comandos innecesarios con `history -d` para evitar confusiones en el futuro.