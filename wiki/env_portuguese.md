# [리눅스] Bash env 사용법

## Overview
O comando `env` é uma ferramenta do Bash que permite visualizar e modificar as variáveis de ambiente do sistema. Ele é frequentemente utilizado para executar um comando em um ambiente modificado, ou simplesmente para listar as variáveis de ambiente atuais. O principal propósito do `env` é facilitar a manipulação do ambiente de execução de programas e scripts.

## Usage
A sintaxe básica do comando `env` é a seguinte:

```bash
env [OPÇÕES] [VARIÁVEIS] [COMANDO]
```

### Opções Comuns:
- `-i`: Inicia um ambiente limpo, sem variáveis de ambiente existentes.
- `-0`: Se usado com a opção `-0`, separa a saída com um caractere nulo em vez de uma nova linha. Isso é útil para manipulação de dados em scripts.

## Examples
### Exemplo 1: Listar variáveis de ambiente
Para listar todas as variáveis de ambiente atuais, você pode simplesmente usar o comando:

```bash
env
```

Este comando exibirá uma lista de todas as variáveis de ambiente e seus valores.

### Exemplo 2: Executar um comando com variáveis de ambiente modificadas
Se você deseja executar um comando com uma variável de ambiente específica, você pode fazer da seguinte forma:

```bash
env VARIAVEL_EXEMPLO=valor_comando comando_a_ser_executado
```

Por exemplo, se você quiser executar o comando `printenv` com uma variável de ambiente chamada `TESTE` definida como `123`, você faria:

```bash
env TESTE=123 printenv TESTE
```

Isso exibirá `123` como resultado.

## Tips
- Utilize `env -i` para iniciar um ambiente limpo quando você quiser evitar que variáveis de ambiente indesejadas afetem a execução do seu comando.
- O comando `env` é especialmente útil em scripts para garantir que um ambiente específico seja utilizado, evitando conflitos com variáveis de ambiente globais.
- Para depuração, você pode usar `env` para verificar quais variáveis estão definidas antes e depois da execução de um script ou comando.