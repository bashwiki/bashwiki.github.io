# [Linux] Bash ss uso equivalente: [visualizar conexiones de red]

## Overview
El comando `ss` se utiliza en sistemas Linux para investigar y mostrar información sobre las conexiones de red. Es una herramienta poderosa que permite a los administradores de sistemas y a los usuarios obtener detalles sobre los sockets de red, incluyendo conexiones activas, puertos en uso y estadísticas de red.

## Usage
La sintaxis básica del comando `ss` es la siguiente:

```bash
ss [opciones] [argumentos]
```

## Common Options
- `-t`: Muestra solo conexiones TCP.
- `-u`: Muestra solo conexiones UDP.
- `-l`: Muestra solo sockets que están escuchando.
- `-p`: Muestra el proceso que está utilizando el socket.
- `-n`: Muestra direcciones y puertos en formato numérico, sin resolver nombres.

## Common Examples
- Para mostrar todas las conexiones TCP activas:

```bash
ss -t
```

- Para listar todos los sockets UDP:

```bash
ss -u
```

- Para ver todos los sockets que están escuchando:

```bash
ss -l
```

- Para mostrar conexiones con información del proceso:

```bash
ss -p
```

- Para ver todas las conexiones y puertos en formato numérico:

```bash
ss -n
```

## Tips
- Utiliza `ss -tuln` para obtener una vista completa de todos los sockets TCP y UDP que están escuchando, junto con sus números de puerto.
- Combina opciones para obtener información más específica, como `ss -tunlp` para ver conexiones TCP y UDP activas junto con los procesos que las utilizan.
- Recuerda que necesitarás permisos de superusuario para ver información sobre todos los procesos; usa `sudo` si es necesario.