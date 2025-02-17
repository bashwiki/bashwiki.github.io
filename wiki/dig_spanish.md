# [Linux] Bash dig Uso equivalente: consulta DNS

El comando `dig` se utiliza para realizar consultas DNS (Domain Name System) y obtener información sobre registros de dominio.

## Overview
El comando `dig` permite a los usuarios consultar servidores DNS para obtener información sobre nombres de dominio. Es una herramienta muy útil para administradores de sistemas y desarrolladores que necesitan verificar la configuración DNS de un dominio.

## Usage
La sintaxis básica del comando `dig` es la siguiente:

```
dig [opciones] [argumentos]
```

## Common Options
- `@servidor`: Especifica el servidor DNS al que se enviará la consulta.
- `-t tipo`: Define el tipo de registro que se desea consultar (por ejemplo, A, AAAA, MX, etc.).
- `+short`: Muestra una salida más concisa, útil para obtener solo la información esencial.
- `+trace`: Realiza una consulta recursiva desde el servidor raíz hasta el servidor autoritativo.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `dig`:

1. **Consulta el registro A de un dominio:**
   ```bash
   dig example.com
   ```

2. **Consulta el registro MX de un dominio:**
   ```bash
   dig -t MX example.com
   ```

3. **Consulta a un servidor DNS específico:**
   ```bash
   dig @8.8.8.8 example.com
   ```

4. **Salida concisa de la consulta:**
   ```bash
   dig +short example.com
   ```

5. **Rastrea la consulta desde el servidor raíz:**
   ```bash
   dig +trace example.com
   ```

## Tips
- Utiliza `+short` para obtener resultados más limpios y fáciles de leer, especialmente cuando solo necesitas la dirección IP.
- Si estás depurando problemas de DNS, el uso de `+trace` puede ayudarte a identificar dónde puede estar fallando la resolución.
- Recuerda que algunos servidores DNS pueden tener configuraciones específicas que afectan las respuestas; prueba con diferentes servidores si no obtienes los resultados esperados.