# [Linux] Bash exit uso: Terminar un script o sesión de shell

## Overview
El comando `exit` se utiliza en Bash para finalizar un script o cerrar una sesión de shell. Al ejecutar este comando, se puede especificar un código de salida que indica el estado de la ejecución del script, donde un código de salida de 0 generalmente significa que todo ha funcionado correctamente.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
exit [número]
```

Donde `[número]` es un código de salida opcional.

## Common Options
- **número**: Un valor numérico que representa el código de salida. Por convención, un código de salida de 0 indica éxito, mientras que cualquier otro número indica un error.

## Common Examples

1. **Salir de un script con éxito**:
   ```bash
   #!/bin/bash
   echo "Script ejecutado correctamente."
   exit 0
   ```

2. **Salir de un script con un error**:
   ```bash
   #!/bin/bash
   echo "Se produjo un error."
   exit 1
   ```

3. **Cerrar una sesión de shell**:
   ```bash
   exit
   ```

4. **Salir de un script y pasar un código de error**:
   ```bash
   #!/bin/bash
   if [ ! -f "archivo.txt" ]; then
       echo "El archivo no existe."
       exit 2
   fi
   ```

## Tips
- Siempre es una buena práctica especificar un código de salida al usar `exit`, ya que esto ayuda a identificar el resultado de la ejecución del script.
- Utiliza `exit 0` para indicar que el script se completó sin errores, lo que es útil para la depuración y el manejo de errores en scripts más complejos.
- Recuerda que si no se especifica un código de salida, Bash utilizará el código de salida del último comando ejecutado.