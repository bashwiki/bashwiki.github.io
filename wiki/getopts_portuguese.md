# [리눅스] Bash getopts 사용법

## Overview
O `getopts` é um comando em Bash utilizado para analisar opções e argumentos passados para scripts de shell. Ele permite que os desenvolvedores criem scripts que aceitam opções de linha de comando de forma estruturada, facilitando a manipulação de argumentos e melhorando a usabilidade do script. O `getopts` é especialmente útil para scripts que precisam de opções curtas (como `-a`) e longas (como `--option`).

## Usage
A sintaxe básica do `getopts` é a seguinte:

```bash
getopts "opções" variável
```

- **opções**: Uma string que define quais opções o script aceita. Cada letra representa uma opção. Se uma opção requer um argumento, deve ser seguida de dois pontos (`:`).
- **variável**: O nome da variável onde o valor da opção atual será armazenado.

### Exemplo de opções:
- `a`: opção sem argumento.
- `b:`: opção que requer um argumento.
- `c::`: opção que pode ter um argumento opcional.

## Examples
### Exemplo 1: Script simples com `getopts`
```bash
#!/bin/bash

while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "Opção -a ativada."
      ;;
    b)
      echo "Opção -b ativada com argumento: $OPTARG"
      ;;
    c)
      echo "Opção -c ativada com argumento opcional: $OPTARG"
      ;;
    *)
      echo "Opção inválida."
      ;;
  esac
done
```
Neste exemplo, o script aceita as opções `-a`, `-b` (que requer um argumento) e `-c` (que pode ter um argumento opcional). O loop `while` continua até que todas as opções sejam processadas.

### Exemplo 2: Usando `getopts` com argumentos
```bash
#!/bin/bash

while getopts "u:p:" opt; do
  case $opt in
    u)
      echo "Usuário: $OPTARG"
      ;;
    p)
      echo "Senha: $OPTARG"
      ;;
    *)
      echo "Uso: $0 -u usuário -p senha"
      exit 1
      ;;
  esac
done
```
Neste exemplo, o script espera as opções `-u` para o nome do usuário e `-p` para a senha. As informações fornecidas são exibidas na saída.

## Tips
- Sempre forneça uma mensagem de uso clara quando uma opção inválida for fornecida, para ajudar o usuário a entender como usar o script corretamente.
- Utilize a variável especial `OPTARG` para acessar o argumento da opção atual.
- Considere usar um loop `while` para processar todas as opções, pois isso permite que o script aceite múltiplas opções em uma única execução.
- Teste seu script com diferentes combinações de opções para garantir que ele se comporte conforme o esperado.

O `getopts` é uma ferramenta poderosa para melhorar a interatividade e a funcionalidade dos scripts Bash, tornando-os mais amigáveis e robustos para os usuários.