# [리눅스] Bash git 사용법

## Overview
El comando `git` es un sistema de control de versiones distribuido que permite a los desarrolladores gestionar y realizar un seguimiento de los cambios en el código fuente a lo largo del tiempo. Su principal propósito es facilitar la colaboración en proyectos de software, permitiendo a múltiples desarrolladores trabajar en el mismo código de manera simultánea sin conflictos. Git permite realizar operaciones como commit, branch, merge y revert, entre otras, lo que lo convierte en una herramienta esencial en el desarrollo de software moderno.

## Usage
La sintaxis básica del comando `git` es la siguiente:

```
git [opciones] [subcomando] [argumentos]
```

Algunas de las opciones y subcomandos más comunes son:

- `git init`: Inicializa un nuevo repositorio Git.
- `git clone [url]`: Clona un repositorio remoto en tu máquina local.
- `git add [archivo]`: Agrega cambios en el archivo especificado al área de preparación.
- `git commit -m "mensaje"`: Registra los cambios en el repositorio con un mensaje descriptivo.
- `git status`: Muestra el estado actual del repositorio, incluyendo archivos modificados y no rastreados.
- `git push`: Envía los cambios locales a un repositorio remoto.
- `git pull`: Actualiza el repositorio local con los cambios del repositorio remoto.

## Examples
### Ejemplo 1: Inicializar un nuevo repositorio
Para crear un nuevo repositorio Git en un directorio existente, puedes usar el siguiente comando:

```bash
mkdir mi_proyecto
cd mi_proyecto
git init
```

Este comando crea un nuevo repositorio vacío en el directorio `mi_proyecto`.

### Ejemplo 2: Clonar un repositorio remoto
Si deseas clonar un repositorio existente desde GitHub, puedes usar el siguiente comando:

```bash
git clone https://github.com/usuario/repositorio.git
```

Este comando descarga todos los archivos y el historial de cambios del repositorio remoto a tu máquina local.

## Tips
- Siempre escribe mensajes de commit claros y descriptivos para facilitar la comprensión de los cambios realizados.
- Utiliza ramas (`git branch`) para trabajar en nuevas características o correcciones de errores sin afectar la rama principal.
- Realiza commits frecuentes para mantener un historial detallado de tu trabajo y facilitar la reversión de cambios si es necesario.
- Familiarízate con el uso de `git status` para mantenerte al tanto de los cambios en tu repositorio.
- Considera usar `.gitignore` para excluir archivos o directorios que no deseas rastrear en tu repositorio, como archivos temporales o de configuración local.