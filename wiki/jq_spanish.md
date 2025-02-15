# [리눅스] Bash jq 사용법

## Overview
`jq` es una herramienta de línea de comandos para procesar y manipular datos en formato JSON. Su propósito principal es permitir a los desarrolladores y a los ingenieros extraer, transformar y filtrar datos JSON de manera eficiente y sencilla. `jq` es especialmente útil en scripts de Bash y en la manipulación de datos en aplicaciones web y APIs.

## Usage
La sintaxis básica de `jq` es la siguiente:

```bash
jq [opciones] 'expresión' archivo.json
```

### Opciones Comunes
- `-c`: Produce salida compacta (una línea por objeto).
- `-r`: Genera salida sin comillas, útil para obtener texto plano.
- `-f archivo.jq`: Carga un archivo de filtros `jq` en lugar de pasar la expresión directamente en la línea de comandos.
- `--arg nombre valor`: Define una variable que puede ser utilizada dentro de la expresión `jq`.

## Examples
### Ejemplo 1: Extraer un campo específico
Supongamos que tenemos un archivo `data.json` con el siguiente contenido:

```json
{
  "nombre": "Juan",
  "edad": 30,
  "ciudad": "Madrid"
}
```

Para extraer el campo `nombre`, usaríamos el siguiente comando:

```bash
jq '.nombre' data.json
```

Esto devolverá:

```
"Juan"
```

### Ejemplo 2: Filtrar una lista de objetos
Si tenemos un archivo `usuarios.json` con el siguiente contenido:

```json
[
  { "nombre": "Juan", "edad": 30 },
  { "nombre": "Ana", "edad": 25 },
  { "nombre": "Luis", "edad": 35 }
]
```

Podemos filtrar los usuarios mayores de 30 años con el siguiente comando:

```bash
jq '.[] | select(.edad > 30)' usuarios.json
```

Esto devolverá:

```json
{
  "nombre": "Luis",
  "edad": 35
}
```

## Tips
- Utiliza la opción `-r` si necesitas obtener texto plano en lugar de JSON, especialmente cuando trabajas con scripts que requieren salida limpia.
- Familiarízate con la sintaxis de `jq`, ya que permite realizar operaciones complejas de filtrado y transformación de datos.
- Puedes combinar múltiples filtros en una sola expresión para realizar tareas más complejas, lo que hace que `jq` sea una herramienta poderosa para la manipulación de datos JSON.