# [리눅스] Bash nslookup 사용법

## Overview
El comando `nslookup` (Name Server Lookup) es una herramienta de red utilizada para consultar el Sistema de Nombres de Dominio (DNS). Su propósito principal es permitir a los usuarios obtener información sobre direcciones IP y nombres de dominio, facilitando la resolución de nombres y la verificación de la configuración del DNS. Es especialmente útil para desarrolladores e ingenieros que necesitan diagnosticar problemas de conectividad o verificar la configuración de sus servidores DNS.

## Usage
La sintaxis básica del comando `nslookup` es la siguiente:

```bash
nslookup [opciones] [nombre_de_dominio]
```

### Opciones Comunes:
- `-type=tipo`: Especifica el tipo de registro DNS que se desea consultar (por ejemplo, `A`, `MX`, `CNAME`, etc.).
- `-debug`: Muestra información de depuración adicional sobre la consulta DNS.
- `-timeout=segundos`: Establece el tiempo de espera para la respuesta del servidor DNS.
- `-port=puerto`: Especifica el puerto a utilizar para la consulta (por defecto es el puerto 53).

## Examples
### Ejemplo 1: Consulta de un registro A
Para obtener la dirección IP asociada a un nombre de dominio, puedes usar el siguiente comando:

```bash
nslookup www.ejemplo.com
```

Este comando devolverá la dirección IP correspondiente a `www.ejemplo.com`.

### Ejemplo 2: Consulta de un registro MX
Si deseas consultar los registros de intercambio de correo (MX) para un dominio, puedes usar:

```bash
nslookup -type=MX ejemplo.com
```

Esto mostrará los servidores de correo que manejan los correos electrónicos para `ejemplo.com`.

## Tips
- Utiliza la opción `-debug` si necesitas más detalles sobre la consulta, lo cual puede ser útil para solucionar problemas.
- Si trabajas en un entorno donde hay múltiples servidores DNS, considera especificar el servidor DNS al que deseas enviar la consulta añadiendo la dirección IP del servidor al final del comando, por ejemplo:

```bash
nslookup www.ejemplo.com 8.8.8.8
```

Esto consultará a Google DNS (8.8.8.8) en lugar del servidor DNS configurado por defecto en tu sistema.