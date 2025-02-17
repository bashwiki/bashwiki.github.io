# [Linux] Bash hostname uso: [muestra el nombre del host]

## Overview
El comando `hostname` se utiliza para mostrar o establecer el nombre del host del sistema. Este nombre es esencial para identificar la máquina en una red y puede ser utilizado por varias aplicaciones y servicios.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
hostname [opciones] [argumentos]
```

## Common Options
- `-a`, `--alias`: Muestra el alias del host.
- `-d`, `--domain`: Muestra el dominio del host.
- `-f`, `--fqdn`: Muestra el nombre de dominio completamente calificado (FQDN).
- `-i`, `--ip-address`: Muestra la dirección IP del host.
- `-s`, `--short`: Muestra solo el nombre corto del host.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `hostname`:

1. **Mostrar el nombre del host actual:**
   ```bash
   hostname
   ```

2. **Mostrar el nombre de dominio completamente calificado:**
   ```bash
   hostname -f
   ```

3. **Mostrar la dirección IP del host:**
   ```bash
   hostname -i
   ```

4. **Establecer un nuevo nombre de host:**
   ```bash
   sudo hostname nuevo-nombre
   ```

5. **Mostrar solo el nombre corto del host:**
   ```bash
   hostname -s
   ```

## Tips
- Asegúrate de tener privilegios de superusuario al cambiar el nombre del host, ya que se requiere para realizar esta acción.
- Después de cambiar el nombre del host, considera reiniciar el sistema o el servicio de red para que los cambios surtan efecto.
- Utiliza `hostname -d` para verificar el dominio de tu máquina, lo que puede ser útil en configuraciones de red.