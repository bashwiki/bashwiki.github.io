# [Linux] Bash read uso: Leer entrada del usuario

El comando `read` en Bash se utiliza para leer la entrada del usuario desde la línea de comandos y almacenar esa entrada en variables.

## Overview
El comando `read` permite capturar la entrada del usuario y asignarla a variables, lo que es útil en scripts para interactuar con el usuario y obtener información necesaria para la ejecución del script.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
read [opciones] [nombre_variable]
```

## Common Options
- `-p`: Muestra un mensaje de aviso antes de leer la entrada.
- `-s`: Silencia la entrada, útil para contraseñas.
- `-a`: Lee la entrada en un array.
- `-d`: Especifica un delimitador diferente para finalizar la entrada.

## Common Examples

### Ejemplo 1: Leer una sola línea
```bash
read nombre
echo "Hola, $nombre"
```
Este script pide al usuario que ingrese su nombre y luego lo saluda.

### Ejemplo 2: Usar un mensaje de aviso
```bash
read -p "Introduce tu edad: " edad
echo "Tienes $edad años."
```
Aquí, se muestra un mensaje antes de que el usuario ingrese su edad.

### Ejemplo 3: Leer una contraseña
```bash
read -s -p "Introduce tu contraseña: " contraseña
echo "Contraseña guardada."
```
Este ejemplo oculta la entrada del usuario mientras escribe la contraseña.

### Ejemplo 4: Leer múltiples valores
```bash
read -p "Introduce tu nombre y apellido: " nombre apellido
echo "Nombre: $nombre, Apellido: $apellido"
```
En este caso, el usuario puede ingresar su nombre y apellido en una sola línea.

### Ejemplo 5: Leer en un array
```bash
read -a frutas -p "Introduce varias frutas separadas por espacio: "
echo "Las frutas son: ${frutas[@]}"
```
Este script almacena múltiples entradas en un array y las muestra.

## Tips
- Utiliza el flag `-p` para hacer que tus scripts sean más amigables al usuario.
- Si necesitas leer una contraseña, no olvides usar `-s` para ocultar la entrada.
- Almacenar entradas en un array con `-a` puede ser útil para manejar múltiples valores de manera eficiente.