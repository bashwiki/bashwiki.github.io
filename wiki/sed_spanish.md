# [Linux] Bash sed Uso: Herramienta para la manipulación de texto

## Overview
El comando `sed` (stream editor) es una herramienta poderosa en Bash que permite realizar transformaciones y manipulaciones de texto de manera no interactiva. Se utiliza comúnmente para buscar, reemplazar, insertar o eliminar texto en archivos o flujos de datos.

## Usage
La sintaxis básica del comando `sed` es la siguiente:

```bash
sed [opciones] [argumentos]
```

## Common Options
- `-e`: Permite agregar múltiples expresiones de edición.
- `-i`: Edita archivos en su lugar (in-place), modificando el archivo original.
- `-n`: Suprime la salida automática, permitiendo mostrar solo las líneas especificadas.
- `s/patrón/reemplazo/`: Realiza una sustitución del patrón encontrado por el texto de reemplazo.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `sed`:

1. **Reemplazar texto en un archivo:**
   ```bash
   sed 's/hola/adiós/' archivo.txt
   ```
   Este comando reemplaza la primera aparición de "hola" por "adiós" en cada línea de `archivo.txt`.

2. **Reemplazar texto en todas las apariciones:**
   ```bash
   sed 's/hola/adiós/g' archivo.txt
   ```
   Aquí, el modificador `g` asegura que todas las apariciones de "hola" sean reemplazadas por "adiós".

3. **Eliminar líneas que contienen un patrón:**
   ```bash
   sed '/patrón/d' archivo.txt
   ```
   Este comando elimina todas las líneas que contienen "patrón" en `archivo.txt`.

4. **Modificar el archivo original:**
   ```bash
   sed -i 's/hola/adiós/g' archivo.txt
   ```
   Con la opción `-i`, este comando reemplaza "hola" por "adiós" directamente en `archivo.txt`.

5. **Mostrar solo líneas que coinciden con un patrón:**
   ```bash
   sed -n '/patrón/p' archivo.txt
   ```
   Este comando muestra solo las líneas que contienen "patrón" en `archivo.txt`.

## Tips
- Siempre es recomendable hacer una copia de seguridad de los archivos antes de usar la opción `-i`, ya que modifica el archivo original.
- Puedes usar expresiones regulares en `sed` para patrones más complejos.
- Combina `sed` con otros comandos como `grep` o `awk` para tareas más avanzadas de procesamiento de texto.