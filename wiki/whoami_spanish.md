# [Linux] Bash whoami Uso equivalente: Muestra el nombre del usuario actual

## Overview
El comando `whoami` en Bash se utiliza para mostrar el nombre de usuario del usuario actualmente conectado en la sesión de terminal. Es una herramienta sencilla pero útil para verificar con qué cuenta de usuario se está trabajando.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
whoami [opciones]
```

## Common Options
El comando `whoami` tiene pocas opciones, pero aquí están las más comunes:

- `--help`: Muestra la ayuda del comando y una breve descripción de su uso.
- `--version`: Muestra la versión del comando `whoami`.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso del comando `whoami`:

1. **Mostrar el nombre de usuario actual:**
   ```bash
   whoami
   ```

2. **Mostrar la ayuda del comando:**
   ```bash
   whoami --help
   ```

3. **Mostrar la versión del comando:**
   ```bash
   whoami --version
   ```

## Tips
- Utiliza `whoami` cuando necesites confirmar rápidamente el usuario con el que estás trabajando, especialmente si estás en un entorno compartido.
- Puedes combinar `whoami` con otros comandos en scripts para realizar acciones basadas en el usuario actual.
- Recuerda que `whoami` siempre mostrará el nombre de usuario, independientemente de si tienes permisos de superusuario o no.