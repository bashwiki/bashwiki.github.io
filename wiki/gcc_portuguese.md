# [리눅스] Bash gcc 사용법

## Overview
O `gcc` (GNU Compiler Collection) é um compilador de código-fonte que suporta várias linguagens de programação, sendo mais conhecido por compilar programas escritos em C e C++. O principal objetivo do `gcc` é transformar o código-fonte em um executável, permitindo que os desenvolvedores criem aplicações a partir de seus códigos.

## Usage
A sintaxe básica do comando `gcc` é a seguinte:

```bash
gcc [opções] arquivo_fonte.c -o nome_executavel
```

### Opções Comuns:
- `-o nome_executavel`: Especifica o nome do arquivo executável gerado. Se não for fornecido, o padrão será `a.out`.
- `-Wall`: Ativa todos os avisos recomendados, ajudando a identificar problemas potenciais no código.
- `-g`: Inclui informações de depuração no executável, útil para depuração com ferramentas como `gdb`.
- `-O`: Ativa otimizações no código, onde `-O1`, `-O2`, e `-O3` representam níveis crescentes de otimização.
- `-I`: Adiciona diretórios à lista de diretórios de inclusão para cabeçalhos.

## Examples
### Exemplo 1: Compilando um arquivo C simples
Para compilar um arquivo chamado `programa.c` e gerar um executável chamado `programa`, você pode usar o seguinte comando:

```bash
gcc programa.c -o programa
```

### Exemplo 2: Compilando com avisos e informações de depuração
Se você deseja compilar `programa.c` com avisos ativados e informações de depuração, use:

```bash
gcc -Wall -g programa.c -o programa
```

## Tips
- Sempre use a opção `-Wall` para garantir que você esteja ciente de possíveis problemas no seu código.
- Considere usar a opção `-g` durante o desenvolvimento para facilitar a depuração, mas remova-a em versões de produção para reduzir o tamanho do executável.
- Mantenha seu código bem organizado e utilize comentários para facilitar a manutenção e a compreensão do código.
- Utilize um sistema de controle de versão para gerenciar alterações no seu código-fonte e facilitar a colaboração com outros desenvolvedores.