# [리눅스] Bash egrep 사용법

## Overview
El comando `egrep` es una variante de `grep` que permite buscar patrones en texto utilizando expresiones regulares extendidas. Su propósito principal es facilitar la búsqueda de cadenas complejas en archivos o en la salida de otros comandos, haciendo que sea más sencillo encontrar coincidencias que requieren patrones más sofisticados que los que permite `grep` por defecto.

## Usage
La sintaxis básica del comando `egrep` es la siguiente:

```
egrep [opciones] 'patrón' [archivo...]
```

### Opciones comunes:
- `-i`: Ignora la distinción entre mayúsculas y minúsculas.
- `-v`: Invertir la coincidencia, mostrando líneas que no coinciden con el patrón.
- `-c`: Contar el número de líneas que coinciden con el patrón.
- `-n`: Mostrar el número de línea junto con las líneas coincidentes.
- `-r` o `-R`: Buscar recursivamente en directorios.

## Examples
### Ejemplo 1: Búsqueda simple
Para buscar la palabra "error" en un archivo llamado `log.txt`, puedes usar el siguiente comando:

```bash
egrep 'error' log.txt
```

Este comando mostrará todas las líneas del archivo `log.txt` que contienen la palabra "error".

### Ejemplo 2: Búsqueda con opciones
Si deseas buscar la palabra "advertencia" sin distinguir entre mayúsculas y minúsculas y mostrar el número de línea, puedes utilizar:

```bash
egrep -i -n 'advertencia' log.txt
```

Este comando mostrará todas las líneas que contienen "advertencia" (en cualquier combinación de mayúsculas y minúsculas) junto con el número de línea correspondiente.

## Tips
- Utiliza comillas simples alrededor del patrón para evitar que el shell interprete caracteres especiales.
- Si trabajas con patrones complejos, considera usar paréntesis y operadores como `|` (o) para combinar múltiples patrones.
- Recuerda que `egrep` es equivalente a `grep -E`, por lo que puedes usar cualquiera de los dos según tus preferencias.
- Para mejorar la legibilidad de la salida, considera redirigirla a un archivo o utilizar tuberías para procesar los resultados con otros comandos.