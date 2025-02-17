# [Linux] Bash arp uso: Gestionar la tabla ARP

El comando `arp` se utiliza para manipular y mostrar la tabla de resolución de direcciones de protocolo de Internet (ARP) en sistemas basados en Unix.

## Overview
El comando `arp` permite a los usuarios ver y modificar la tabla ARP, que asocia direcciones IP con direcciones MAC. Esto es útil para la resolución de direcciones en redes locales.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
arp [opciones] [argumentos]
```

## Common Options
- `-a`: Muestra la tabla ARP completa.
- `-d [dirección]`: Elimina una entrada específica de la tabla ARP.
- `-s [dirección] [dirección MAC]`: Agrega una nueva entrada a la tabla ARP.
- `-n`: Muestra las direcciones IP en formato numérico, sin intentar resolver los nombres de host.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `arp`:

1. **Mostrar la tabla ARP completa:**
   ```bash
   arp -a
   ```

2. **Eliminar una entrada específica de la tabla ARP:**
   ```bash
   arp -d 192.168.1.10
   ```

3. **Agregar una nueva entrada a la tabla ARP:**
   ```bash
   arp -s 192.168.1.20 00:1A:2B:3C:4D:5E
   ```

4. **Mostrar la tabla ARP sin resolver nombres de host:**
   ```bash
   arp -n
   ```

## Tips
- Asegúrate de tener privilegios de administrador al modificar la tabla ARP, ya que algunas operaciones requieren permisos elevados.
- Utiliza `arp -a` frecuentemente para verificar las entradas ARP y asegurarte de que no haya conflictos en la red.
- Recuerda que las entradas ARP pueden caducar, así que verifica periódicamente si necesitas agregar o actualizar entradas.