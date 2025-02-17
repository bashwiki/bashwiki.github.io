# [Linux] Bash lsusb Uso equivalente en español: listar dispositivos USB conectados

## Overview
El comando `lsusb` se utiliza para mostrar información sobre los dispositivos USB conectados al sistema. Proporciona detalles como el ID del fabricante, el ID del producto y la descripción del dispositivo, lo que resulta útil para identificar y diagnosticar dispositivos USB.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
lsusb [opciones] [argumentos]
```

## Common Options
- `-v`: Muestra información detallada sobre los dispositivos USB.
- `-t`: Muestra la topología de los dispositivos USB en un formato de árbol.
- `-s [bus]:[device]`: Muestra información solo para el dispositivo específico en el bus y el número de dispositivo dados.
- `-d [vendor]:[product]`: Muestra información solo para dispositivos que coinciden con el ID del vendedor y el ID del producto especificados.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `lsusb`:

1. **Listar todos los dispositivos USB conectados:**
   ```bash
   lsusb
   ```

2. **Mostrar información detallada sobre todos los dispositivos USB:**
   ```bash
   lsusb -v
   ```

3. **Mostrar la topología de los dispositivos USB:**
   ```bash
   lsusb -t
   ```

4. **Mostrar información de un dispositivo específico:**
   ```bash
   lsusb -s 001:002
   ```

5. **Filtrar dispositivos por ID de vendedor y producto:**
   ```bash
   lsusb -d 1234:5678
   ```

## Tips
- Utiliza `lsusb -v` con precaución, ya que puede generar una gran cantidad de información, especialmente si tienes muchos dispositivos conectados.
- Combina `lsusb` con otros comandos como `grep` para filtrar resultados específicos.
- Revisa la documentación del sistema (`man lsusb`) para obtener más detalles sobre las opciones disponibles y su uso.