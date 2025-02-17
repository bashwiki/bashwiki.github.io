# [Linux] Bash true uso equivalente: Comando que siempre devuelve éxito

## Overview
El comando `true` en Bash es una utilidad que no realiza ninguna acción y siempre devuelve un estado de salida exitoso (0). Es útil en scripts y en situaciones donde se requiere un comando que no haga nada, pero que aún así indique que se ha ejecutado correctamente.

## Usage
La sintaxis básica del comando `true` es la siguiente:

```bash
true [opciones]
```

## Common Options
El comando `true` no tiene opciones específicas. Simplemente se ejecuta tal cual. Sin embargo, se puede usar en combinación con otros comandos o en scripts.

## Common Examples

### Ejemplo 1: Uso básico
Ejecutar el comando `true` simplemente devolverá un estado de éxito.
```bash
true
echo $?
```
Este comando imprimirá `0`, indicando que `true` se ejecutó correctamente.

### Ejemplo 2: Uso en un bucle
Se puede utilizar `true` en un bucle infinito, aunque generalmente no se recomienda.
```bash
while true; do
  echo "Este bucle nunca terminará."
done
```

### Ejemplo 3: Combinación con `&&`
Se puede usar `true` para asegurar que un comando previo se ejecute sin errores.
```bash
mkdir nueva_carpeta && true
```
En este caso, si `mkdir` tiene éxito, `true` se ejecutará y devolverá un estado de éxito.

### Ejemplo 4: Uso en scripts
`true` se puede usar en scripts para crear un marcador de posición.
```bash
#!/bin/bash
# Este script no hace nada, pero se ejecuta correctamente
true
```

## Tips
- Utiliza `true` como un marcador de posición en scripts en desarrollo.
- Combina `true` con otros comandos para manejar flujos de control en scripts.
- Recuerda que `true` siempre devuelve un estado de éxito, lo que puede ser útil en condiciones de prueba.