# [Linux] Bash shift Uso equivalente: Mover parâmetros para a esquerda

O comando `shift` é utilizado em scripts Bash para deslocar os parâmetros posicionais para a esquerda, permitindo o acesso a argumentos subsequentes de forma mais fácil.

## Overview
O comando `shift` remove o primeiro parâmetro da lista de parâmetros posicionais e desloca todos os outros para a esquerda. Isso significa que o parâmetro `$2` se torna `$1`, o `$3` se torna `$2`, e assim por diante. É especialmente útil em loops ou quando você precisa processar uma lista de argumentos.

## Usage
A sintaxe básica do comando `shift` é a seguinte:

```bash
shift [n]
```

Onde `n` é o número de posições a serem deslocadas. Se `n` não for especificado, o padrão é 1.

## Common Options
- `n`: Número de posições a serem deslocadas. Por exemplo, `shift 2` desloca os parâmetros em duas posições.
  
## Common Examples

### Exemplo 1: Deslocar um parâmetro
```bash
#!/bin/bash
echo "Primeiro parâmetro: $1"
shift
echo "Após shift, primeiro parâmetro: $1"
```
Saída:
```
Primeiro parâmetro: um
Após shift, primeiro parâmetro: dois
```

### Exemplo 2: Deslocar múltiplos parâmetros
```bash
#!/bin/bash
echo "Parâmetros iniciais: $1 $2 $3"
shift 2
echo "Após shift 2, parâmetros: $1 $2"
```
Saída:
```
Parâmetros iniciais: um dois três
Após shift 2, parâmetros: três
```

### Exemplo 3: Usando shift em um loop
```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Processando: $1"
    shift
done
```
Saída (supondo que os parâmetros sejam "um", "dois", "três"):
```
Processando: um
Processando: dois
Processando: três
```

## Tips
- Use `shift` em loops para processar todos os argumentos de forma sequencial.
- Combine `shift` com outras estruturas de controle, como `if` ou `case`, para criar scripts mais dinâmicos.
- Sempre verifique o número de parâmetros restantes com `$#` antes de usar `shift`, para evitar erros.