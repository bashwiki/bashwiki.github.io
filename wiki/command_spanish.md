# [Linux] Bash command uso: [ejecutar comandos en segundo plano]

## Overview
El comando `&` en Bash se utiliza para ejecutar procesos en segundo plano. Esto permite que el usuario continúe utilizando la terminal mientras el proceso se está ejecutando.

## Usage
La sintaxis básica del comando es:

```
comando [opciones] [argumentos] &
```

## Common Options
Aunque el comando `&` en sí no tiene opciones, se puede combinar con otros comandos y opciones. Aquí hay algunas consideraciones:

- `nohup`: Permite que un comando continúe ejecutándose incluso después de cerrar la sesión.
- `disown`: Elimina un trabajo del control de la terminal, permitiendo que continúe ejecutándose en segundo plano.

## Common Examples

1. **Ejecutar un script en segundo plano:**
   ```bash
   ./mi_script.sh &
   ```

2. **Ejecutar un comando con nohup:**
   ```bash
   nohup ./mi_script.sh &
   ```

3. **Ver trabajos en segundo plano:**
   ```bash
   jobs
   ```

4. **Desasociar un trabajo en segundo plano:**
   ```bash
   disown %1
   ```

## Tips
- Utiliza `jobs` para ver los procesos que se están ejecutando en segundo plano.
- Puedes usar `fg` para traer un trabajo en segundo plano de vuelta al primer plano.
- Recuerda que si cierras la terminal, los procesos en segundo plano pueden finalizar a menos que uses `nohup`.