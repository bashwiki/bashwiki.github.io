# [리눅스] Bash basename 사용법

## Overview
El comando `basename` en Bash se utiliza para extraer el nombre de un archivo o directorio de una ruta completa. Su propósito principal es simplificar el manejo de rutas, permitiendo a los desarrolladores y administradores de sistemas obtener solo el nombre del archivo o directorio sin la información de la ruta que lo precede.

## Usage
La sintaxis básica del comando `basename` es la siguiente:

```bash
basename [ruta] [sufijo]
```

- **ruta**: Es la ruta completa del archivo o directorio del cual se desea extraer el nombre.
- **sufijo** (opcional): Especifica un sufijo que se eliminará del nombre del archivo resultante.

### Opciones Comunes
- No hay opciones adicionales en el comando `basename`, pero se puede usar el sufijo para eliminar extensiones de archivos.

## Examples
### Ejemplo 1: Obtener el nombre de un archivo
Supongamos que tenemos un archivo ubicado en `/home/usuario/documentos/informe.txt`. Para obtener solo el nombre del archivo, se puede usar el siguiente comando:

```bash
basename /home/usuario/documentos/informe.txt
```

**Salida:**
```
informe.txt
```

### Ejemplo 2: Eliminar un sufijo
Si deseamos obtener solo el nombre del archivo sin la extensión, podemos usar el sufijo:

```bash
basename /home/usuario/documentos/informe.txt .txt
```

**Salida:**
```
informe
```

## Tips
- Utiliza `basename` en scripts para simplificar el manejo de archivos y rutas, especialmente cuando necesitas trabajar solo con los nombres de los archivos.
- Recuerda que `basename` no modifica los archivos ni las rutas, simplemente devuelve el nombre solicitado.
- Puedes combinar `basename` con otros comandos como `find` o `ls` para procesar listas de archivos de manera más eficiente.