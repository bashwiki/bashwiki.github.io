# [Linux] Bash rsync Uso: Sincronizar archivos y directorios

## Overview
El comando `rsync` se utiliza para sincronizar archivos y directorios entre dos ubicaciones, ya sea en la misma máquina o en diferentes sistemas a través de una red. Es especialmente útil para realizar copias de seguridad y transferencias eficientes, ya que solo copia los archivos que han cambiado.

## Usage
La sintaxis básica del comando `rsync` es la siguiente:

```bash
rsync [opciones] [origen] [destino]
```

## Common Options
- `-a`: Modo archivo; preserva permisos, tiempos de modificación, y enlaces simbólicos.
- `-v`: Modo verbose; muestra información detallada sobre el proceso de sincronización.
- `-z`: Comprime los datos durante la transferencia para ahorrar ancho de banda.
- `-r`: Sincroniza recursivamente los directorios.
- `--delete`: Elimina archivos en el destino que no están en el origen.

## Common Examples
1. Sincronizar un directorio local a otro directorio local:
   ```bash
   rsync -av /ruta/origen/ /ruta/destino/
   ```

2. Sincronizar un directorio local a un servidor remoto:
   ```bash
   rsync -av /ruta/origen/ usuario@servidor:/ruta/destino/
   ```

3. Sincronizar un directorio remoto a un directorio local:
   ```bash
   rsync -av usuario@servidor:/ruta/origen/ /ruta/destino/
   ```

4. Sincronizar y eliminar archivos en el destino que no están en el origen:
   ```bash
   rsync -av --delete /ruta/origen/ /ruta/destino/
   ```

## Tips
- Siempre es recomendable usar la opción `-n` (dry run) para simular la operación antes de realizar cambios reales:
  ```bash
  rsync -avn /ruta/origen/ /ruta/destino/
  ```
- Asegúrate de incluir una barra al final de las rutas de origen y destino para evitar confusiones sobre qué se está sincronizando.
- Utiliza la opción `-z` al transferir archivos grandes a través de conexiones lentas para mejorar la velocidad de transferencia.