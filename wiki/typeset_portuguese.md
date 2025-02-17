# [Linux] Bash typeset uso: Define variáveis e atributos

## Overview
O comando `typeset` é utilizado em scripts e no shell interativo do Bash para definir variáveis e seus atributos. Ele permite que você especifique características como se a variável é somente leitura, um array ou uma variável associativa.

## Usage
A sintaxe básica do comando `typeset` é a seguinte:

```bash
typeset [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `typeset`:

- `-r`: Define a variável como somente leitura, impedindo que seu valor seja alterado.
- `-a`: Declara a variável como um array.
- `-A`: Declara a variável como um array associativo.
- `-i`: Define a variável como um inteiro, permitindo operações aritméticas.
- `-x`: Exporta a variável para o ambiente do shell, tornando-a disponível para subprocessos.

## Common Examples

### Definindo uma variável simples
```bash
typeset nome="João"
echo $nome
```

### Definindo uma variável somente leitura
```bash
typeset -r pi=3.14
echo $pi
# pi=3.15  # Isso causará um erro, pois pi é somente leitura.
```

### Criando um array
```bash
typeset -a frutas=("maçã" "banana" "laranja")
echo ${frutas[1]}  # Saída: banana
```

### Criando um array associativo
```bash
typeset -A idade
idade["João"]=30
idade["Maria"]=25
echo ${idade["João"]}  # Saída: 30
```

### Definindo uma variável inteira
```bash
typeset -i contador=0
contador+=1
echo $contador  # Saída: 1
```

## Tips
- Use `typeset` para garantir que suas variáveis tenham o comportamento desejado, especialmente em scripts complexos.
- Lembre-se de que `typeset` é uma construção do Bash, então não funcionará em outros shells como o sh ou zsh.
- Considere usar arrays associativos para armazenar pares chave-valor, facilitando a manipulação de dados complexos.