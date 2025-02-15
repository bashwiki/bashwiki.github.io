# [리눅스] Bash sysctl 사용법

## Overview
El comando `sysctl` se utiliza en sistemas Unix y Linux para modificar y consultar parámetros del núcleo del sistema en tiempo real. Su propósito principal es permitir a los administradores del sistema ajustar configuraciones del núcleo sin necesidad de reiniciar el sistema. Esto es especialmente útil para optimizar el rendimiento y la seguridad del sistema.

## Usage
La sintaxis básica del comando `sysctl` es la siguiente:

```bash
sysctl [opciones] [nombre_de_parámetro]
```

### Opciones Comunes:
- `-a`: Muestra todos los parámetros del núcleo y sus valores actuales.
- `-n`: Muestra solo el valor del parámetro especificado, sin mostrar el nombre del parámetro.
- `-w`: Permite establecer un nuevo valor para un parámetro del núcleo. Este cambio es temporal y se perderá al reiniciar el sistema.
- `-p [archivo]`: Carga parámetros desde un archivo de configuración, típicamente `/etc/sysctl.conf`.

## Examples
### Ejemplo 1: Consultar todos los parámetros del núcleo
Para ver todos los parámetros del núcleo y sus valores actuales, puedes usar:

```bash
sysctl -a
```

### Ejemplo 2: Cambiar un parámetro del núcleo
Si deseas cambiar el valor del parámetro `vm.swappiness` para ajustar la forma en que el sistema utiliza la memoria, puedes hacerlo con:

```bash
sysctl -w vm.swappiness=10
```

Este comando establece el valor de `swappiness` a 10, lo que indica al sistema que prefiera utilizar la memoria RAM antes de recurrir al intercambio en disco.

## Tips
- **Persistencia de Cambios**: Para que los cambios realizados con `sysctl -w` sean persistentes después de un reinicio, es recomendable agregar los parámetros deseados en el archivo `/etc/sysctl.conf`.
- **Verificación de Cambios**: Después de modificar un parámetro, puedes verificar que el cambio se haya aplicado correctamente utilizando `sysctl -n nombre_de_parámetro`.
- **Precaución**: Al modificar parámetros del núcleo, es importante tener cuidado, ya que algunos cambios pueden afectar la estabilidad y el rendimiento del sistema. Siempre es recomendable realizar pruebas en un entorno controlado antes de aplicar cambios en producción.