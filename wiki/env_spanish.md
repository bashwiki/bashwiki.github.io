# [Linux] Bash env uso equivalente: [gestionar variables de entorno]

## Overview
El comando `env` se utiliza en Bash para ejecutar un programa en un entorno modificado. Permite establecer o modificar variables de entorno antes de ejecutar un comando, lo que puede ser útil para cambiar configuraciones sin alterar el entorno global.

## Usage
La sintaxis básica del comando `env` es la siguiente:

```bash
env [opciones] [argumentos]
```

## Common Options
- `-i`: Ejecuta el comando en un entorno vacío, eliminando todas las variables de entorno existentes.
- `-u VARIABLE`: Elimina la variable de entorno especificada antes de ejecutar el comando.
- `VARIABLE=valor`: Establece una variable de entorno temporalmente para el comando que se va a ejecutar.

## Common Examples
1. **Ejecutar un comando con una variable de entorno específica:**

```bash
env MY_VAR=valor_comando ./mi_script.sh
```

2. **Eliminar una variable de entorno antes de ejecutar un comando:**

```bash
env -u MY_VAR ./mi_script.sh
```

3. **Ejecutar un comando en un entorno vacío:**

```bash
env -i bash
```

4. **Ver todas las variables de entorno actuales:**

```bash
env
```

## Tips
- Utiliza `env` para probar scripts en un entorno limpio, lo que puede ayudar a identificar problemas relacionados con variables de entorno.
- Al establecer variables de entorno, asegúrate de que no interfieran con otras configuraciones necesarias para el comando que estás ejecutando.
- Recuerda que las variables establecidas con `env` solo son válidas para el comando que se ejecuta y no afectan al entorno global.