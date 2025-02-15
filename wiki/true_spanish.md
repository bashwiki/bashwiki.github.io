# [리눅스] Bash true 사용법

## Overview
El comando `true` en Bash es una utilidad muy simple que no realiza ninguna acción y siempre devuelve un estado de salida exitoso (código de salida 0). Su propósito principal es ser utilizado en scripts y comandos donde se requiere una operación que siempre sea exitosa, como en condiciones de bucles o como un marcador de posición en scripts.

## Usage
La sintaxis básica del comando `true` es la siguiente:

```bash
true
```

No tiene opciones o argumentos, ya que su única función es devolver un estado de salida exitoso.

## Examples
### Ejemplo 1: Uso en un bucle
Puedes utilizar `true` en un bucle infinito, donde el bucle se ejecutará indefinidamente hasta que se interrumpa manualmente:

```bash
while true; do
    echo "Este bucle se ejecuta indefinidamente. Presiona Ctrl+C para detenerlo."
done
```

### Ejemplo 2: Uso en un script como marcador de posición
Si estás escribiendo un script y deseas dejar un lugar para una futura implementación, puedes usar `true` como un marcador de posición:

```bash
#!/bin/bash

# Este es un marcador de posición para una futura implementación
if true; then
    echo "Esta condición siempre se cumple."
fi
```

## Tips
- Utiliza `true` cuando necesites un comando que siempre devuelva un estado de éxito en scripts, especialmente en condiciones donde no se requiere ninguna acción.
- Es útil en pruebas y depuración, donde puedes querer simular un comportamiento exitoso sin realizar ninguna operación real.
- Recuerda que `true` no produce salida, por lo que si necesitas ver algún resultado, considera usar `echo` junto con `true` en tus scripts.