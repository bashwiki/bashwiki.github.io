# [Linux] Bash svn uso: Control de versiones de archivos

## Overview
El comando `svn` (Subversion) se utiliza para el control de versiones de archivos y directorios. Permite a los usuarios gestionar cambios en el código fuente y otros documentos, facilitando la colaboración en proyectos de desarrollo.

## Usage
La sintaxis básica del comando `svn` es la siguiente:

```bash
svn [opciones] [argumentos]
```

## Common Options
- `checkout`: Descarga una copia de trabajo de un repositorio.
- `commit`: Envía los cambios realizados en la copia de trabajo al repositorio.
- `update`: Sincroniza la copia de trabajo con los cambios del repositorio.
- `add`: Añade nuevos archivos o directorios al control de versiones.
- `delete`: Elimina archivos o directorios del control de versiones.
- `status`: Muestra el estado de los archivos en la copia de trabajo.

## Common Examples
1. **Descargar un repositorio:**
   ```bash
   svn checkout https://example.com/repo/trunk
   ```

2. **Enviar cambios al repositorio:**
   ```bash
   svn commit -m "Descripción de los cambios realizados"
   ```

3. **Actualizar la copia de trabajo:**
   ```bash
   svn update
   ```

4. **Añadir un nuevo archivo:**
   ```bash
   svn add nuevo_archivo.txt
   ```

5. **Eliminar un archivo del control de versiones:**
   ```bash
   svn delete archivo_a_eliminar.txt
   ```

6. **Ver el estado de los archivos:**
   ```bash
   svn status
   ```

## Tips
- Siempre realiza un `svn update` antes de comenzar a trabajar para asegurarte de que tienes la versión más reciente del código.
- Utiliza mensajes de commit claros y descriptivos para facilitar la comprensión de los cambios realizados.
- Considera crear ramas (`branches`) para trabajar en nuevas características sin afectar la versión principal del proyecto.