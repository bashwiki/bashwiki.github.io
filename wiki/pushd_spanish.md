# [Linux] Bash pushd uso: Cambiar directorios de forma eficiente

## Overview
El comando `pushd` se utiliza en Bash para cambiar de directorio y, al mismo tiempo, guardar el directorio actual en una pila. Esto permite navegar fácilmente entre directorios sin perder el rastro de la ubicación anterior.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
pushd [opciones] [argumentos]
```

## Common Options
- `+n`: Cambia al directorio en la posición `n` de la pila.
- `-n`: Cambia al directorio en la posición `-n` de la pila.
- `-`: Regresa al último directorio visitado.

## Common Examples
1. **Cambiar a un nuevo directorio y guardar el actual:**
   ```bash
   pushd /ruta/al/nuevo/directorio
   ```

2. **Volver al directorio anterior:**
   ```bash
   pushd -
   ```

3. **Acceder a un directorio en la pila:**
   ```bash
   pushd +1
   ```

4. **Ver la pila de directorios:**
   ```bash
   dirs
   ```

## Tips
- Utiliza `popd` para regresar al directorio anterior y eliminarlo de la pila.
- Combina `pushd` con `popd` para crear un flujo de trabajo eficiente al cambiar entre varios directorios.
- Recuerda que puedes ver el estado actual de la pila de directorios usando el comando `dirs`.