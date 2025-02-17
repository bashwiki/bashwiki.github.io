# [Linux] Bash uniq Uso: Eliminar líneas duplicadas de un archivo

## Overview
El comando `uniq` se utiliza en Bash para eliminar líneas duplicadas de un archivo o de la entrada estándar. Es especialmente útil cuando se trabaja con archivos de texto donde se desea obtener una lista de elementos únicos.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
uniq [opciones] [archivo]
```

## Common Options
- `-c`: Cuenta el número de ocurrencias de cada línea.
- `-d`: Muestra solo las líneas duplicadas.
- `-u`: Muestra solo las líneas únicas.
- `-i`: Ignora la distinción entre mayúsculas y minúsculas.
- `-w N`: Compara solo los primeros N caracteres de cada línea.

## Common Examples

1. **Eliminar líneas duplicadas de un archivo:**
   ```bash
   uniq archivo.txt
   ```

2. **Contar las ocurrencias de cada línea:**
   ```bash
   uniq -c archivo.txt
   ```

3. **Mostrar solo líneas duplicadas:**
   ```bash
   uniq -d archivo.txt
   ```

4. **Mostrar solo líneas únicas:**
   ```bash
   uniq -u archivo.txt
   ```

5. **Ignorar mayúsculas y minúsculas:**
   ```bash
   uniq -i archivo.txt
   ```

6. **Comparar solo los primeros N caracteres:**
   ```bash
   uniq -w 5 archivo.txt
   ```

## Tips
- Asegúrate de que el archivo esté ordenado antes de usar `uniq`, ya que solo elimina duplicados adyacentes.
- Puedes combinar `uniq` con otros comandos como `sort` para obtener resultados más precisos.
- Utiliza la opción `-c` para obtener un resumen de cuántas veces aparece cada línea, lo que puede ser útil para análisis de datos.