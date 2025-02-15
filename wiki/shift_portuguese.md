# [리눅스] Bash shift 사용법

## Overview
O comando `shift` no Bash é utilizado para manipular os parâmetros posicionais de um script ou função. Ele desloca os parâmetros para a esquerda, permitindo que o primeiro parâmetro (ou seja, `$1`) seja removido e os demais parâmetros sejam reindexados. O principal propósito do `shift` é facilitar o processamento de listas de argumentos em scripts, permitindo que você trate os parâmetros de forma sequencial.

## Usage
A sintaxe básica do comando `shift` é a seguinte:

```bash
shift [n]
```

- `n`: Um número opcional que especifica quantos parâmetros devem ser deslocados. Se `n` não for fornecido, o padrão é 1, ou seja, apenas o primeiro parâmetro é removido.

## Examples

### Exemplo 1: Uso básico do shift
```bash
#!/bin/bash

echo "Parâmetros originais: $1 $2 $3"
shift
echo "Após shift: $1 $2 $3"
```
Se você executar este script com os parâmetros `arg1 arg2 arg3`, a saída será:
```
Parâmetros originais: arg1 arg2 arg3
Após shift: arg2 arg3 
```

### Exemplo 2: Deslocando múltiplos parâmetros
```bash
#!/bin/bash

echo "Parâmetros originais: $1 $2 $3 $4"
shift 2
echo "Após shift 2: $1 $2 $3 $4"
```
Se você executar este script com os parâmetros `arg1 arg2 arg3 arg4`, a saída será:
```
Parâmetros originais: arg1 arg2 arg3 arg4
Após shift 2: arg3 arg4 
```

## Tips
- Utilize `shift` em loops para processar todos os parâmetros de forma sequencial. Isso é especialmente útil em scripts que precisam lidar com um número variável de argumentos.
- Sempre verifique se há parâmetros disponíveis antes de usar `shift`, para evitar erros. Você pode fazer isso verificando a variável especial `$#`, que contém o número de parâmetros passados.
- Combine `shift` com outras estruturas de controle, como `while` ou `for`, para criar scripts mais robustos que lidam com entradas dinâmicas.