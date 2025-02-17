# [Linux] Bash lsattr Uso equivalente: Muestra atributos de archivos

## Overview
El comando `lsattr` se utiliza en sistemas Linux para mostrar los atributos de los archivos en un directorio. Estos atributos pueden afectar cómo se manejan los archivos, como si son inmutables o si se pueden eliminar.

## Usage
La sintaxis básica del comando `lsattr` es la siguiente:

```bash
lsattr [opciones] [argumentos]
```

## Common Options
- `-a`: Muestra todos los archivos, incluyendo los ocultos.
- `-d`: Muestra los atributos de los directorios en lugar de los archivos.
- `-R`: Realiza una búsqueda recursiva en los subdirectorios.
- `-v`: Muestra información adicional sobre los atributos.

## Common Examples
1. **Mostrar atributos de archivos en el directorio actual:**

   ```bash
   lsattr
   ```

2. **Mostrar atributos de archivos, incluyendo los ocultos:**

   ```bash
   lsattr -a
   ```

3. **Mostrar atributos de un directorio específico:**

   ```bash
   lsattr -d /ruta/al/directorio
   ```

4. **Mostrar atributos de archivos de manera recursiva:**

   ```bash
   lsattr -R /ruta/al/directorio
   ```

5. **Mostrar atributos con información adicional:**

   ```bash
   lsattr -v
   ```

## Tips
- Utiliza `lsattr` junto con `chattr` para modificar los atributos de los archivos.
- Verifica los atributos de archivos críticos del sistema para evitar cambios no deseados.
- Recuerda que algunos atributos pueden requerir permisos de superusuario para ser visualizados o modificados.