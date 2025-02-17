# [Linux] Bash scp Uso: Copiar archivos de forma segura entre sistemas

## Overview
El comando `scp` (Secure Copy Protocol) se utiliza para copiar archivos y directorios de manera segura entre sistemas a través de una red. Utiliza el protocolo SSH para garantizar que la transferencia de datos sea segura y encriptada.

## Usage
La sintaxis básica del comando `scp` es la siguiente:

```bash
scp [opciones] [origen] [destino]
```

## Common Options
- `-r`: Copia directorios de manera recursiva.
- `-P`: Especifica el puerto a utilizar en el servidor remoto.
- `-i`: Permite especificar una clave privada para la autenticación.
- `-v`: Muestra información detallada sobre el proceso de copia, útil para la depuración.

## Common Examples
1. **Copiar un archivo local a un servidor remoto:**
   ```bash
   scp archivo.txt usuario@servidor:/ruta/destino/
   ```

2. **Copiar un archivo desde un servidor remoto a la máquina local:**
   ```bash
   scp usuario@servidor:/ruta/origen/archivo.txt /ruta/local/
   ```

3. **Copiar un directorio completo a un servidor remoto:**
   ```bash
   scp -r /ruta/local/directorio usuario@servidor:/ruta/destino/
   ```

4. **Copiar un archivo utilizando un puerto específico:**
   ```bash
   scp -P 2222 archivo.txt usuario@servidor:/ruta/destino/
   ```

5. **Usar una clave privada para la autenticación:**
   ```bash
   scp -i /ruta/a/clave_privada archivo.txt usuario@servidor:/ruta/destino/
   ```

## Tips
- Asegúrate de tener permisos adecuados en el destino para evitar errores de acceso.
- Utiliza la opción `-v` para obtener más información si encuentras problemas durante la transferencia.
- Considera usar `rsync` si necesitas sincronizar archivos de manera más eficiente, ya que puede ser más rápido en transferencias sucesivas.