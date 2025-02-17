# [Linux] Bash dmesg Uso: Visualizar mensajes del núcleo

## Overview
El comando `dmesg` se utiliza para mostrar los mensajes del núcleo de Linux. Estos mensajes son generados por el sistema operativo y pueden incluir información sobre el hardware, controladores y eventos del sistema. Es una herramienta útil para diagnosticar problemas y entender el comportamiento del sistema.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
dmesg [opciones] [argumentos]
```

## Common Options
- `-C`: Borra el buffer de mensajes del núcleo.
- `-c`: Borra el buffer después de mostrar los mensajes.
- `-n nivel`: Establece el nivel de prioridad de los mensajes que se mostrarán.
- `-f fac`: Filtra los mensajes por la faceta especificada.
- `-T`: Convierte las marcas de tiempo a un formato legible.

## Common Examples
- Para mostrar todos los mensajes del núcleo:

```bash
dmesg
```

- Para mostrar los mensajes más recientes:

```bash
dmesg | tail
```

- Para borrar el buffer después de mostrar los mensajes:

```bash
dmesg -c
```

- Para mostrar mensajes con un nivel de prioridad específico (por ejemplo, nivel 3):

```bash
dmesg -n 3
```

- Para mostrar mensajes con marcas de tiempo legibles:

```bash
dmesg -T
```

## Tips
- Utiliza `dmesg | less` para navegar por los mensajes de manera más cómoda.
- Revisa los mensajes de `dmesg` después de un arranque para identificar problemas de hardware.
- Filtra los mensajes relevantes usando `grep`, por ejemplo: `dmesg | grep error` para buscar errores específicos.