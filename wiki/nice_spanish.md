# [Linux] Bash nice Uso: Ajustar la prioridad de ejecución de procesos

## Overview
El comando `nice` en Bash se utiliza para ejecutar un programa con una prioridad de CPU ajustada. Permite a los usuarios aumentar o disminuir la prioridad de un proceso, lo que puede ser útil para gestionar la carga del sistema y asegurar que los procesos más importantes reciban más recursos de CPU.

## Usage
La sintaxis básica del comando `nice` es la siguiente:

```bash
nice [opciones] [comando] [argumentos]
```

## Common Options
- `-n, --adjustment`: Especifica el valor de ajuste de la prioridad. Puede ser un número entre -20 (máxima prioridad) y 19 (mínima prioridad).
- `--help`: Muestra la ayuda sobre el uso del comando.
- `--version`: Muestra la versión del comando `nice`.

## Common Examples
1. **Ejecutar un comando con prioridad por defecto:**
   ```bash
   nice my_script.sh
   ```

2. **Ejecutar un comando con una prioridad ajustada (por ejemplo, -5):**
   ```bash
   nice -n -5 my_script.sh
   ```

3. **Ejecutar un comando con prioridad mínima:**
   ```bash
   nice -n 19 my_script.sh
   ```

4. **Verificar la prioridad de un proceso en ejecución:**
   ```bash
   ps -o pid,nice,cmd
   ```

## Tips
- Utiliza `nice` para procesos que no son críticos y que pueden esperar más tiempo para ejecutarse.
- Si necesitas cambiar la prioridad de un proceso que ya está en ejecución, considera usar el comando `renice`.
- Recuerda que solo los usuarios con privilegios adecuados pueden establecer prioridades negativas (mayor prioridad).