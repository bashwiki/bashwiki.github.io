# [Linux] Bash ulimit uso: Limitar recursos del sistema para procesos

## Overview
El comando `ulimit` se utiliza en sistemas Unix y Linux para establecer límites en los recursos que pueden ser utilizados por los procesos en ejecución. Esto es útil para prevenir que un solo proceso consuma todos los recursos del sistema, lo que podría afectar a otros procesos.

## Usage
La sintaxis básica del comando `ulimit` es la siguiente:

```bash
ulimit [opciones] [argumentos]
```

## Common Options
- `-a`: Muestra todos los límites actuales de recursos.
- `-c`: Establece el tamaño máximo de los archivos de volcado de núcleo.
- `-d`: Establece el tamaño máximo de la memoria de datos.
- `-f`: Establece el tamaño máximo de los archivos que se pueden crear.
- `-l`: Establece el tamaño máximo de la memoria bloqueada.
- `-n`: Establece el número máximo de descriptores de archivo que un proceso puede tener.
- `-s`: Establece el tamaño máximo de la pila.
- `-t`: Establece el tiempo máximo de CPU en segundos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `ulimit`:

1. **Mostrar todos los límites actuales:**
   ```bash
   ulimit -a
   ```

2. **Establecer un límite de tamaño de archivo a 100 MB:**
   ```bash
   ulimit -f 102400
   ```

3. **Establecer un límite de descriptores de archivo a 2048:**
   ```bash
   ulimit -n 2048
   ```

4. **Establecer un límite de tiempo de CPU a 60 segundos:**
   ```bash
   ulimit -t 60
   ```

5. **Establecer el tamaño máximo de la pila a 8 MB:**
   ```bash
   ulimit -s 8192
   ```

## Tips
- Es recomendable verificar los límites actuales antes de realizar cambios, utilizando `ulimit -a`.
- Cambios realizados con `ulimit` son temporales y solo afectan la sesión actual. Para hacer cambios permanentes, edita el archivo de configuración correspondiente (como `/etc/security/limits.conf`).
- Ten cuidado al aumentar los límites, ya que puede afectar la estabilidad del sistema si un proceso consume demasiados recursos.