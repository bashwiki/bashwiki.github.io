# [Linux] Bash getopts Uso: Manipulação de opções em scripts

## Overview
O comando `getopts` é utilizado em scripts Bash para analisar opções e argumentos passados na linha de comando. Ele permite que os desenvolvedores criem scripts mais interativos e flexíveis, facilitando a configuração de parâmetros de entrada.

## Usage
A sintaxe básica do comando `getopts` é a seguinte:

```bash
getopts [options] [arguments]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com `getopts`:

- `-a`: Ativa a opção para adicionar um argumento.
- `-b`: Permite a opção de exibir um argumento.
- `-c`: Usada para definir um argumento como obrigatório.
- `-h`: Exibe a ajuda sobre o uso do script.

## Common Examples

### Exemplo 1: Analisando opções simples
Neste exemplo, o script aceita duas opções: `-a` e `-b`.

```bash
#!/bin/bash

while getopts "ab" option; do
  case $option in
    a) echo "Opção A ativada" ;;
    b) echo "Opção B ativada" ;;
    *) echo "Opção inválida" ;;
  esac
done
```

### Exemplo 2: Analisando opções com argumentos
Aqui, o script aceita uma opção `-f` que requer um argumento.

```bash
#!/bin/bash

while getopts "f:" option; do
  case $option in
    f) echo "Arquivo fornecido: $OPTARG" ;;
    *) echo "Opção inválida" ;;
  esac
done
```

### Exemplo 3: Usando múltiplas opções
Neste exemplo, o script aceita várias opções e argumentos.

```bash
#!/bin/bash

while getopts "a:b:c:" option; do
  case $option in
    a) echo "Opção A: $OPTARG" ;;
    b) echo "Opção B: $OPTARG" ;;
    c) echo "Opção C: $OPTARG" ;;
    *) echo "Opção inválida" ;;
  esac
done
```

## Tips
- Sempre use dois pontos (`:`) após uma letra de opção que requer um argumento.
- Utilize `OPTIND` para redefinir o índice de opções se você precisar chamar `getopts` várias vezes no mesmo script.
- Considere adicionar uma opção `-h` ou `--help` para fornecer informações sobre como usar seu script.