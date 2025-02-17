# [Linux] Bash jq Uso: Procesar y filtrar datos JSON

## Overview
El comando `jq` es una herramienta de línea de comandos para procesar y manipular datos en formato JSON. Permite filtrar, transformar y extraer información de archivos JSON de manera sencilla y eficiente.

## Usage
La sintaxis básica del comando `jq` es la siguiente:

```bash
jq [opciones] [argumentos]
```

## Common Options
- `-c`: Salida compacta, sin espacios en blanco adicionales.
- `-r`: Salida sin comillas, útil para obtener resultados en texto plano.
- `-f <archivo>`: Cargar filtros desde un archivo.
- `--arg <nombre> <valor>`: Pasar un argumento como variable.

## Common Examples

### Filtrar un campo específico
Para extraer un campo específico de un archivo JSON, puedes usar el siguiente comando:

```bash
jq '.nombre' archivo.json
```

### Filtrar múltiples campos
Si deseas extraer varios campos, puedes hacerlo así:

```bash
jq '{nombre: .nombre, edad: .edad}' archivo.json
```

### Usar un argumento
Para pasar un argumento a `jq`, puedes utilizar la opción `--arg`:

```bash
jq --arg nombre "Juan" '.[] | select(.nombre == $nombre)' archivo.json
```

### Salida en formato plano
Para obtener la salida en formato plano, sin comillas:

```bash
jq -r '.nombre' archivo.json
```

### Transformar datos
Puedes transformar la estructura de un JSON con `jq`:

```bash
jq '{nuevoNombre: .nombre, nuevaEdad: .edad}' archivo.json
```

## Tips
- Siempre verifica la estructura de tu JSON antes de aplicar filtros, esto te ayudará a evitar errores.
- Usa la opción `-c` para obtener una salida más compacta, especialmente útil al trabajar con grandes volúmenes de datos.
- Combina `jq` con otros comandos de Unix para crear potentes tuberías de procesamiento de datos.