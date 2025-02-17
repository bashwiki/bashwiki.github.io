# [Linux] Bash expr Uso equivalente: Evaluar expresiones

## Overview
El comando `expr` se utiliza en Bash para evaluar expresiones aritméticas, lógicas y de cadenas. Permite realizar cálculos simples y manipular cadenas de texto, lo que lo convierte en una herramienta útil en scripts y en la línea de comandos.

## Usage
La sintaxis básica del comando `expr` es la siguiente:

```bash
expr [opciones] [argumentos]
```

## Common Options
- `+`: Suma dos números.
- `-`: Resta dos números.
- `*`: Multiplica dos números (se debe escapar con `\` o usar comillas).
- `/`: Divide dos números.
- `%`: Calcula el módulo de dos números.
- `=`: Compara dos cadenas.
- `:`: Utilizado para extraer subcadenas.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `expr`:

### Sumar dos números
```bash
expr 5 + 3
```
Salida:
```
8
```

### Restar dos números
```bash
expr 10 - 4
```
Salida:
```
6
```

### Multiplicar dos números
```bash
expr 4 \* 2
```
Salida:
```
8
```

### Dividir dos números
```bash
expr 10 / 2
```
Salida:
```
5
```

### Calcular el módulo
```bash
expr 10 % 3
```
Salida:
```
1
```

### Comparar cadenas
```bash
expr "hola" = "hola"
```
Salida:
```
1
```

### Extraer una subcadena
```bash
expr substr "Hola Mundo" 1 4
```
Salida:
```
Hola
```

## Tips
- Recuerda escapar el asterisco (`*`) con una barra invertida (`\`) para evitar que sea interpretado como un comodín por el shell.
- Usa comillas alrededor de las cadenas para evitar problemas con espacios.
- Aunque `expr` es útil, considera usar `$(( ... ))` para cálculos aritméticos en Bash, ya que es más moderno y fácil de leer.