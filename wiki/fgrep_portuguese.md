# [Linux] Bash fgrep Uso: Busca por strings fixas em arquivos

## Overview
O comando `fgrep` é utilizado para buscar por strings fixas em arquivos de texto. Ele é uma versão do comando `grep`, mas que não interpreta expressões regulares, tornando a busca mais rápida e eficiente quando se trata de encontrar padrões exatos.

## Usage
A sintaxe básica do comando `fgrep` é a seguinte:

```bash
fgrep [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `fgrep`:

- `-i`: Ignora a diferenciação entre maiúsculas e minúsculas.
- `-v`: Inverte a busca, mostrando linhas que **não** contêm a string especificada.
- `-c`: Conta o número de linhas que correspondem à busca.
- `-n`: Mostra o número da linha junto com as correspondências.
- `-r`: Busca recursivamente em diretórios.

## Common Examples

### Exemplo 1: Busca simples
Para buscar a string "exemplo" em um arquivo chamado `arquivo.txt`:

```bash
fgrep "exemplo" arquivo.txt
```

### Exemplo 2: Ignorar maiúsculas e minúsculas
Para buscar a string "ExEmPlO" ignorando a diferenciação entre maiúsculas e minúsculas:

```bash
fgrep -i "ExEmPlO" arquivo.txt
```

### Exemplo 3: Contar correspondências
Para contar quantas vezes a string "teste" aparece em um arquivo:

```bash
fgrep -c "teste" arquivo.txt
```

### Exemplo 4: Buscar recursivamente em diretórios
Para buscar a string "dados" em todos os arquivos de um diretório e suas subpastas:

```bash
fgrep -r "dados" /caminho/para/diretorio
```

### Exemplo 5: Inverter a busca
Para mostrar todas as linhas que **não** contêm a string "erro":

```bash
fgrep -v "erro" arquivo.txt
```

## Tips
- Utilize `fgrep` quando precisar de uma busca rápida e não precisar de expressões regulares.
- Combine opções para refinar suas buscas, como `-i` e `-n` para ignorar maiúsculas e mostrar números de linha.
- Para arquivos grandes, considere usar `fgrep` em vez de `grep` para melhorar o desempenho.