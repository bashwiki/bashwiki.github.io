# [Linux] Bash fgrep Uso: Buscar cadenas exactas en archivos

## Overview
El comando `fgrep` se utiliza en Bash para buscar cadenas de texto exactas dentro de archivos. A diferencia de `grep`, que permite expresiones regulares, `fgrep` se centra en coincidencias literales, lo que lo hace útil para buscar términos específicos sin complicaciones.

## Usage
La sintaxis básica del comando `fgrep` es la siguiente:

```bash
fgrep [opciones] [argumentos]
```

## Common Options
- `-i`: Ignora mayúsculas y minúsculas durante la búsqueda.
- `-v`: Inversa la coincidencia, mostrando líneas que no contienen la cadena.
- `-c`: Muestra solo el conteo de líneas que coinciden con la búsqueda.
- `-n`: Muestra el número de línea junto con las coincidencias.
- `-r`: Busca recursivamente en directorios.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `fgrep`:

1. **Buscar una cadena exacta en un archivo:**
   ```bash
   fgrep "texto específico" archivo.txt
   ```

2. **Buscar una cadena ignorando mayúsculas y minúsculas:**
   ```bash
   fgrep -i "Texto Específico" archivo.txt
   ```

3. **Contar cuántas líneas coinciden con la cadena:**
   ```bash
   fgrep -c "cadena" archivo.txt
   ```

4. **Mostrar líneas que no contienen la cadena:**
   ```bash
   fgrep -v "cadena" archivo.txt
   ```

5. **Buscar en todos los archivos de un directorio:**
   ```bash
   fgrep -r "cadena" /ruta/al/directorio
   ```

## Tips
- Utiliza `fgrep` cuando necesites realizar búsquedas rápidas y exactas sin preocuparte por las expresiones regulares.
- Combina `fgrep` con redirección para guardar resultados en un archivo:
  ```bash
  fgrep "cadena" archivo.txt > resultados.txt
  ```
- Recuerda que `fgrep` es más eficiente que `grep` para búsquedas literales, así que elige el comando adecuado según tus necesidades.