# [Linux] Bash rev: Invertir líneas de texto

## Overview
El comando `rev` se utiliza para invertir el orden de los caracteres en cada línea de un archivo o entrada estándar. Es útil para manipular texto de manera sencilla y rápida.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
rev [opciones] [archivo]
```

## Common Options
- `-o, --output=archivo`: Especifica un archivo de salida en lugar de mostrar el resultado en la salida estándar.
- `-h, --help`: Muestra la ayuda del comando y sale.
- `-V, --version`: Muestra la versión del comando.

## Common Examples

1. **Invertir texto de un archivo:**
   Para invertir el contenido de un archivo llamado `texto.txt`:
   ```bash
   rev texto.txt
   ```

2. **Invertir texto desde la entrada estándar:**
   Puedes usar `rev` para invertir texto que ingreses directamente:
   ```bash
   echo "Hola Mundo" | rev
   ```

3. **Guardar la salida invertida en un nuevo archivo:**
   Para guardar el resultado en un archivo llamado `invertido.txt`:
   ```bash
   rev texto.txt > invertido.txt
   ```

4. **Invertir múltiples líneas:**
   Si deseas invertir varias líneas de texto:
   ```bash
   cat <<EOF | rev
   Línea uno
   Línea dos
   Línea tres
   EOF
   ```

## Tips
- Asegúrate de redirigir la salida a un archivo si deseas conservar el texto invertido.
- Puedes combinar `rev` con otros comandos de Unix para realizar tareas más complejas, como usarlo con `sort` o `grep`.
- Recuerda que `rev` solo invierte los caracteres en cada línea, no afecta el orden de las líneas en el archivo original.