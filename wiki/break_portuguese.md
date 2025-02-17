# [Linux] Bash break uso: Interrompe loops em scripts

## Overview
O comando `break` é utilizado em scripts Bash para interromper a execução de loops, como `for`, `while` e `until`. Quando o `break` é chamado, ele encerra o loop mais interno em que está inserido, permitindo que o script continue a execução após o loop.

## Usage
A sintaxe básica do comando `break` é a seguinte:

```bash
break [n]
```

Onde `n` é um número opcional que especifica quantos níveis de loops devem ser interrompidos. Se não for especificado, o `break` interrompe apenas o loop mais interno.

## Common Options
- `n`: Um número que indica quantos níveis de loops devem ser interrompidos. Por exemplo, `break 2` interrompe dois níveis de loops.

## Common Examples

### Exemplo 1: Interrompendo um loop `for`
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        break
    fi
    echo "Número: $i"
done
```
Saída:
```
Número: 1
Número: 2
```

### Exemplo 2: Interrompendo um loop `while`
```bash
count=1
while [ $count -le 5 ]; do
    if [ $count -eq 4 ]; then
        break
    fi
    echo "Contagem: $count"
    ((count++))
done
```
Saída:
```
Contagem: 1
Contagem: 2
Contagem: 3
```

### Exemplo 3: Interrompendo múltiplos níveis de loops
```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $i -eq 2 ] && [ $j -eq 2 ]; then
            break 2
        fi
        echo "i: $i, j: $j"
    done
done
```
Saída:
```
i: 1, j: 1
i: 1, j: 2
i: 1, j: 3
i: 2, j: 1
```

## Tips
- Utilize `break` quando precisar sair de um loop baseado em uma condição específica para evitar iterações desnecessárias.
- Combine `break` com `if` para criar condições de saída mais complexas em seus loops.
- Lembre-se de que `break` só afeta o loop mais interno, então, se você estiver em múltiplos níveis de loops, use o número apropriado para interromper os níveis desejados.