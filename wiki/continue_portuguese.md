# [Linux] Bash continue uso equivalente: Continuar a execução de um loop

## Overview
O comando `continue` é utilizado dentro de estruturas de repetição em Bash, como `for`, `while` ou `until`. Ele serve para pular a iteração atual do loop e continuar com a próxima iteração, permitindo que você controle o fluxo de execução de maneira mais eficiente.

## Usage
A sintaxe básica do comando `continue` é a seguinte:

```bash
continue [n]
```

Aqui, `n` é um número opcional que indica quantas iterações do loop devem ser puladas. Se `n` não for especificado, o padrão é `1`.

## Common Options
- `n`: Um número que indica quantas iterações do loop devem ser puladas. Se não for fornecido, o valor padrão é `1`.

## Common Examples

### Exemplo 1: Usando continue em um loop for
Neste exemplo, o comando `continue` é usado para pular números ímpares em um loop que imprime números de 1 a 10.

```bash
for i in {1..10}; do
    if (( i % 2 != 0 )); then
        continue
    fi
    echo $i
done
```

### Exemplo 2: Usando continue em um loop while
Aqui, o comando `continue` é utilizado para pular a iteração quando a variável `count` é igual a 5.

```bash
count=0
while [ $count -lt 10 ]; do
    count=$((count + 1))
    if [ $count -eq 5 ]; then
        continue
    fi
    echo $count
done
```

### Exemplo 3: Usando continue com um número específico
Neste exemplo, o comando `continue` é usado para pular duas iterações quando o número atual é 3.

```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue 2
    fi
    echo $i
done
```

## Tips
- Use `continue` para evitar a execução de código desnecessário dentro de loops, tornando seu script mais eficiente.
- Lembre-se de que o `continue` só afeta a iteração atual do loop em que está inserido.
- Utilize comentários no seu código para explicar o uso do `continue`, especialmente se a lógica for complexa, para facilitar a manutenção futura.