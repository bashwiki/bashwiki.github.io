# [Linux] Bash chattr uso: Modificar atributos de archivos en el sistema de archivos

## Overview
El comando `chattr` se utiliza en sistemas Linux para cambiar los atributos de los archivos en el sistema de archivos. Esto permite a los usuarios proteger archivos de modificaciones accidentales o no autorizadas, así como establecer ciertas propiedades que afectan su comportamiento.

## Usage
La sintaxis básica del comando `chattr` es la siguiente:

```bash
chattr [opciones] [atributos] [archivo]
```

## Common Options
- `+a`: Permite que el archivo sea añadido, pero no modificado.
- `+i`: Hace que el archivo sea inmutable, impidiendo cualquier cambio.
- `-i`: Elimina el atributo inmutable de un archivo.
- `+e`: Permite que el archivo sea borrado incluso si está en uso.
- `-e`: Elimina el atributo que permite borrar el archivo en uso.

## Common Examples
- Para hacer un archivo inmutable:
  ```bash
  chattr +i archivo.txt
  ```

- Para permitir que se añadan datos a un archivo, pero no se modifique:
  ```bash
  chattr +a archivo.log
  ```

- Para quitar el atributo inmutable de un archivo:
  ```bash
  chattr -i archivo.txt
  ```

- Para ver los atributos de un archivo:
  ```bash
  lsattr archivo.txt
  ```

## Tips
- Utiliza `lsattr` para verificar los atributos de los archivos antes de aplicar cambios con `chattr`.
- Ten cuidado al usar el atributo inmutable (`+i`), ya que puede dificultar la eliminación o modificación del archivo.
- Es recomendable usar `chattr` en archivos críticos del sistema o en archivos de configuración para protegerlos de cambios accidentales.