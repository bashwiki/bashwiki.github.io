# [Linux] Bash lspci Uso: Muestra información sobre dispositivos PCI

## Overview
El comando `lspci` se utiliza en sistemas Linux para listar todos los dispositivos conectados al bus PCI (Peripheral Component Interconnect). Este comando es útil para obtener información detallada sobre el hardware del sistema, como tarjetas gráficas, controladores de red y otros dispositivos.

## Usage
La sintaxis básica del comando `lspci` es la siguiente:

```bash
lspci [opciones] [argumentos]
```

## Common Options
A continuación se presentan algunas opciones comunes que se pueden utilizar con `lspci`:

- `-v`: Muestra información detallada sobre cada dispositivo.
- `-vv`: Muestra aún más información detallada.
- `-k`: Muestra los controladores utilizados por cada dispositivo.
- `-n`: Muestra los identificadores de los dispositivos en formato numérico.
- `-s <slot>`: Muestra información solo para el dispositivo en el slot especificado.

## Common Examples

1. **Listar todos los dispositivos PCI:**
   ```bash
   lspci
   ```

2. **Mostrar información detallada sobre los dispositivos:**
   ```bash
   lspci -v
   ```

3. **Mostrar controladores utilizados por los dispositivos:**
   ```bash
   lspci -k
   ```

4. **Listar dispositivos con identificadores numéricos:**
   ```bash
   lspci -n
   ```

5. **Mostrar información de un dispositivo específico:**
   ```bash
   lspci -s 00:1f.0
   ```

## Tips
- Utiliza `lspci | less` para paginar la salida si hay muchos dispositivos listados.
- Combina `lspci` con `grep` para buscar un dispositivo específico. Por ejemplo:
  ```bash
  lspci | grep -i vga
  ```
- Si necesitas más información sobre un dispositivo, puedes usar `lspci -vv -s <slot>` para obtener detalles extensos.