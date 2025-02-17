# [Linux] Bash tr Uso equivalente: Transforma ou substitui caracteres

## Overview
O comando `tr` (translate) é utilizado no Bash para transformar ou substituir caracteres em um fluxo de texto. Ele lê da entrada padrão e pode modificar os dados de acordo com as especificações fornecidas.

## Usage
A sintaxe básica do comando `tr` é a seguinte:

```bash
tr [opções] [argumentos]
```

## Common Options
- `-d`: Remove caracteres especificados.
- `-s`: Compacta sequências de caracteres repetidos em um único caractere.
- `-c`: Inverte o conjunto de caracteres especificados.
- `-t`: Substitui caracteres, mas não os remove.

## Common Examples

### Substituir caracteres
Para substituir todas as letras minúsculas 'a' por 'o':

```bash
echo "banana" | tr 'a' 'o'
```

### Remover caracteres
Para remover todas as vogais de uma string:

```bash
echo "Olá Mundo" | tr -d 'aeiouáéíóú'
```

### Compactar caracteres repetidos
Para compactar espaços em branco consecutivos em uma única ocorrência:

```bash
echo "Isto   é   um   teste." | tr -s ' '
```

### Inverter caracteres
Para inverter caracteres, por exemplo, transformar letras minúsculas em maiúsculas e vice-versa:

```bash
echo "Hello World" | tr '[:upper:]' '[:lower:]'
```

## Tips
- Sempre teste o comando com um pequeno conjunto de dados antes de aplicá-lo em arquivos grandes.
- Combine `tr` com outros comandos como `grep` ou `sort` para manipulações de texto mais complexas.
- Use `man tr` no terminal para acessar a documentação completa e explorar mais opções disponíveis.