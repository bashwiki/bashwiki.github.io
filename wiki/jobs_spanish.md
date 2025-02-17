# [Linux] Bash jobs uso: Gestionar trabajos en segundo plano

## Overview
El comando `jobs` en Bash se utiliza para mostrar la lista de trabajos en segundo plano que se están ejecutando en la sesión actual del terminal. Permite a los usuarios ver el estado de estos trabajos, facilitando la gestión de procesos que no están en primer plano.

## Usage
La sintaxis básica del comando es la siguiente:

```
jobs [opciones]
```

## Common Options
- `-l`: Muestra el ID del proceso (PID) junto con la información del trabajo.
- `-n`: Muestra solo los trabajos que han cambiado de estado desde la última vez que se ejecutó el comando.
- `-p`: Muestra solo los IDs de los procesos de los trabajos.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `jobs`:

1. **Listar trabajos en segundo plano:**
   ```bash
   jobs
   ```

2. **Listar trabajos en segundo plano con PID:**
   ```bash
   jobs -l
   ```

3. **Listar trabajos que han cambiado de estado:**
   ```bash
   jobs -n
   ```

4. **Obtener solo los IDs de los procesos:**
   ```bash
   jobs -p
   ```

## Tips
- Asegúrate de ejecutar `jobs` en la misma sesión de terminal donde iniciaste los trabajos en segundo plano para obtener resultados precisos.
- Puedes usar el comando `fg` seguido del número del trabajo para llevar un trabajo en segundo plano de vuelta al primer plano.
- Utiliza `bg` para reanudar un trabajo detenido en segundo plano, lo que te permite continuar su ejecución sin que ocupe el terminal.