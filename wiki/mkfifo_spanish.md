# [Linux] Bash mkfifo Uso: Crear tuberías con nombre

El comando `mkfifo` se utiliza para crear tuberías con nombre en sistemas Unix y Linux, permitiendo la comunicación entre procesos.

## Overview
El comando `mkfifo` crea un archivo especial llamado "tubería con nombre" (FIFO, por sus siglas en inglés). Este tipo de archivo permite que los procesos se comuniquen entre sí mediante la escritura y lectura de datos, facilitando la transferencia de información en tiempo real.

## Usage
La sintaxis básica del comando `mkfifo` es la siguiente:

```bash
mkfifo [opciones] [nombre_del_fifo]
```

## Common Options
- `-m, --mode=MODE`: Establece los permisos del archivo FIFO. `MODE` puede ser un valor octal que define los permisos.
- `--help`: Muestra la ayuda sobre el uso del comando.
- `--version`: Muestra la versión del comando.

## Common Examples

### Crear un FIFO simple
Para crear un FIFO llamado `mi_fifo`, puedes usar el siguiente comando:

```bash
mkfifo mi_fifo
```

### Crear un FIFO con permisos específicos
Si deseas crear un FIFO con permisos específicos, por ejemplo, solo lectura y escritura para el propietario, puedes hacer lo siguiente:

```bash
mkfifo -m 600 mi_fifo
```

### Usar un FIFO en un comando
Puedes usar un FIFO para comunicarte entre dos procesos. Por ejemplo, puedes crear un FIFO y luego usarlo para enviar datos entre un proceso de escritura y un proceso de lectura:

1. En una terminal, crea el FIFO:
   ```bash
   mkfifo mi_fifo
   ```

2. En una terminal, escribe datos en el FIFO:
   ```bash
   echo "Hola desde el FIFO" > mi_fifo
   ```

3. En otra terminal, lee los datos del FIFO:
   ```bash
   cat mi_fifo
   ```

### Usar un FIFO con comandos en segundo plano
Puedes ejecutar un comando en segundo plano que escriba en el FIFO mientras lees en otra terminal:

```bash
# En una terminal
echo "Mensaje en segundo plano" > mi_fifo &

# En otra terminal
cat mi_fifo
```

## Tips
- Asegúrate de que el FIFO esté creado antes de intentar leer o escribir en él.
- Recuerda que los procesos que intentan leer de un FIFO se bloquearán hasta que haya datos disponibles.
- Utiliza permisos adecuados al crear el FIFO para evitar accesos no deseados.