# [리눅스] Bash break 사용법

## Visão Geral
O comando `break` é utilizado em scripts Bash para interromper a execução de loops, como `for`, `while` e `until`. Quando o comando `break` é chamado, ele encerra o loop mais interno em que está sendo executado, permitindo que o controle do script seja transferido para a próxima linha de código após o loop.

## Uso
A sintaxe básica do comando `break` é a seguinte:

```bash
break [n]
```

Onde `n` é um número opcional que indica quantos níveis de loops devem ser interrompidos. Se `n` não for especificado, o `break` interrompe apenas o loop mais interno.

### Opções Comuns
- `n`: Um número que especifica quantos loops internos devem ser interrompidos. Por exemplo, `break 2` interrompe dois níveis de loops.

## Exemplos

### Exemplo 1: Interrompendo um loop `for`
```bash
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo "Número: $i"
done
```
Neste exemplo, o loop `for` imprime números de 1 a 10, mas é interrompido quando `i` é igual a 5. A saída será:
```
Número: 1
Número: 2
Número: 3
Número: 4
```

### Exemplo 2: Interrompendo um loop `while`
```bash
count=1
while [ $count -le 10 ]; do
    if [ $count -eq 7 ]; then
        break
    fi
    echo "Contagem: $count"
    ((count++))
done
```
Neste exemplo, o loop `while` conta de 1 a 10, mas é interrompido quando `count` é igual a 7. A saída será:
```
Contagem: 1
Contagem: 2
Contagem: 3
Contagem: 4
Contagem: 5
Contagem: 6
```

## Dicas
- Utilize `break` com cautela para evitar a interrupção inesperada de loops, especialmente em loops aninhados.
- Considere usar `break` em conjunto com condições que garantam que o loop não seja interrompido prematuramente.
- Para loops aninhados, especifique o número de níveis a serem interrompidos para um controle mais preciso.

O comando `break` é uma ferramenta poderosa para controlar o fluxo de execução em scripts Bash, permitindo que você saia de loops de maneira eficiente e organizada.