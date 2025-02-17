# [Linux] Bash inotifywait Uso: Monitorear cambios en archivos y directorios

## Overview
El comando `inotifywait` es una herramienta de línea de comandos que permite a los usuarios monitorear cambios en archivos y directorios en tiempo real. Utiliza el sistema de notificación inotify del núcleo de Linux para detectar eventos como la creación, modificación o eliminación de archivos.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
inotifywait [opciones] [argumentos]
```

## Common Options
- `-m`: Modo de monitoreo continuo, permite que el comando siga ejecutándose y escuche eventos indefinidamente.
- `-r`: Monitorea directorios de forma recursiva.
- `-e`: Especifica el tipo de evento a monitorear (por ejemplo, `modify`, `create`, `delete`).
- `--format`: Permite personalizar la salida del comando.

## Common Examples
1. **Monitorear un directorio específico por cambios en archivos:**
   ```bash
   inotifywait -m /ruta/al/directorio
   ```

2. **Monitorear un directorio recursivamente por modificaciones:**
   ```bash
   inotifywait -mr -e modify /ruta/al/directorio
   ```

3. **Monitorear un archivo específico por eliminación:**
   ```bash
   inotifywait -e delete /ruta/al/archivo.txt
   ```

4. **Monitorear múltiples eventos en un directorio:**
   ```bash
   inotifywait -m -e create -e delete /ruta/al/directorio
   ```

5. **Personalizar la salida:**
   ```bash
   inotifywait -m --format '%w%f %e' /ruta/al/directorio
   ```

## Tips
- Utiliza el modo `-m` para mantener el comando en ejecución y recibir notificaciones continuas.
- Combina múltiples eventos con el flag `-e` para tener un monitoreo más completo.
- Considera redirigir la salida a un archivo para registrar los cambios en lugar de solo mostrarlos en la terminal.
- Asegúrate de tener los permisos adecuados para monitorear los archivos o directorios deseados.