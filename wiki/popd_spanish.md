# [Linux] Bash popd uso equivalente: Regresar al directorio anterior

## Overview
El comando `popd` se utiliza en Bash para cambiar al directorio que se encuentra en la parte superior de la pila de directorios. Este comando es útil para navegar entre directorios de manera eficiente, permitiendo volver rápidamente a ubicaciones anteriores.

## Usage
La sintaxis básica del comando es la siguiente:

```bash
popd [options] [arguments]
```

## Common Options
- `-n`: No elimina el directorio de la pila, solo cambia al directorio superior.
- `+n`: Cambia al directorio en la posición `n` de la pila, donde `n` es un número que representa la posición del directorio en la pila.

## Common Examples

1. **Regresar al directorio anterior**:
   ```bash
   popd
   ```

2. **Regresar al segundo directorio en la pila**:
   ```bash
   popd +1
   ```

3. **Regresar al tercer directorio en la pila**:
   ```bash
   popd +2
   ```

4. **No eliminar el directorio de la pila**:
   ```bash
   popd -n
   ```

## Tips
- Asegúrate de usar `pushd` antes de `popd` para que haya directorios en la pila.
- Puedes ver el contenido de la pila de directorios usando el comando `dirs`.
- Utiliza `popd` junto con `pushd` para crear un flujo de trabajo eficiente al navegar por múltiples directorios.