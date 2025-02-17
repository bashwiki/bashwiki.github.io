# [Linux] Bash let uso: Realiza operações aritméticas

## Overview
O comando `let` no Bash é utilizado para realizar operações aritméticas em variáveis. Ele permite que você execute cálculos simples, como adição, subtração, multiplicação e divisão, diretamente no shell.

## Usage
A sintaxe básica do comando `let` é a seguinte:

```bash
let [opções] [argumentos]
```

## Common Options
O comando `let` não possui muitas opções, mas algumas das operações aritméticas que você pode usar incluem:

- `+` : Adição
- `-` : Subtração
- `*` : Multiplicação
- `/` : Divisão
- `%` : Módulo

## Common Examples

Aqui estão alguns exemplos práticos do uso do comando `let`:

### Exemplo 1: Adição
```bash
let "resultado = 5 + 3"
echo $resultado  # Saída: 8
```

### Exemplo 2: Subtração
```bash
let "resultado = 10 - 4"
echo $resultado  # Saída: 6
```

### Exemplo 3: Multiplicação
```bash
let "resultado = 7 * 6"
echo $resultado  # Saída: 42
```

### Exemplo 4: Divisão
```bash
let "resultado = 20 / 4"
echo $resultado  # Saída: 5
```

### Exemplo 5: Módulo
```bash
let "resultado = 10 % 3"
echo $resultado  # Saída: 1
```

## Tips
- Sempre coloque as operações entre aspas para evitar erros de interpretação pelo shell.
- Você pode usar `let` em uma linha de comando para realizar cálculos rapidamente, sem a necessidade de definir variáveis intermediárias.
- Lembre-se de que `let` não imprime o resultado automaticamente; você precisa usar `echo` para visualizar o resultado.