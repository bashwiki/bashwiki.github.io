# [Linux] Bash paste Uso: Combina líneas de archivos

## Overview
El comando `paste` se utiliza en Bash para combinar líneas de varios archivos en una sola línea, separando los contenidos de cada archivo con un delimitador. Es especialmente útil para fusionar datos de diferentes fuentes en un formato más manejable.

## Usage
La sintaxis básica del comando `paste` es la siguiente:

```bash
paste [opciones] [archivos]
```

## Common Options
- `-d`: Especifica un delimitador diferente al predeterminado (tabulación).
- `-s`: Combina las líneas de cada archivo en una sola línea.
- `-z`: Usa un delimitador nulo, lo que permite combinar líneas sin ningún separador.

## Common Examples

1. **Combinar dos archivos con tabulaciones como delimitador:**

```bash
paste archivo1.txt archivo2.txt
```

2. **Usar un delimitador personalizado (coma):**

```bash
paste -d ',' archivo1.txt archivo2.txt
```

3. **Combinar líneas de un solo archivo en una sola línea:**

```bash
paste -s archivo.txt
```

4. **Combinar múltiples archivos usando un delimitador nulo:**

```bash
paste -z archivo1.txt archivo2.txt
```

## Tips
- Si deseas ver cómo se combinan los archivos sin modificar los originales, considera redirigir la salida a un nuevo archivo usando `>`:
  
  ```bash
  paste archivo1.txt archivo2.txt > combinado.txt
  ```

- Recuerda que `paste` solo funcionará correctamente si los archivos tienen el mismo número de líneas o si deseas combinar líneas de manera específica.
  
- Para visualizar el resultado en la terminal sin crear un nuevo archivo, simplemente ejecuta el comando sin redirección.