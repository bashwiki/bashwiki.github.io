# [Linux] Bash sleep Uso: Pausar la ejecución de un script

## Overview
El comando `sleep` en Bash se utiliza para pausar la ejecución de un script o un comando durante un período de tiempo específico. Es útil para controlar el flujo de ejecución en scripts, permitiendo retrasos entre comandos.

## Usage
La sintaxis básica del comando `sleep` es la siguiente:

```
sleep [opciones] [tiempo]
```

## Common Options
- `-h`, `--help`: Muestra la ayuda sobre el comando.
- `-V`, `--version`: Muestra la versión del comando.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `sleep`:

1. **Pausar por 5 segundos:**
   ```bash
   sleep 5
   ```

2. **Pausar por 2 minutos:**
   ```bash
   sleep 2m
   ```

3. **Pausar por 1.5 segundos:**
   ```bash
   sleep 1.5
   ```

4. **Usar sleep en un bucle:**
   ```bash
   for i in {1..5}; do
       echo "Contando: $i"
       sleep 1
   done
   ```

5. **Pausar entre comandos en un script:**
   ```bash
   echo "Iniciando proceso..."
   sleep 3
   echo "Proceso en ejecución..."
   sleep 2
   echo "Proceso completado."
   ```

## Tips
- Utiliza `sleep` para evitar que un script consuma demasiados recursos al hacer pausas entre tareas.
- Puedes combinar `sleep` con otros comandos en un script para crear temporizadores o retrasos.
- Recuerda que el tiempo puede ser especificado en segundos (s), minutos (m), horas (h) o días (d).