# [리눅스] Bash firewalld 사용법

## Overview
El comando `firewalld` es una herramienta de gestión de cortafuegos en sistemas Linux que proporciona una interfaz dinámica para administrar las reglas de firewall. Su propósito principal es facilitar la configuración y el mantenimiento de las políticas de seguridad de red, permitiendo a los administradores definir qué tráfico de red se permite o se bloquea en función de zonas y servicios.

## Usage
La sintaxis básica del comando `firewalld` es la siguiente:

```bash
firewalld [opciones]
```

### Opciones Comunes:
- `--zone=<zona>`: Especifica la zona en la que se aplicarán las reglas.
- `--add-service=<servicio>`: Agrega un servicio específico a la zona.
- `--remove-service=<servicio>`: Elimina un servicio de la zona.
- `--add-port=<puerto>/<protocolo>`: Abre un puerto específico para el tráfico.
- `--remove-port=<puerto>/<protocolo>`: Cierra un puerto específico para el tráfico.
- `--list-all`: Muestra todas las configuraciones de la zona actual.

## Examples
### Ejemplo 1: Agregar un servicio
Para permitir el tráfico HTTP en la zona pública, puedes usar el siguiente comando:

```bash
firewall-cmd --zone=public --add-service=http --permanent
```
Este comando agrega el servicio HTTP a la zona pública de manera permanente. Para que los cambios surtan efecto, es necesario recargar la configuración:

```bash
firewall-cmd --reload
```

### Ejemplo 2: Abrir un puerto específico
Si deseas abrir el puerto 8080 para el tráfico TCP, puedes usar el siguiente comando:

```bash
firewall-cmd --zone=public --add-port=8080/tcp --permanent
```
Recuerda recargar la configuración después de hacer cambios.

## Tips
- Siempre utiliza la opción `--permanent` si deseas que los cambios persistan después de reiniciar el servicio `firewalld`.
- Usa `firewall-cmd --list-all` para verificar la configuración actual de la zona y asegurarte de que los cambios se hayan aplicado correctamente.
- Considera crear zonas personalizadas para diferentes tipos de redes (por ejemplo, trabajo, hogar, público) para gestionar mejor las reglas de firewall.
- Realiza copias de seguridad de la configuración antes de realizar cambios significativos, para poder restaurar fácilmente si es necesario.