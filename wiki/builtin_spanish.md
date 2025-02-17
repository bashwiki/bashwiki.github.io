# [Linux] Bash builtin : Comando para ejecutar funciones internas

## Overview
El comando `builtin` en Bash se utiliza para ejecutar comandos internos de la shell, permitiendo que se ejecuten incluso si hay un comando externo con el mismo nombre. Esto es útil para asegurarse de que se está utilizando la versión interna del comando.

## Usage
La sintaxis básica del comando `builtin` es la siguiente:

```bash
builtin [opciones] [argumentos]
```

## Common Options
A continuación se presentan algunas opciones comunes para el comando `builtin`:

- `-p`: Muestra la versión interna del comando sin ejecutar.
- `-f`: Evita que se sobrescriba la función interna si hay un comando externo con el mismo nombre.

## Common Examples

### Ejemplo 1: Ejecutar el comando `echo` interno
```bash
builtin echo "Este es un comando interno"
```

### Ejemplo 2: Usar `builtin` para evitar un alias
Si tienes un alias para `cd`, puedes usar `builtin` para acceder al comando interno:
```bash
alias cd='cd /home/user'
builtin cd /var
```

### Ejemplo 3: Verificar la versión interna de `type`
```bash
builtin type -a echo
```

## Tips
- Utiliza `builtin` cuando necesites asegurarte de que estás utilizando la versión interna de un comando, especialmente si has definido alias o funciones que pueden interferir.
- Recuerda que no todos los comandos tienen una versión interna; verifica si el comando que deseas usar es un builtin.
- Usa `help` seguido del nombre del comando para obtener más información sobre los builtins disponibles en tu shell.