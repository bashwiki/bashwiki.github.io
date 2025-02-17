# [Linux] Bash yum uso: Gestor de paquetes para instalar, actualizar y eliminar software

## Overview
El comando `yum` (Yellowdog Updater Modified) es un gestor de paquetes utilizado en sistemas basados en RPM, como CentOS y Fedora. Permite a los usuarios instalar, actualizar y eliminar software de manera sencilla, gestionando automáticamente las dependencias necesarias.

## Usage
La sintaxis básica del comando `yum` es la siguiente:

```bash
yum [opciones] [argumentos]
```

## Common Options
- `install`: Instala un paquete específico.
- `remove`: Elimina un paquete instalado.
- `update`: Actualiza todos los paquetes instalados a la última versión disponible.
- `search`: Busca un paquete en los repositorios.
- `info`: Muestra información detallada sobre un paquete específico.
- `list`: Lista todos los paquetes disponibles o instalados.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `yum`:

- **Instalar un paquete**:
  ```bash
  yum install nombre_del_paquete
  ```

- **Eliminar un paquete**:
  ```bash
  yum remove nombre_del_paquete
  ```

- **Actualizar todos los paquetes**:
  ```bash
  yum update
  ```

- **Buscar un paquete**:
  ```bash
  yum search nombre_del_paquete
  ```

- **Mostrar información sobre un paquete**:
  ```bash
  yum info nombre_del_paquete
  ```

- **Listar todos los paquetes instalados**:
  ```bash
  yum list installed
  ```

## Tips
- Siempre es recomendable ejecutar `yum update` regularmente para mantener el sistema seguro y actualizado.
- Utiliza `yum clean all` para limpiar la caché de yum y liberar espacio en disco.
- Revisa las dependencias de los paquetes antes de realizar instalaciones o eliminaciones para evitar problemas en el sistema.