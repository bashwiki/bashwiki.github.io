# [Linux] Bash declare Uso: Declarar variáveis e atributos no Bash

## Overview
O comando `declare` no Bash é utilizado para declarar variáveis e definir atributos para essas variáveis. Ele permite que você especifique se uma variável é um array, uma variável somente leitura, entre outros atributos, facilitando o gerenciamento de variáveis em scripts.

## Usage
A sintaxe básica do comando `declare` é a seguinte:

```bash
declare [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `declare`:

- `-a`: Declara uma variável como um array.
- `-r`: Declara uma variável como somente leitura, impedindo que seu valor seja alterado.
- `-x`: Exporta a variável para o ambiente, tornando-a disponível para subprocessos.
- `-i`: Declara uma variável como um número inteiro, permitindo operações matemáticas.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `declare`:

1. Declarar uma variável simples:
   ```bash
   declare nome="João"
   ```

2. Declarar uma variável somente leitura:
   ```bash
   declare -r pi=3.14
   ```

3. Declarar um array:
   ```bash
   declare -a frutas=("maçã" "banana" "laranja")
   ```

4. Declarar uma variável inteira:
   ```bash
   declare -i numero=10
   ```

5. Exportar uma variável para o ambiente:
   ```bash
   declare -x usuario="admin"
   ```

## Tips
- Use `declare -p` para exibir todas as variáveis e seus atributos atuais.
- Lembre-se de que variáveis somente leitura não podem ser alteradas após a declaração, então use-as com cuidado.
- Ao trabalhar com arrays, você pode acessar elementos individuais usando a sintaxe `${array[index]}`.