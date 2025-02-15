# [리눅스] Bash ufw 사용법

## Overview
`ufw` (Uncomplicated Firewall) es una herramienta de gestión de cortafuegos diseñada para facilitar la configuración de reglas de firewall en sistemas operativos basados en Linux. Su propósito principal es permitir o denegar el tráfico de red de manera sencilla, proporcionando una interfaz más amigable que las herramientas de firewall más complejas, como `iptables`. `ufw` es especialmente útil para administradores de sistemas y desarrolladores que buscan implementar medidas de seguridad de red sin complicaciones.

## Usage
La sintaxis básica del comando `ufw` es la siguiente:

```bash
ufw [opciones] [subcomando]
```

### Comandos Comunes
- `enable`: Activa el firewall.
- `disable`: Desactiva el firewall.
- `allow [puerto]`: Permite el tráfico a través del puerto especificado.
- `deny [puerto]`: Deniega el tráfico a través del puerto especificado.
- `status`: Muestra el estado actual del firewall y las reglas configuradas.

### Ejemplo de Uso
1. **Activar el firewall**:
   ```bash
   sudo ufw enable
   ```
   Este comando activa el firewall, comenzando a aplicar las reglas configuradas.

2. **Permitir tráfico HTTP**:
   ```bash
   sudo ufw allow 80
   ```
   Este comando permite el tráfico a través del puerto 80, que es el puerto estándar para HTTP.

## Tips
- **Verifica el estado del firewall**: Siempre es una buena práctica verificar el estado del firewall después de realizar cambios. Puedes hacerlo con el comando `ufw status`.
- **Reglas específicas**: Si necesitas permitir tráfico desde una dirección IP específica, puedes usar `sudo ufw allow from [IP] to any port [puerto]`.
- **Registro de actividad**: Habilita el registro de `ufw` para monitorear la actividad del firewall utilizando `sudo ufw logging on`.
- **Desactivar temporalmente**: Si necesitas realizar pruebas, puedes desactivar temporalmente el firewall con `sudo ufw disable` y volver a activarlo posteriormente.

Usar `ufw` de manera efectiva puede ayudar a asegurar tu sistema y protegerlo contra accesos no autorizados.