# [리눅스] Bash g++ 사용법

## Overview
O `g++` é um compilador de C++ que faz parte do projeto GNU Compiler Collection (GCC). Ele é utilizado para compilar programas escritos na linguagem C++, convertendo o código fonte em um executável. O `g++` suporta uma ampla gama de padrões da linguagem C++ e oferece diversas opções para otimização e depuração.

## Usage
A sintaxe básica do comando `g++` é a seguinte:

```bash
g++ [opções] [arquivos de código fonte] -o [nome do executável]
```

### Opções Comuns:
- `-o [nome do executável]`: Especifica o nome do arquivo executável que será gerado. Se não for fornecido, o executável padrão será chamado `a.out`.
- `-Wall`: Ativa todos os avisos recomendados, ajudando a identificar potenciais problemas no código.
- `-g`: Inclui informações de depuração no executável, útil para depuração com ferramentas como `gdb`.
- `-O`: Ativa otimizações no código. Por exemplo, `-O2` é um nível de otimização comum que melhora o desempenho sem aumentar muito o tempo de compilação.

## Examples
### Exemplo 1: Compilando um arquivo simples
Suponha que você tenha um arquivo chamado `programa.cpp`. Para compilar este arquivo e gerar um executável chamado `programa`, você pode usar o seguinte comando:

```bash
g++ programa.cpp -o programa
```

### Exemplo 2: Compilando com avisos e depuração
Se você deseja compilar o mesmo arquivo, mas quer que o compilador mostre avisos e inclua informações de depuração, você pode usar:

```bash
g++ -Wall -g programa.cpp -o programa
```

## Tips
- Sempre utilize a opção `-Wall` para garantir que você esteja ciente de possíveis problemas no seu código.
- Considere usar a opção `-O2` ou `-O3` para otimizar o desempenho do seu programa em produção.
- Mantenha seu código organizado e modular, dividindo-o em múltiplos arquivos de código fonte e compilando-os juntos, se necessário.
- Utilize ferramentas de depuração como `gdb` junto com a opção `-g` para facilitar o processo de identificação de erros durante a execução do seu programa.