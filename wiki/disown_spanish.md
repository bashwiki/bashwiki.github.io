# [Linux] Bash disown uso equivalente: Desasociar trabajos en segundo plano

## Overview
El comando `disown` se utiliza en Bash para desasociar un trabajo en segundo plano de la terminal actual. Esto significa que el trabajo continuará ejecutándose incluso si se cierra la terminal o se cierra la sesión. Es útil para mantener procesos en ejecución sin que dependan de la terminal.

## Usage
La sintaxis básica del comando `disown` es la siguiente:

```bash
disown [opciones] [argumentos]
```

## Common Options
- `-h`: Evita que el trabajo se reciba una señal SIGHUP (hangup) cuando la terminal se cierra.
- `-a`: Desasocia todos los trabajos en segundo plano.
- `-r`: Desasocia todos los trabajos en segundo plano que están en ejecución.

## Common Examples

### Desasociar un trabajo específico
Si tienes un trabajo en segundo plano con un ID de trabajo específico, puedes desasociarlo usando:

```bash
disown %1
```

### Desasociar todos los trabajos en segundo plano
Para desasociar todos los trabajos en segundo plano, simplemente usa:

```bash
disown -a
```

### Desasociar un trabajo y evitar SIGHUP
Si deseas desasociar un trabajo y asegurarte de que no reciba la señal SIGHUP, puedes usar:

```bash
disown -h %1
```

## Tips
- Asegúrate de que el trabajo que deseas desasociar esté en segundo plano; puedes usar `jobs` para verificar el estado de los trabajos.
- Utiliza `bg` para enviar un trabajo a segundo plano antes de usar `disown`.
- Recuerda que una vez que desasocias un trabajo, no podrás controlarlo desde la terminal, así que asegúrate de que esté funcionando correctamente antes de hacerlo.