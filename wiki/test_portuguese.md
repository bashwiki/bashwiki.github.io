# [리눅스] Bash test 사용법

## Overview
O comando `test` é uma ferramenta fundamental no Bash que permite avaliar expressões condicionais. Seu principal propósito é verificar condições, como se um arquivo existe, se é um diretório, se uma string está vazia, entre outras. O `test` retorna um código de saída que pode ser utilizado em estruturas de controle, como `if`, para determinar o fluxo de execução de um script.

## Usage
A sintaxe básica do comando `test` é a seguinte:

```bash
test EXPRESSION
```

ou, de forma equivalente, você pode usar os colchetes:

```bash
[ EXPRESSION ]
```

### Opções Comuns
- `-e FILE`: Verifica se o arquivo existe.
- `-d FILE`: Verifica se o arquivo é um diretório.
- `-f FILE`: Verifica se o arquivo é um arquivo regular.
- `-z STRING`: Verifica se a string é vazia.
- `-n STRING`: Verifica se a string não é vazia.
- `STRING1 = STRING2`: Verifica se duas strings são iguais.
- `STRING1 != STRING2`: Verifica se duas strings são diferentes.

## Examples
### Exemplo 1: Verificando a existência de um arquivo
```bash
if test -e "meuarquivo.txt"; then
    echo "O arquivo existe."
else
    echo "O arquivo não existe."
fi
```

### Exemplo 2: Verificando se uma string está vazia
```bash
string=""
if test -z "$string"; then
    echo "A string está vazia."
else
    echo "A string não está vazia."
fi
```

## Tips
- Utilize colchetes `[` e `]` para tornar o código mais legível, mas não se esqueça de incluir espaços ao redor dos colchetes.
- O `test` pode ser combinado com operadores lógicos como `-a` (E) e `-o` (OU) para avaliações mais complexas.
- Sempre verifique o código de saída do comando `test` usando `$?` para depuração e controle de fluxo em scripts. 

O comando `test` é uma ferramenta poderosa e versátil que pode ajudar a tornar seus scripts Bash mais robustos e dinâmicos.