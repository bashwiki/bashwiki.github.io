# [Linux] Bash umask uso: Controla los permisos predeterminados de archivos y directorios

## Overview
El comando `umask` se utiliza en sistemas Unix y Linux para establecer los permisos predeterminados de los archivos y directorios que se crean en el sistema. Específicamente, define una "máscara" que determina qué permisos no se otorgarán a los nuevos archivos y directorios.

## Usage
La sintaxis básica del comando `umask` es la siguiente:

```bash
umask [opciones] [argumentos]
```

## Common Options
- `-S`: Muestra la máscara de permisos en formato simbólico.
- `-p`: Muestra la máscara de permisos actual en formato octal.

## Common Examples
1. **Ver la máscara de permisos actual:**
   ```bash
   umask
   ```

2. **Establecer una nueva máscara de permisos:**
   ```bash
   umask 027
   ```
   Esto establece que los nuevos archivos tendrán permisos de lectura y escritura para el propietario, y solo permisos de lectura para el grupo.

3. **Mostrar la máscara en formato simbólico:**
   ```bash
   umask -S
   ```

4. **Restablecer a la máscara por defecto:**
   ```bash
   umask 0022
   ```
   Esto permite que los archivos sean legibles por todos, pero solo el propietario puede escribir en ellos.

## Tips
- Recuerda que la máscara se aplica a los archivos y directorios creados después de que se establece. Para aplicar cambios, es posible que necesites reiniciar la sesión o ejecutar el comando en el contexto adecuado.
- Es recomendable establecer la máscara en archivos de configuración como `.bashrc` o `.profile` para que se aplique automáticamente en cada sesión.
- Ten cuidado al establecer una máscara demasiado permisiva, ya que puede comprometer la seguridad de tu sistema.