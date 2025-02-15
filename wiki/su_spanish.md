# [리눅스] Bash su 사용법

## Overview
El comando `su` (substitute user) en Bash se utiliza para cambiar de usuario en un entorno de terminal. Su propósito principal es permitir que un usuario se convierta en otro usuario, lo que es especialmente útil para obtener privilegios de administrador o para ejecutar comandos como un usuario diferente. Por defecto, al ejecutar `su` sin argumentos, se cambia al usuario root, que tiene acceso completo al sistema.

## Usage
La sintaxis básica del comando `su` es la siguiente:

```bash
su [opciones] [usuario]
```

### Opciones Comunes:
- `-`: Inicia una sesión de inicio de sesión del usuario especificado, cargando su entorno.
- `-c`: Permite ejecutar un comando específico como el usuario indicado.
- `-l` o `--login`: Similar a `-`, inicia una sesión de inicio de sesión del usuario especificado.
- `-s`: Permite especificar un shell diferente para la sesión.

## Examples
### Ejemplo 1: Cambiar al usuario root
Para cambiar al usuario root y obtener acceso completo al sistema, simplemente se puede ejecutar:

```bash
su -
```

Después de ingresar la contraseña de root, se tendrá acceso al entorno del usuario root.

### Ejemplo 2: Ejecutar un comando como otro usuario
Si se desea ejecutar un comando específico como un usuario diferente, se puede usar la opción `-c`. Por ejemplo, para listar los archivos en el directorio home del usuario "usuario1":

```bash
su -c "ls -la" usuario1
```

Esto ejecutará el comando `ls -la` como el usuario "usuario1".

## Tips
- **Usar `sudo` cuando sea posible**: En muchos sistemas, es preferible usar `sudo` en lugar de `su`, ya que `sudo` permite ejecutar comandos con privilegios elevados sin necesidad de cambiar de usuario por completo.
- **Evitar el uso de `su` sin el guion**: Al usar `su` sin el guion, no se cargará el entorno del usuario, lo que puede llevar a confusiones si se necesitan variables de entorno específicas.
- **Seguridad**: Siempre asegúrate de tener cuidado al usar `su`, especialmente al cambiar a root, ya que puedes realizar cambios críticos en el sistema.