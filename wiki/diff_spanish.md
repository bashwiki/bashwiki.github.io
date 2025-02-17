# [Linux] Bash diff uso equivalente: Comparar archivos y mostrar diferencias

## Overview
El comando `diff` se utiliza para comparar archivos de texto línea por línea. Muestra las diferencias entre dos archivos, lo que es útil para identificar cambios, errores o diferencias en el contenido.

## Usage
La sintaxis básica del comando `diff` es la siguiente:

```bash
diff [opciones] [archivo1] [archivo2]
```

## Common Options
- `-u`: Muestra las diferencias en un formato unificado, que es más fácil de leer.
- `-c`: Muestra las diferencias en un formato de contexto, proporcionando más información sobre las líneas alrededor de las diferencias.
- `-i`: Ignora las diferencias entre mayúsculas y minúsculas.
- `-w`: Ignora los espacios en blanco al comparar líneas.
- `-r`: Compara directorios de forma recursiva.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `diff`:

1. Comparar dos archivos de texto:
   ```bash
   diff archivo1.txt archivo2.txt
   ```

2. Usar el formato unificado para ver las diferencias:
   ```bash
   diff -u archivo1.txt archivo2.txt
   ```

3. Ignorar diferencias de mayúsculas y minúsculas:
   ```bash
   diff -i archivo1.txt archivo2.txt
   ```

4. Comparar dos directorios recursivamente:
   ```bash
   diff -r directorio1/ directorio2/
   ```

5. Mostrar diferencias en formato de contexto:
   ```bash
   diff -c archivo1.txt archivo2.txt
   ```

## Tips
- Utiliza la opción `-u` para obtener un resumen más claro de las diferencias, especialmente útil al revisar cambios en código.
- Si trabajas con archivos grandes, considera redirigir la salida a un archivo usando `>` para revisarlo más tarde:
  ```bash
  diff archivo1.txt archivo2.txt > diferencias.txt
  ```
- Para una comparación más visual, puedes combinar `diff` con herramientas como `vimdiff` o `meld`.