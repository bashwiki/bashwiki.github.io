# [Linux] Bash bash uso: Ejecutar comandos en la terminal

## Overview
El comando `bash` se utiliza para invocar el intérprete de comandos de Bash, que permite a los usuarios ejecutar scripts y comandos en la línea de comandos de un sistema operativo basado en Unix. Bash es un shell muy popular que ofrece una amplia gama de funcionalidades para la automatización y la administración del sistema.

## Usage
La sintaxis básica del comando `bash` es la siguiente:

```bash
bash [opciones] [archivo]
```

## Common Options
- `-c`: Ejecuta un comando especificado como una cadena.
- `-i`: Inicia un shell interactivo.
- `-l`: Inicia un shell como un login shell.
- `-s`: Lee comandos desde la entrada estándar.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `bash`:

1. **Ejecutar un script de Bash**:
   ```bash
   bash script.sh
   ```

2. **Ejecutar un comando directamente**:
   ```bash
   bash -c 'echo "Hola, mundo!"'
   ```

3. **Iniciar un shell interactivo**:
   ```bash
   bash -i
   ```

4. **Ejecutar un script desde la entrada estándar**:
   ```bash
   echo -e 'echo "Ejecutando desde stdin"' | bash -s
   ```

## Tips
- Siempre verifica los permisos de tu script antes de ejecutarlo con `bash`, asegurándote de que sea ejecutable.
- Utiliza `bash -x script.sh` para depurar un script y ver qué comandos se están ejecutando.
- Familiarízate con las variables de entorno de Bash, ya que pueden facilitar la personalización de tu entorno de trabajo.