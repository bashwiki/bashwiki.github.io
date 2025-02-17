# [Linux] Bash firewalld uso: Gestionar la configuración del cortafuegos

## Overview
El comando `firewalld` es una herramienta de gestión de cortafuegos que proporciona una interfaz fácil de usar para configurar reglas de seguridad en sistemas Linux. Permite gestionar las reglas de filtrado de paquetes de manera dinámica, sin necesidad de reiniciar el servicio.

## Usage
La sintaxis básica del comando `firewalld` es la siguiente:

```bash
firewalld [opciones] [argumentos]
```

## Common Options
- `--zone`: Especifica la zona a la que se aplicarán las reglas.
- `--add-service`: Añade un servicio a la zona especificada.
- `--remove-service`: Elimina un servicio de la zona especificada.
- `--add-port`: Abre un puerto específico en la zona.
- `--remove-port`: Cierra un puerto específico en la zona.
- `--list-all`: Muestra todas las configuraciones de la zona actual.

## Common Examples
A continuación se presentan algunos ejemplos prácticos del uso de `firewalld`:

1. **Listar todas las zonas disponibles:**
   ```bash
   firewall-cmd --get-zones
   ```

2. **Añadir el servicio HTTP a la zona pública:**
   ```bash
   firewall-cmd --zone=public --add-service=http
   ```

3. **Eliminar el servicio SSH de la zona pública:**
   ```bash
   firewall-cmd --zone=public --remove-service=ssh
   ```

4. **Abrir el puerto 8080 en la zona de trabajo:**
   ```bash
   firewall-cmd --zone=work --add-port=8080/tcp
   ```

5. **Listar todas las configuraciones de la zona actual:**
   ```bash
   firewall-cmd --list-all
   ```

## Tips
- Siempre verifica la configuración actual de tu cortafuegos antes de hacer cambios significativos.
- Utiliza `--permanent` para hacer cambios que persistan después de reiniciar el servicio.
- Recuerda recargar la configuración con `firewall-cmd --reload` después de realizar cambios permanentes.
- Consulta la documentación oficial de `firewalld` para obtener información más detallada sobre opciones avanzadas y configuraciones específicas.