# [Linux] Bash nslookup Uso: Consulta de direcciones DNS

## Overview
El comando `nslookup` se utiliza para consultar el sistema de nombres de dominio (DNS) y obtener información sobre direcciones IP y nombres de dominio. Permite a los usuarios verificar la configuración de DNS y solucionar problemas relacionados con la resolución de nombres.

## Usage
La sintaxis básica del comando `nslookup` es la siguiente:

```bash
nslookup [opciones] [argumentos]
```

## Common Options
- `-type=tipo`: Especifica el tipo de registro DNS que se desea consultar (por ejemplo, A, MX, CNAME).
- `-timeout=segundos`: Establece el tiempo de espera para recibir una respuesta.
- `-retry=número`: Define el número de intentos de consulta en caso de fallo.
- `-debug`: Muestra información detallada sobre la consulta y la respuesta.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `nslookup`:

1. **Consultar la dirección IP de un dominio:**
   ```bash
   nslookup example.com
   ```

2. **Consultar un registro específico (tipo A):**
   ```bash
   nslookup -type=A example.com
   ```

3. **Consultar un registro de correo (MX):**
   ```bash
   nslookup -type=MX example.com
   ```

4. **Usar un servidor DNS específico para la consulta:**
   ```bash
   nslookup example.com 8.8.8.8
   ```

5. **Obtener información detallada sobre la consulta:**
   ```bash
   nslookup -debug example.com
   ```

## Tips
- Asegúrate de tener una conexión a Internet activa para realizar consultas DNS.
- Utiliza el tipo de registro adecuado para obtener la información específica que necesitas.
- Si experimentas problemas con la resolución de nombres, prueba con diferentes servidores DNS, como los de Google (8.8.8.8 y 8.8.4.4).
- Recuerda que `nslookup` es útil para la solución de problemas, pero para configuraciones más avanzadas, considera usar `dig`.