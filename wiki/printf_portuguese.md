# [Linux] Bash printf Uso: Formatação de saída de texto

## Overview
O comando `printf` em Bash é utilizado para formatar e exibir texto na saída padrão. Ele permite um controle preciso sobre a formatação, como a largura do campo, a precisão e a inclusão de caracteres especiais.

## Usage
A sintaxe básica do comando `printf` é a seguinte:

```bash
printf [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `printf`:

- `%s`: Formata uma string.
- `%d`: Formata um número inteiro decimal.
- `%f`: Formata um número de ponto flutuante.
- `%x`: Formata um número em hexadecimal.
- `-`: Alinha à esquerda o texto dentro do campo especificado.
- `0`: Preenche com zeros à esquerda.

## Common Examples

### Exemplo 1: Exibir uma string
```bash
printf "Olá, Mundo!\n"
```

### Exemplo 2: Formatar um número inteiro
```bash
printf "O número é: %d\n" 42
```

### Exemplo 3: Formatar um número de ponto flutuante
```bash
printf "O valor de pi é aproximadamente: %.2f\n" 3.14159
```

### Exemplo 4: Exibir múltiplos valores
```bash
printf "Nome: %s, Idade: %d\n" "Alice" 30
```

### Exemplo 5: Preenchimento com zeros
```bash
printf "Número com preenchimento: %05d\n" 7
```

## Tips
- Utilize `\n` para adicionar quebras de linha em suas saídas.
- Experimente diferentes especificadores de formato para entender melhor como eles funcionam.
- Lembre-se de que `printf` não adiciona automaticamente uma nova linha ao final da saída, ao contrário do comando `echo`.