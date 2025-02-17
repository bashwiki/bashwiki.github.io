# [Linux] Bash iptables Uso: Control de tráfico de red

## Overview
El comando `iptables` se utiliza en sistemas Linux para configurar, gestionar y mantener las reglas de filtrado de paquetes en el firewall. Permite a los administradores de sistemas controlar el tráfico de red, permitiendo o bloqueando paquetes según diversas condiciones.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
iptables [options] [arguments]
```

## Common Options
- `-A` : Añadir una regla a una cadena.
- `-D` : Eliminar una regla de una cadena.
- `-L` : Listar las reglas actuales en las cadenas.
- `-F` : Limpiar todas las reglas en las cadenas.
- `-P` : Establecer la política predeterminada para una cadena.
- `-I` : Insertar una regla en una posición específica de una cadena.

## Common Examples
1. **Listar todas las reglas actuales:**
   ```bash
   iptables -L
   ```

2. **Añadir una regla para permitir tráfico HTTP:**
   ```bash
   iptables -A INPUT -p tcp --dport 80 -j ACCEPT
   ```

3. **Bloquear tráfico SSH:**
   ```bash
   iptables -A INPUT -p tcp --dport 22 -j DROP
   ```

4. **Eliminar una regla específica:**
   ```bash
   iptables -D INPUT -p tcp --dport 80 -j ACCEPT
   ```

5. **Establecer la política predeterminada para bloquear todo el tráfico:**
   ```bash
   iptables -P INPUT DROP
   ```

## Tips
- Siempre realiza una copia de seguridad de tus reglas actuales antes de hacer cambios importantes.
- Utiliza `iptables-save` y `iptables-restore` para guardar y restaurar configuraciones de reglas.
- Prueba tus reglas en un entorno de desarrollo antes de aplicarlas en producción para evitar interrupciones inesperadas.