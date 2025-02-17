# [Linux] Bash cron uso: Programa tareas automáticamente

## Overview
El comando `cron` se utiliza en sistemas Unix y Linux para programar la ejecución de tareas de manera automática en intervalos regulares. Permite a los usuarios ejecutar scripts o comandos en momentos específicos, lo que es útil para tareas de mantenimiento, copias de seguridad y otras operaciones programadas.

## Usage
La sintaxis básica del comando `cron` se define en un archivo llamado `crontab`, donde se especifican las tareas programadas. La estructura general es la siguiente:

```bash
* * * * * comando_a_ejecutar
```

Los cinco asteriscos representan, en orden, los minutos, horas, días del mes, meses y días de la semana en que se ejecutará el comando.

## Common Options
- `-e`: Editar el archivo crontab del usuario actual.
- `-l`: Listar las tareas programadas en el crontab del usuario actual.
- `-r`: Eliminar el crontab del usuario actual.

## Common Examples
1. **Ejecutar un script cada día a las 2 AM:**
   ```bash
   0 2 * * * /ruta/al/script.sh
   ```

2. **Ejecutar un comando cada hora:**
   ```bash
   0 * * * * /usr/bin/mi_comando
   ```

3. **Ejecutar un script todos los lunes a las 5 PM:**
   ```bash
   0 17 * * 1 /ruta/al/script.sh
   ```

4. **Ejecutar un comando cada 15 minutos:**
   ```bash
   */15 * * * * /usr/bin/mi_comando
   ```

## Tips
- Asegúrate de que los scripts tengan permisos de ejecución.
- Usa rutas absolutas para los comandos y scripts para evitar problemas de localización.
- Revisa los registros de cron para verificar que las tareas se ejecuten correctamente, generalmente en `/var/log/syslog` o `/var/log/cron.log`.