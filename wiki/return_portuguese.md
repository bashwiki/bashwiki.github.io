# [Linux] Bash return uso equivalente: Retornar o status de um comando

## Overview
O comando `return` no Bash é utilizado para encerrar uma função e retornar um código de status para o chamador. Esse código pode ser usado para indicar se a função foi executada com sucesso ou se ocorreu algum erro.

## Usage
A sintaxe básica do comando `return` é a seguinte:

```bash
return [número]
```

Onde `número` é o código de status que você deseja retornar. Se não for especificado, o retorno será o código de status da última execução.

## Common Options
O comando `return` não possui opções específicas, mas você pode usar os seguintes códigos de status comuns:
- `0`: Indica sucesso.
- `1`: Indica um erro genérico.
- Outros números podem ser usados para indicar diferentes tipos de erros ou estados.

## Common Examples

### Exemplo 1: Retornar sucesso
```bash
minha_funcao() {
    echo "Executando a função"
    return 0
}
minha_funcao
```

### Exemplo 2: Retornar erro
```bash
minha_funcao() {
    echo "Ocorreu um erro"
    return 1
}
minha_funcao
```

### Exemplo 3: Retornar o status da última execução
```bash
minha_funcao() {
    ls /diretorio_inexistente
    return $?  # Retorna o status da última execução do comando ls
}
minha_funcao
```

## Tips
- Sempre use códigos de status significativos para facilitar a depuração.
- Utilize `return` dentro de funções para controlar o fluxo do seu script.
- Lembre-se de que o `return` só pode ser usado dentro de funções e não em scripts de nível superior.