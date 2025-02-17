# [Linux] Bash w: Muestra quién está conectado y qué están haciendo

## Overview
El comando `w` en Bash se utiliza para mostrar información sobre los usuarios que están actualmente conectados al sistema y las actividades que están realizando. Proporciona detalles como el nombre de usuario, la terminal, el tiempo de actividad y el comando que se está ejecutando.

## Usage
La sintaxis básica del comando `w` es la siguiente:

```bash
w [opciones] [argumentos]
```

## Common Options
- `-h`: Omite la línea de encabezado.
- `-s`: Muestra una salida más corta, omitiendo información adicional.
- `-f`: Muestra el nombre completo del host.
- `-u`: Muestra el tiempo de inactividad de los usuarios.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `w`:

1. **Mostrar todos los usuarios conectados:**
   ```bash
   w
   ```

2. **Mostrar información sin la línea de encabezado:**
   ```bash
   w -h
   ```

3. **Mostrar una salida más corta:**
   ```bash
   w -s
   ```

4. **Incluir el nombre completo del host:**
   ```bash
   w -f
   ```

5. **Mostrar usuarios con tiempo de inactividad:**
   ```bash
   w -u
   ```

## Tips
- Utiliza `w` para monitorear la actividad de los usuarios en sistemas compartidos, especialmente en servidores.
- Combina `w` con otros comandos como `grep` para filtrar usuarios específicos.
- Revisa la información de tiempo de inactividad para identificar sesiones que podrían cerrarse.