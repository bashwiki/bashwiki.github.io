# [Linux] Bash export Uso equivalente: Establecer variables de entorno

El comando `export` se utiliza en Bash para establecer variables de entorno que estarán disponibles para los procesos hijos del shell.

## Overview
El comando `export` permite que las variables definidas en el entorno del shell se conviertan en variables de entorno, lo que significa que estarán disponibles para cualquier programa o script que se ejecute desde ese shell. Esto es útil para configurar configuraciones que deben ser accesibles en diferentes contextos.

## Usage
La sintaxis básica del comando `export` es la siguiente:

```bash
export [opciones] [argumentos]
```

## Common Options
- `-p`: Muestra todas las variables de entorno exportadas.
- `-n`: Elimina la exportación de una variable, haciéndola local al shell.
- `-f`: Exporta funciones en lugar de variables.

## Common Examples

1. **Exportar una variable simple:**
   ```bash
   MY_VAR="Hola Mundo"
   export MY_VAR
   ```

2. **Exportar y asignar en una sola línea:**
   ```bash
   export MY_VAR="Hola Mundo"
   ```

3. **Ver las variables de entorno exportadas:**
   ```bash
   export -p
   ```

4. **Eliminar la exportación de una variable:**
   ```bash
   export -n MY_VAR
   ```

5. **Exportar una función:**
   ```bash
   my_function() {
       echo "Esta es una función exportada"
   }
   export -f my_function
   ```

## Tips
- Siempre verifica las variables de entorno exportadas usando `export -p` para evitar conflictos.
- Utiliza nombres de variables descriptivos para facilitar la comprensión de su propósito.
- Recuerda que las variables exportadas solo estarán disponibles para los procesos hijos, no para el shell padre.