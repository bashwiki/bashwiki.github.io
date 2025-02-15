# [리눅스] Bash pushd 사용법

## Overview
El comando `pushd` en Bash se utiliza para cambiar el directorio de trabajo actual y, al mismo tiempo, almacenar el directorio anterior en una pila. Esto permite a los usuarios navegar fácilmente entre varios directorios sin perder la ubicación anterior. Su principal propósito es facilitar la gestión de directorios en la línea de comandos, especialmente cuando se trabaja en múltiples ubicaciones.

## Usage
La sintaxis básica del comando `pushd` es la siguiente:

```bash
pushd [DIRECTORIO]
```

- **DIRECTORIO**: Especifica el directorio al que deseas cambiar. Si no se proporciona un directorio, `pushd` intercambiará el directorio actual con el último directorio en la pila.

### Opciones Comunes
- `+N`: Cambia al directorio en la posición N de la pila. Por ejemplo, `pushd +1` cambiará al segundo directorio en la pila.
- `-N`: Cambia al directorio en la posición N desde el final de la pila.

## Examples
### Ejemplo 1: Cambiar a un nuevo directorio
```bash
pushd /ruta/al/nuevo/directorio
```
Este comando cambiará al directorio especificado y almacenará el directorio actual en la pila.

### Ejemplo 2: Intercambiar directorios
```bash
pushd
```
Si ejecutas `pushd` sin argumentos, intercambiará el directorio actual con el último directorio que se encuentra en la pila.

## Tips
- Utiliza `popd` para volver al directorio anterior que has almacenado en la pila. Esto es útil para regresar rápidamente a la ubicación anterior.
- Puedes visualizar la pila de directorios utilizando el comando `dirs`, que mostrará todos los directorios almacenados en la pila.
- Recuerda que la pila de directorios funciona como una estructura LIFO (Last In, First Out), lo que significa que el último directorio que agregues será el primero en ser eliminado cuando uses `popd`.