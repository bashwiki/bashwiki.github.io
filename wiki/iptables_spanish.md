# [리눅스] Bash iptables 사용법

## Overview
El comando `iptables` es una herramienta de administración de firewall en sistemas Linux que permite a los usuarios configurar, mantener y supervisar las reglas de filtrado de paquetes en el kernel de Linux. Su propósito principal es controlar el tráfico de red permitiendo o denegando paquetes según las reglas definidas por el usuario. `iptables` es fundamental para la seguridad de los sistemas, ya que ayuda a protegerlos de accesos no autorizados y ataques maliciosos.

## Usage
La sintaxis básica del comando `iptables` es la siguiente:

```bash
iptables [opciones] [cadena] [regla]
```

### Opciones Comunes:
- `-A`: Añadir una regla a una cadena.
- `-D`: Eliminar una regla de una cadena.
- `-L`: Listar las reglas en las cadenas.
- `-F`: Limpiar todas las reglas en las cadenas.
- `-P`: Establecer la política predeterminada para una cadena.
- `-I`: Insertar una regla en una posición específica de una cadena.

### Cadenas Comunes:
- `INPUT`: Para el tráfico que va hacia el sistema.
- `OUTPUT`: Para el tráfico que sale del sistema.
- `FORWARD`: Para el tráfico que se reenvía a través del sistema.

## Examples
### Ejemplo 1: Listar Reglas Actuales
Para ver las reglas actuales configuradas en el firewall, puedes usar el siguiente comando:

```bash
iptables -L -n -v
```
Este comando lista todas las reglas en las cadenas, mostrando el número de paquetes y bytes que han coincidido con cada regla.

### Ejemplo 2: Permitir Tráfico SSH
Para permitir el tráfico SSH (puerto 22) en tu firewall, puedes añadir la siguiente regla:

```bash
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```
Este comando añade una regla a la cadena `INPUT` que acepta paquetes TCP dirigidos al puerto 22.

## Tips
- **Guardar Configuraciones**: Asegúrate de guardar tus reglas de `iptables` después de configurarlas, ya que se perderán tras un reinicio. Puedes usar `iptables-save` para exportar las reglas a un archivo.
- **Pruebas**: Siempre prueba tus reglas en un entorno seguro antes de aplicarlas en producción para evitar bloqueos accidentales.
- **Documentación**: Consulta la página de manual de `iptables` (`man iptables`) para obtener información detallada sobre todas las opciones y características disponibles.