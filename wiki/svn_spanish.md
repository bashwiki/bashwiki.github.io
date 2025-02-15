# [리눅스] Bash svn 사용법

## Overview
El comando `svn` es una herramienta de control de versiones que forma parte del sistema Apache Subversion. Su propósito principal es gestionar y mantener versiones de archivos y directorios, permitiendo a los desarrolladores colaborar en proyectos de software de manera eficiente. Con `svn`, los usuarios pueden realizar operaciones como la creación de repositorios, la actualización de archivos, la adición de nuevos elementos y la resolución de conflictos.

## Usage
La sintaxis básica del comando `svn` es la siguiente:

```
svn [opciones] [subcomando] [ruta]
```

### Opciones comunes:
- `checkout`: Clona un repositorio en el sistema local.
- `update`: Sincroniza los archivos locales con el repositorio.
- `add`: Añade nuevos archivos o directorios al control de versiones.
- `commit`: Envía los cambios locales al repositorio.
- `status`: Muestra el estado de los archivos en el directorio de trabajo.
- `log`: Muestra el historial de cambios del repositorio.

## Examples
### Ejemplo 1: Clonar un repositorio
Para clonar un repositorio remoto a tu máquina local, puedes usar el siguiente comando:

```bash
svn checkout https://ejemplo.com/repositorio/trunk
```

Este comando descargará el contenido del directorio `trunk` del repositorio especificado.

### Ejemplo 2: Actualizar archivos locales
Para actualizar tu copia local con los últimos cambios del repositorio, utiliza:

```bash
svn update
```

Este comando descargará y aplicará cualquier cambio que se haya realizado en el repositorio desde la última vez que actualizaste.

## Tips
- Siempre realiza un `svn update` antes de comenzar a trabajar en tus archivos para asegurarte de que estás trabajando con la versión más reciente.
- Utiliza `svn status` frecuentemente para verificar el estado de tus archivos y asegurarte de que no hay cambios no guardados.
- Al hacer un `commit`, incluye un mensaje descriptivo utilizando la opción `-m`, por ejemplo:

```bash
svn commit -m "Añadido nuevo módulo de autenticación"
```

Esto ayudará a mantener un historial claro y comprensible de los cambios realizados en el proyecto.