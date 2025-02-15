# [리눅스] Bash umask 사용법

## Overview
El comando `umask` en Bash se utiliza para establecer la máscara de creación de archivos, que determina los permisos predeterminados para los nuevos archivos y directorios creados en el sistema. Su propósito principal es controlar el acceso a los archivos, limitando los permisos que se otorgan a los usuarios y grupos al momento de crear nuevos archivos.

## Usage
La sintaxis básica del comando `umask` es la siguiente:

```bash
umask [opciones] [máscara]
```

### Opciones Comunes
- **Sin argumentos**: Al ejecutar `umask` sin argumentos, muestra la máscara actual.
- **Máscara**: Se puede especificar una máscara en formato octal (por ejemplo, `022`, `077`), donde cada dígito representa los permisos que se deben denegar a los usuarios (propietario, grupo, otros).

## Examples
### Ejemplo 1: Ver la máscara actual
Para ver la máscara de creación de archivos actual, simplemente ejecuta:

```bash
umask
```

Esto devolverá un valor en formato octal, como `0022`, que indica los permisos que se deniegan.

### Ejemplo 2: Establecer una nueva máscara
Para establecer una nueva máscara que deniegue permisos de escritura a otros usuarios, puedes usar:

```bash
umask 0022
```

Con esta configuración, los nuevos archivos tendrán permisos `rw-r--r--` y los nuevos directorios tendrán permisos `rwxr-xr-x`.

## Tips
- Es recomendable establecer la máscara de creación de archivos en un valor que minimice el riesgo de acceso no autorizado, especialmente en entornos de producción.
- Puedes agregar el comando `umask` a tu archivo de inicio de sesión (como `.bashrc` o `.bash_profile`) para que se aplique automáticamente cada vez que inicies una nueva sesión de terminal.
- Recuerda que la máscara de umask se aplica solo a los archivos y directorios creados después de que se establece; no afecta a los archivos ya existentes.