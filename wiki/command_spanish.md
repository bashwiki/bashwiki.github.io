# [리눅스] Bash command 사용법

## Overview
El comando `command` en Bash se utiliza para ejecutar un comando sin que se vean afectados los alias o funciones definidas por el usuario. Su propósito principal es permitir que los usuarios accedan a los comandos internos de Bash o a los comandos externos que podrían estar enmascarados por alias o funciones.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
command [opciones] comando [argumentos]
```

### Opciones Comunes
- `-v`: Muestra el comando que se va a ejecutar.
- `-p`: Busca el comando en el PATH predeterminado, ignorando alias y funciones.

## Examples
### Ejemplo 1: Ejecutar un comando sin alias
Supongamos que tienes un alias definido para `ls`, pero deseas ejecutar el comando original. Puedes hacerlo de la siguiente manera:

```bash
alias ls='ls --color=auto'
command ls
```
Este comando ejecutará el comando `ls` sin el alias, mostrando la salida estándar del comando.

### Ejemplo 2: Usar el comando `command` con opciones
Si deseas asegurarte de que estás ejecutando la versión del comando que se encuentra en el PATH predeterminado, puedes usar la opción `-p`:

```bash
command -p ls
```
Esto ejecutará el comando `ls` desde el PATH predeterminado, ignorando cualquier alias o función que puedas haber definido.

## Tips
- Utiliza `command` cuando necesites asegurarte de que estás ejecutando el comando original y no una versión modificada por un alias o función.
- Es útil en scripts donde la consistencia del comando es crucial y no quieres que los usuarios cambien los alias.
- Recuerda que `command` no es un comando que se utilice frecuentemente, pero es muy valioso en situaciones específicas donde la claridad y la precisión son necesarias.