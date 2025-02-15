# [리눅스] Bash who 사용법

## Overview
El comando `who` en Bash se utiliza para mostrar información sobre los usuarios que están actualmente conectados al sistema. Proporciona detalles como el nombre de usuario, la terminal que están utilizando, la fecha y hora en que se conectaron, y en algunos casos, la dirección IP desde la que se conectaron. Este comando es especialmente útil para administradores de sistemas y desarrolladores que necesitan monitorear la actividad de los usuarios en un entorno multiusuario.

## Usage
La sintaxis básica del comando `who` es la siguiente:

```bash
who [opciones]
```

### Opciones comunes:
- `-a`: Muestra toda la información disponible, incluyendo usuarios conectados, tiempos de inactividad y más.
- `-b`: Muestra la última vez que el sistema fue reiniciado.
- `-q`: Muestra solo los nombres de los usuarios conectados y el conteo de usuarios.
- `--help`: Muestra la ayuda del comando.

## Examples
### Ejemplo 1: Mostrar usuarios conectados
Para ver una lista de los usuarios actualmente conectados al sistema, simplemente ejecuta:

```bash
who
```

La salida mostrará una lista con el nombre de usuario, la terminal, la fecha y la hora de conexión.

### Ejemplo 2: Mostrar información detallada
Para obtener información más detallada sobre los usuarios conectados, puedes usar la opción `-a`:

```bash
who -a
```

Esto mostrará información adicional, como los tiempos de inactividad y otros detalles relevantes.

## Tips
- Utiliza el comando `who` junto con otros comandos como `grep` para filtrar la información. Por ejemplo, si deseas ver si un usuario específico está conectado, puedes hacer:

```bash
who | grep nombre_de_usuario
```

- Recuerda que el comando `who` solo muestra usuarios que están actualmente conectados. Si necesitas información sobre todos los usuarios, considera usar el comando `w` o `users` para obtener diferentes perspectivas sobre la actividad del sistema. 

Utilizar `who` es una forma efectiva de monitorear la actividad de los usuarios y gestionar un entorno de trabajo colaborativo.