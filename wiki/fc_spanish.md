# [리눅스] Bash fc 사용법

## Overview
El comando `fc` en Bash se utiliza para listar, editar y reejecutar comandos que se han ejecutado previamente en la sesión actual del shell. Su principal propósito es facilitar la corrección de errores y la reutilización de comandos sin tener que volver a escribirlos manualmente. Esto es especialmente útil para desarrolladores e ingenieros que trabajan con múltiples comandos y necesitan realizar ajustes rápidamente.

## Usage
La sintaxis básica del comando `fc` es la siguiente:

```bash
fc [opciones] [número de comandos]
```

### Opciones comunes:
- `-l`: Lista los comandos en el historial. Puedes especificar un rango de comandos usando `n..m` (por ejemplo, `fc -l 10..20`).
- `-r`: Reejecuta los comandos listados en orden inverso.
- `-s`: Ejecuta el último comando de la lista sin abrir un editor.
- `-e`: Especifica un editor diferente al predeterminado para editar el comando.

## Examples
### Ejemplo 1: Listar comandos en el historial
Para listar los últimos 5 comandos ejecutados, puedes usar:

```bash
fc -l -5
```

Esto mostrará los últimos 5 comandos en tu historial.

### Ejemplo 2: Editar el último comando
Si deseas editar el último comando que ejecutaste, simplemente puedes usar:

```bash
fc
```

Esto abrirá el último comando en el editor de texto predeterminado, permitiéndote realizar cambios antes de ejecutarlo nuevamente.

## Tips
- Utiliza `fc -l` para revisar rápidamente los comandos que has ejecutado, lo que puede ayudarte a recordar y reutilizar comandos útiles.
- Si necesitas realizar ajustes en un comando largo, `fc` te permite hacerlo sin tener que volver a escribirlo completamente.
- Familiarízate con el editor de texto que utilizas con `fc`, ya que esto puede mejorar tu eficiencia al editar comandos. Puedes cambiar el editor predeterminado configurando la variable de entorno `EDITOR`.