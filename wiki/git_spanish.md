# [Linux] Bash git uso: Control de versiones de proyectos

## Overview
El comando `git` es una herramienta de control de versiones que permite a los desarrolladores gestionar y rastrear los cambios en el código fuente a lo largo del tiempo. Facilita la colaboración entre múltiples desarrolladores y ayuda a mantener un historial claro de las modificaciones realizadas en un proyecto.

## Usage
La sintaxis básica del comando `git` es la siguiente:

```bash
git [opciones] [argumentos]
```

## Common Options
- `clone`: Clona un repositorio remoto en tu máquina local.
- `init`: Inicializa un nuevo repositorio de Git.
- `add`: Añade archivos al área de preparación (staging area).
- `commit`: Guarda los cambios en el repositorio.
- `push`: Envía los cambios locales a un repositorio remoto.
- `pull`: Recupera y fusiona cambios desde un repositorio remoto.
- `status`: Muestra el estado de los archivos en el repositorio.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `git`:

### Clonar un repositorio
```bash
git clone https://github.com/usuario/repo.git
```

### Inicializar un nuevo repositorio
```bash
git init mi-nuevo-repo
```

### Añadir archivos al área de preparación
```bash
git add archivo.txt
```

### Realizar un commit
```bash
git commit -m "Mensaje de commit"
```

### Enviar cambios a un repositorio remoto
```bash
git push origin main
```

### Recuperar cambios de un repositorio remoto
```bash
git pull origin main
```

### Ver el estado de los archivos
```bash
git status
```

## Tips
- Siempre escribe mensajes de commit claros y descriptivos para facilitar el seguimiento de los cambios.
- Usa ramas (`branches`) para trabajar en nuevas características sin afectar la rama principal.
- Realiza commits frecuentes para guardar tu progreso y facilitar la recuperación de versiones anteriores si es necesario.