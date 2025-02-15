# [리눅스] Bash local 사용법

## Overview
O comando `local` é utilizado em scripts de shell Bash para declarar variáveis que têm um escopo local dentro de uma função. Isso significa que as variáveis criadas com `local` só estão disponíveis dentro da função onde foram definidas e não afetam ou são acessíveis fora dela. O uso de variáveis locais ajuda a evitar conflitos de nomes e a manter o ambiente de execução limpo.

## Usage
A sintaxe básica do comando `local` é a seguinte:

```bash
local VARIAVEL=valor
```

Onde `VARIAVEL` é o nome da variável que você deseja criar e `valor` é o valor que você deseja atribuir a essa variável. Você pode também declarar múltiplas variáveis locais em uma única linha, separando-as por espaços.

### Opções Comuns
O comando `local` não possui opções adicionais, pois sua principal função é simplesmente definir variáveis locais.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `local` em um script Bash.

### Exemplo 1: Definindo uma variável local
```bash
#!/bin/bash

minha_funcao() {
    local mensagem="Olá, mundo!"
    echo $mensagem
}

minha_funcao
# Saída: Olá, mundo!
echo $mensagem
# Saída: (sem saída, pois 'mensagem' é local à função)
```

### Exemplo 2: Múltiplas variáveis locais
```bash
#!/bin/bash

outra_funcao() {
    local a=10
    local b=20
    local soma=$((a + b))
    echo "A soma é: $soma"
}

outra_funcao
# Saída: A soma é: 30
```

## Tips
- Sempre que possível, use `local` para declarar variáveis dentro de funções. Isso ajuda a evitar conflitos com variáveis globais e torna o código mais modular e fácil de entender.
- Lembre-se de que as variáveis locais são destruídas assim que a função termina sua execução, portanto, não tente acessá-las fora do escopo da função.
- Utilize nomes de variáveis descritivos para facilitar a leitura e a manutenção do código, mesmo em um escopo local.