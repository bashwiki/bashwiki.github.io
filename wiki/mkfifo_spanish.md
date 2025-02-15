# [리눅스] Bash mkfifo 사용법

## Overview
El comando `mkfifo` se utiliza en sistemas Unix y Linux para crear un "FIFO" (First In, First Out), que es un tipo especial de archivo que actúa como un canal de comunicación entre procesos. Los FIFOs permiten que un proceso escriba datos en el archivo mientras que otro proceso puede leer esos datos en el mismo orden en que fueron escritos. Esto es útil para la sincronización y la comunicación entre procesos en aplicaciones concurrentes.

## Usage
La sintaxis básica del comando `mkfifo` es la siguiente:

```bash
mkfifo [opciones] nombre_fifo
```

### Opciones comunes:
- `-m, --mode=MODE`: Establece los permisos del archivo FIFO. El modo se especifica en formato octal (por ejemplo, `0666`).
- `-Z, --context=CONTEXT`: Establece el contexto de seguridad para el archivo FIFO, útil en sistemas que utilizan SELinux.

## Examples
### Ejemplo 1: Crear un FIFO simple
Para crear un FIFO llamado `mi_fifo`, puedes usar el siguiente comando:

```bash
mkfifo mi_fifo
```

Este comando creará un archivo FIFO en el directorio actual. Puedes verificar su creación usando `ls -l`:

```bash
ls -l mi_fifo
```

### Ejemplo 2: Usar un FIFO para comunicación entre procesos
Supongamos que deseas enviar datos desde un proceso a otro. Primero, crea el FIFO:

```bash
mkfifo mi_fifo
```

Luego, en una terminal, puedes usar el siguiente comando para escribir en el FIFO:

```bash
echo "Hola, mundo" > mi_fifo
```

Y en otra terminal, puedes leer el contenido del FIFO:

```bash
cat mi_fifo
```

Esto mostrará "Hola, mundo" en la segunda terminal.

## Tips
- Asegúrate de que el FIFO se elimine cuando ya no lo necesites, utilizando `rm mi_fifo` para evitar confusiones en el futuro.
- Recuerda que el FIFO se bloquea en la escritura hasta que hay un lector disponible. Por lo tanto, es importante tener un proceso de lectura activo antes de escribir en el FIFO.
- Puedes utilizar permisos específicos al crear el FIFO con la opción `-m` para controlar quién puede leer o escribir en el archivo.