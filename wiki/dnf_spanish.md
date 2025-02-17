# [Linux] Bash dnf Uso: Gestor de paquetes en sistemas basados en RPM

## Overview
El comando `dnf` (Dandified YUM) es un gestor de paquetes utilizado en sistemas operativos basados en RPM, como Fedora y CentOS. Permite instalar, actualizar y eliminar paquetes de software de manera eficiente, gestionando las dependencias automáticamente.

## Usage
La sintaxis básica del comando `dnf` es la siguiente:

```bash
dnf [opciones] [argumentos]
```

## Common Options
- `install`: Instala uno o más paquetes.
- `remove`: Elimina uno o más paquetes.
- `update`: Actualiza todos los paquetes instalados a la última versión.
- `search`: Busca paquetes que coincidan con un término específico.
- `info`: Muestra información detallada sobre un paquete.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `dnf`:

- **Instalar un paquete:**
  ```bash
  dnf install nombre-del-paquete
  ```

- **Eliminar un paquete:**
  ```bash
  dnf remove nombre-del-paquete
  ```

- **Actualizar todos los paquetes:**
  ```bash
  dnf update
  ```

- **Buscar un paquete:**
  ```bash
  dnf search nombre-del-paquete
  ```

- **Mostrar información sobre un paquete:**
  ```bash
  dnf info nombre-del-paquete
  ```

## Tips
- Siempre es recomendable ejecutar `dnf update` regularmente para mantener tu sistema seguro y actualizado.
- Utiliza `dnf search` para encontrar paquetes si no estás seguro del nombre exacto.
- Puedes usar `dnf history` para ver un registro de las transacciones realizadas con `dnf`, lo que puede ser útil para deshacer cambios si es necesario.