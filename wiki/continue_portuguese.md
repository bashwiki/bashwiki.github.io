# [리눅스] Bash continue 사용법

## Overview
O comando `continue` no Bash é utilizado dentro de estruturas de repetição, como loops `for`, `while` e `until`. Sua principal finalidade é interromper a iteração atual do loop e passar para a próxima iteração. Isso é útil quando você deseja pular certas condições ou iterações sem sair completamente do loop.

## Usage
A sintaxe básica do comando `continue` é bastante simples:

```bash
continue [n]
```

- `n`: Um número opcional que especifica quantos níveis de loops externos devem ser ignorados. Se não for fornecido, o `continue` afetará apenas o loop mais interno.

## Examples

### Exemplo 1: Usando `continue` em um loop `for`
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "Número: $i"
done
```
Neste exemplo, quando `i` é igual a 3, o comando `continue` é acionado, fazendo com que a iteração atual seja pulada. A saída será:
```
Número: 1
Número: 2
Número: 4
Número: 5
```

### Exemplo 2: Usando `continue` em um loop `while`
```bash
count=0
while [ $count -lt 5 ]; do
    count=$((count + 1))
    if [ $count -eq 2 ]; then
        continue
    fi
    echo "Contagem: $count"
done
```
Aqui, quando `count` é igual a 2, o `continue` faz com que a contagem pule essa iteração. A saída será:
```
Contagem: 1
Contagem: 3
Contagem: 4
Contagem: 5
```

## Tips
- Utilize o `continue` quando precisar ignorar certas condições dentro de loops, tornando seu código mais limpo e legível.
- Lembre-se de que o `continue` só afeta o loop mais interno, a menos que você especifique um número para pular múltiplos níveis de loops.
- Combine `continue` com outras estruturas de controle, como `if`, para um controle mais refinado sobre a lógica do seu loop.