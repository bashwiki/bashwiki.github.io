# [리눅스] Bash export 사용법

## Overview
El comando `export` en Bash se utiliza para establecer variables de entorno que estarán disponibles para los procesos hijos del shell actual. Al exportar una variable, se garantiza que cualquier programa o script que se ejecute desde el shell pueda acceder a esa variable. Esto es especialmente útil para configurar entornos de desarrollo y producción, donde ciertas configuraciones deben ser accesibles para diferentes aplicaciones.

## Usage
La sintaxis básica del comando `export` es la siguiente:

```bash
export VARIABLE=valor
```

Donde `VARIABLE` es el nombre de la variable que deseas exportar y `valor` es el valor que deseas asignarle. Si deseas exportar una variable que ya ha sido definida, simplemente puedes usar:

```bash
export VARIABLE
```

### Opciones Comunes
- `-p`: Muestra todas las variables de entorno exportadas.
- `-n`: Elimina la exportación de una variable, haciéndola local al shell actual.

## Examples
### Ejemplo 1: Exportar una nueva variable
Para crear y exportar una nueva variable llamada `MY_VAR` con el valor `Hello World`, puedes usar el siguiente comando:

```bash
export MY_VAR="Hello World"
```

Ahora, cualquier proceso hijo que se ejecute desde este shell podrá acceder a `MY_VAR`.

### Ejemplo 2: Verificar variables exportadas
Para ver todas las variables de entorno que has exportado, puedes usar el comando:

```bash
export -p
```

Esto mostrará una lista de todas las variables de entorno actualmente exportadas en el shell.

## Tips
- Es recomendable usar nombres de variables en mayúsculas para las variables de entorno, ya que esto ayuda a diferenciarlas de las variables locales.
- Si deseas que una variable esté disponible en todos los shells y no solo en el actual, considera agregar el comando `export` en tu archivo de configuración del shell, como `~/.bashrc` o `~/.bash_profile`.
- Recuerda que las variables de entorno exportadas solo estarán disponibles para los procesos hijos que se inician después de la exportación. Los procesos que ya se están ejecutando no verán los cambios.