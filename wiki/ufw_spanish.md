# [Linux] Bash ufw Uso: Controlar el acceso a la red

## Overview
El comando `ufw` (Uncomplicated Firewall) es una herramienta de línea de comandos diseñada para facilitar la gestión de un cortafuegos en sistemas basados en Linux. Permite a los usuarios permitir o denegar el tráfico de red de manera sencilla, proporcionando una interfaz más accesible que las configuraciones de firewall tradicionales.

## Usage
La sintaxis básica del comando `ufw` es la siguiente:

```
ufw [opciones] [argumentos]
```

## Common Options
- `enable`: Activa el cortafuegos.
- `disable`: Desactiva el cortafuegos.
- `allow [puerto]`: Permite el tráfico a un puerto específico.
- `deny [puerto]`: Deniega el tráfico a un puerto específico.
- `status`: Muestra el estado actual del cortafuegos.
- `reset`: Restablece las reglas del cortafuegos a su estado predeterminado.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `ufw`:

1. **Activar el cortafuegos:**
   ```bash
   sudo ufw enable
   ```

2. **Desactivar el cortafuegos:**
   ```bash
   sudo ufw disable
   ```

3. **Permitir el tráfico en el puerto 22 (SSH):**
   ```bash
   sudo ufw allow 22
   ```

4. **Denegar el tráfico en el puerto 80 (HTTP):**
   ```bash
   sudo ufw deny 80
   ```

5. **Ver el estado del cortafuegos:**
   ```bash
   sudo ufw status
   ```

6. **Restablecer las reglas del cortafuegos:**
   ```bash
   sudo ufw reset
   ```

## Tips
- Siempre verifica el estado de tu cortafuegos después de realizar cambios usando `ufw status`.
- Considera habilitar el cortafuegos al inicio del sistema para una mayor seguridad.
- Usa `ufw allow` y `ufw deny` con cuidado para evitar bloquear accidentalmente el acceso a servicios importantes.