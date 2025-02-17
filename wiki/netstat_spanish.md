# [Linux] Bash netstat Uso: Muestra conexiones de red y estadísticas

## Overview
El comando `netstat` es una herramienta de línea de comandos que se utiliza para mostrar conexiones de red, tablas de enrutamiento, estadísticas de interfaz y otras informaciones relacionadas con la red en sistemas operativos basados en Unix. Es útil para diagnosticar problemas de red y monitorear el estado de las conexiones.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
netstat [opciones] [argumentos]
```

## Common Options
A continuación se presentan algunas opciones comunes que se pueden utilizar con el comando `netstat`:

- `-a`: Muestra todas las conexiones y puertos de escucha.
- `-t`: Muestra solo las conexiones TCP.
- `-u`: Muestra solo las conexiones UDP.
- `-n`: Muestra las direcciones y números de puerto en formato numérico.
- `-l`: Muestra solo los puertos que están en estado de escucha.
- `-p`: Muestra el identificador del proceso (PID) y el nombre del programa que está utilizando la conexión.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `netstat`:

1. **Mostrar todas las conexiones y puertos de escucha:**
   ```bash
   netstat -a
   ```

2. **Mostrar solo las conexiones TCP:**
   ```bash
   netstat -t
   ```

3. **Mostrar solo las conexiones UDP:**
   ```bash
   netstat -u
   ```

4. **Mostrar conexiones con direcciones y puertos en formato numérico:**
   ```bash
   netstat -n
   ```

5. **Mostrar puertos en estado de escucha:**
   ```bash
   netstat -l
   ```

6. **Mostrar conexiones junto con el PID y el nombre del programa:**
   ```bash
   netstat -p
   ```

## Tips
- Utiliza `netstat -tuln` para obtener una visión rápida de los puertos TCP y UDP que están en escucha.
- Combina opciones, como `netstat -tunlp`, para obtener información más detallada sobre las conexiones activas y los procesos asociados.
- Recuerda que en algunos sistemas, es posible que necesites permisos de superusuario para ver información completa sobre los procesos.