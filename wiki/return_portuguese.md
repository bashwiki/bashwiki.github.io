# [리눅스] Bash return 사용법

## Overview
O comando `return` no Bash é utilizado para sair de uma função e retornar um valor de status. O valor de status é um número inteiro que pode ser usado para indicar o sucesso ou a falha da execução de uma função. Por padrão, o `return` retorna 0, que geralmente indica sucesso, mas você pode especificar um valor diferente para indicar diferentes estados de saída.

## Usage
A sintaxe básica do comando `return` é a seguinte:

```bash
return [n]
```

Onde `n` é um número inteiro que representa o valor de status que você deseja retornar. Se `n` não for especificado, o `return` usará o valor de status da última execução de um comando dentro da função.

## Examples

### Exemplo 1: Retornando um valor de sucesso
```bash
minha_funcao() {
    echo "Executando a função..."
    return 0
}

minha_funcao
echo "Valor de retorno: $?"
```
Neste exemplo, a função `minha_funcao` é definida e chamada. O comando `return 0` indica que a função foi executada com sucesso. O valor de retorno pode ser verificado usando `$?`, que mostrará `0`.

### Exemplo 2: Retornando um valor de erro
```bash
minha_funcao() {
    echo "Ocorreu um erro!"
    return 1
}

minha_funcao
echo "Valor de retorno: $?"
```
Aqui, a função `minha_funcao` retorna `1`, indicando que ocorreu um erro. O valor de retorno também pode ser verificado com `$?`, que mostrará `1`.

## Tips
- Utilize o `return` para indicar claramente o resultado da execução de suas funções, facilitando a depuração e o controle de fluxo em scripts mais complexos.
- É uma boa prática retornar valores diferentes para diferentes tipos de erro, o que pode ajudar na identificação de problemas.
- Lembre-se de que o valor de retorno deve ser um número inteiro entre 0 e 255, pois valores fora desse intervalo podem resultar em comportamentos inesperados.