# [리눅스] Bash disown 사용법

## Overview
El comando `disown` en Bash se utiliza para eliminar trabajos de la lista de trabajos del shell, lo que significa que estos trabajos ya no estarán asociados con la sesión actual del terminal. Su propósito principal es permitir que los procesos en segundo plano continúen ejecutándose incluso después de que el usuario cierre la terminal o se desconecte de la sesión. Esto es especialmente útil para tareas largas que no requieren interacción del usuario.

## Usage
La sintaxis básica del comando `disown` es la siguiente:

```bash
disown [opciones] [jobspec]
```

### Opciones comunes:
- `-h`: Marca el trabajo especificado como "no notificado", lo que significa que no se enviará una señal de SIGHUP (hangup) cuando la terminal se cierre.
- `-a`: Aplica el comando a todos los trabajos en segundo plano.
- `-r`: Aplica el comando solo a los trabajos que están en ejecución.

Si no se especifica ningún `jobspec`, `disown` eliminará el trabajo más reciente de la lista de trabajos.

## Examples
### Ejemplo 1: Desasociar el trabajo más reciente
Supongamos que has iniciado un proceso en segundo plano, como un script que tarda mucho tiempo en ejecutarse:

```bash
./mi_script_largo.sh &
```

Para desasociar este trabajo y permitir que continúe ejecutándose incluso si cierras la terminal, puedes usar:

```bash
disown
```

### Ejemplo 2: Desasociar un trabajo específico
Si tienes varios trabajos en segundo plano y deseas desasociar uno específico, primero puedes listar los trabajos con el comando `jobs`:

```bash
jobs
```

Esto mostrará algo como:

```
[1]+  12345 Running                 ./mi_script_largo.sh &
[2]-  12346 Running                 ./otro_script.sh &
```

Para desasociar el primer trabajo, usarías:

```bash
disown %1
```

## Tips
- Recuerda que una vez que un trabajo ha sido desasociado, no podrás volver a conectarte a él desde la terminal. Asegúrate de que realmente deseas que el proceso continúe sin supervisión.
- Utiliza `disown -h %1` si deseas que un trabajo siga ejecutándose pero no quieres que se le envíe una señal de SIGHUP al cerrar la terminal.
- Es una buena práctica verificar el estado de los trabajos en segundo plano con `jobs` antes de usar `disown`, para asegurarte de que estás desasociando el trabajo correcto.