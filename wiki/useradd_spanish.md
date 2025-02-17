# [Linux] Bash useradd Uso: Crear nuevos usuarios en el sistema

## Overview
El comando `useradd` se utiliza en sistemas Linux para crear nuevos usuarios. Este comando permite agregar cuentas de usuario al sistema, configurando diversos parámetros como el directorio home, el shell predeterminado y más.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
useradd [opciones] [argumentos]
```

## Common Options
- `-m`: Crea un directorio home para el nuevo usuario.
- `-s`: Especifica el shell predeterminado para el nuevo usuario.
- `-G`: Añade el usuario a uno o más grupos adicionales.
- `-c`: Permite agregar un comentario, como el nombre completo del usuario.
- `-d`: Define el directorio home del usuario.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `useradd`:

1. **Crear un usuario básico:**
   ```bash
   useradd nuevo_usuario
   ```

2. **Crear un usuario con un directorio home:**
   ```bash
   useradd -m nuevo_usuario
   ```

3. **Crear un usuario con un shell específico:**
   ```bash
   useradd -m -s /bin/bash nuevo_usuario
   ```

4. **Crear un usuario y añadirlo a grupos adicionales:**
   ```bash
   useradd -m -G sudo,adm nuevo_usuario
   ```

5. **Crear un usuario con un comentario:**
   ```bash
   useradd -m -c "Juan Pérez" nuevo_usuario
   ```

## Tips
- Siempre verifica que el nombre de usuario que deseas crear no esté ya en uso.
- Utiliza la opción `-m` para asegurarte de que se cree un directorio home, lo cual es recomendable para la mayoría de los usuarios.
- Considera establecer una contraseña para el nuevo usuario inmediatamente después de crearlo utilizando el comando `passwd nuevo_usuario`.
- Revisa los archivos de configuración de usuarios, como `/etc/passwd`, para verificar que el nuevo usuario se haya creado correctamente.