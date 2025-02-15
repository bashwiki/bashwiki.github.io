# [리눅스] Bash exec 사용법

## Overview
El comando `exec` en Bash se utiliza para ejecutar un comando en el contexto del proceso actual, reemplazando el shell actual con el nuevo proceso. Esto significa que, una vez que se ejecuta el comando con `exec`, el shell original ya no está disponible, y el nuevo proceso toma su lugar. Es especialmente útil para scripts donde se desea finalizar el script y ejecutar un nuevo programa sin crear un nuevo proceso hijo.

## Usage
La sintaxis básica del comando `exec` es la siguiente:

```bash
exec [opciones] comando [argumentos]
```

### Opciones Comunes
- `-a nombre`: Permite especificar un nombre diferente para el proceso que se está ejecutando.
- `-l`: Inicia el nuevo comando como un shell de inicio de sesión.
- `-c`: Cambia el entorno del nuevo proceso, eliminando las variables de entorno heredadas.

## Examples
### Ejemplo 1: Reemplazar el shell actual
Si deseas reemplazar el shell actual con el comando `bash`, puedes usar:

```bash
exec bash
```

Esto cerrará el shell actual y abrirá una nueva sesión de Bash.

### Ejemplo 2: Ejecutar un script
Si tienes un script llamado `script.sh` y deseas ejecutarlo reemplazando el shell actual, puedes usar:

```bash
exec ./script.sh
```

Después de ejecutar este comando, el shell actual se cerrará y `script.sh` se ejecutará en su lugar.

## Tips
- Utiliza `exec` cuando necesites que un script finalice y no necesites volver al shell original.
- Ten cuidado al usar `exec`, ya que perderás el acceso al shell actual y a cualquier comando que desees ejecutar después.
- Puedes usar `exec` para redirigir la salida de un comando a un archivo, por ejemplo:

```bash
exec > salida.txt
```

Esto redirigirá toda la salida estándar del shell a `salida.txt` hasta que se cierre el shell o se cambie la redirección.