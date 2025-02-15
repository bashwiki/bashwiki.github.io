# [리눅스] Bash popd 사용법

## Overview
El comando `popd` se utiliza en Bash para eliminar el directorio superior de la pila de directorios y cambiar el directorio de trabajo actual a ese directorio. Este comando es especialmente útil para navegar de manera eficiente entre múltiples directorios sin tener que escribir la ruta completa cada vez. `popd` complementa al comando `pushd`, que agrega un directorio a la pila.

## Usage
La sintaxis básica del comando `popd` es la siguiente:

```bash
popd [options]
```

### Opciones Comunes
- `-n`: No cambia el directorio actual, solo elimina el directorio superior de la pila.
- `+n`: Elimina el directorio en la posición `n` de la pila y cambia al directorio correspondiente. La posición se cuenta desde 0, siendo el directorio más reciente el 0.

## Examples
### Ejemplo 1: Uso básico de `popd`
Primero, agregamos algunos directorios a la pila con `pushd` y luego usamos `popd` para volver al directorio anterior.

```bash
pushd /ruta/al/directorio1
pushd /ruta/al/directorio2
# Ahora estamos en /ruta/al/directorio2
popd
# Ahora estamos de vuelta en /ruta/al/directorio1
```

### Ejemplo 2: Uso de la opción `+n`
Si tenemos varios directorios en la pila, podemos especificar cuál queremos eliminar y cambiar.

```bash
pushd /ruta/al/directorio1
pushd /ruta/al/directorio2
pushd /ruta/al/directorio3
# La pila ahora contiene: /ruta/al/directorio3, /ruta/al/directorio2, /ruta/al/directorio1
popd +1
# Ahora estamos en /ruta/al/directorio3, y /ruta/al/directorio2 ha sido eliminado de la pila
```

## Tips
- Utiliza `dirs` para ver el contenido actual de la pila de directorios antes de usar `popd`. Esto te ayudará a saber qué directorios están disponibles para navegar.
- Combina `pushd` y `popd` para crear scripts de navegación más eficientes, permitiéndote cambiar rápidamente entre directorios sin perder el rastro de tu ubicación.
- Recuerda que `popd` solo afecta la pila de directorios si has utilizado `pushd` previamente; de lo contrario, no tendrá efecto.