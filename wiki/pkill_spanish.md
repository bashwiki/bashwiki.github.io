# [Linux] Bash pkill Uso: Termina procesos por nombre

## Overview
El comando `pkill` se utiliza en sistemas Unix y Linux para terminar procesos basados en su nombre o en otros atributos. Es una herramienta poderosa que permite a los usuarios gestionar los procesos en ejecución de manera eficiente.

## Usage
La sintaxis básica del comando `pkill` es la siguiente:

```bash
pkill [opciones] [argumentos]
```

## Common Options
- `-f`: Permite buscar en la línea de comandos completa del proceso.
- `-n`: Termina solo el proceso más reciente que coincida con el nombre.
- `-o`: Termina solo el proceso más antiguo que coincida con el nombre.
- `-signal`: Especifica la señal que se enviará al proceso (por defecto es SIGTERM).

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `pkill`:

1. **Terminar un proceso por nombre**:
   ```bash
   pkill firefox
   ```
   Este comando terminará todos los procesos de Firefox en ejecución.

2. **Terminar un proceso usando una señal específica**:
   ```bash
   pkill -9 firefox
   ```
   Aquí se envía la señal SIGKILL (9) a todos los procesos de Firefox, forzando su terminación.

3. **Buscar y terminar procesos que coincidan con una expresión regular**:
   ```bash
   pkill -f "python.*script.py"
   ```
   Este comando terminará cualquier proceso que esté ejecutando un script de Python específico.

4. **Terminar solo el proceso más reciente**:
   ```bash
   pkill -n firefox
   ```
   Este comando solo terminará la instancia más reciente de Firefox.

## Tips
- Siempre verifica los procesos en ejecución antes de usar `pkill` para evitar cerrar accidentalmente procesos importantes. Puedes usar `ps aux` para listar los procesos.
- Utiliza la opción `-f` con precaución, ya que puede coincidir con más procesos de los que esperas.
- Considera usar `pgrep` para buscar procesos antes de decidir terminarlos, lo que te permite ver qué procesos se verán afectados.