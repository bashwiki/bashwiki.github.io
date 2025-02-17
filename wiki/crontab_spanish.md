# [Linux] Bash crontab Uso: Programa tareas automáticamente

## Overview
El comando `crontab` se utiliza para programar tareas que se ejecutan automáticamente en intervalos regulares en sistemas Unix y Linux. Permite a los usuarios definir comandos o scripts que se ejecutan en momentos específicos, facilitando la automatización de tareas repetitivas.

## Usage
La sintaxis básica del comando `crontab` es la siguiente:

```bash
crontab [opciones] [archivo]
```

## Common Options
- `-e`: Editar el archivo crontab del usuario actual.
- `-l`: Listar las tareas programadas en el crontab del usuario actual.
- `-r`: Eliminar el archivo crontab del usuario actual.
- `-i`: Preguntar antes de eliminar el crontab.

## Common Examples
Aquí hay algunos ejemplos prácticos de cómo usar `crontab`:

1. **Editar el crontab**:
   Para editar las tareas programadas, puedes usar:
   ```bash
   crontab -e
   ```

2. **Listar tareas programadas**:
   Para ver las tareas que ya tienes programadas:
   ```bash
   crontab -l
   ```

3. **Eliminar el crontab**:
   Para eliminar todas las tareas programadas (se te pedirá confirmación):
   ```bash
   crontab -r -i
   ```

4. **Programar un script para que se ejecute cada día a las 2 AM**:
   Al editar el crontab, puedes agregar la siguiente línea:
   ```bash
   0 2 * * * /ruta/al/script.sh
   ```

5. **Ejecutar un comando cada hora**:
   Para ejecutar un comando cada hora, añade:
   ```bash
   0 * * * * comando_a_ejecutar
   ```

## Tips
- Siempre verifica la sintaxis de las entradas en el crontab para evitar errores.
- Utiliza rutas absolutas para los scripts o comandos que deseas ejecutar.
- Revisa los logs del sistema para asegurarte de que las tareas se están ejecutando como se espera.