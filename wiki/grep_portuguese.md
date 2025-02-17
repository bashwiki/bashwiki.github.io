# [Linux] Bash grep Uso: Busca texto em arquivos

## Overview
O comando `grep` é uma ferramenta poderosa utilizada para buscar padrões de texto dentro de arquivos. Ele é amplamente utilizado em sistemas Unix e Linux para filtrar linhas que contêm uma determinada sequência de caracteres.

## Usage
A sintaxe básica do comando `grep` é a seguinte:

```bash
grep [opções] [padrão] [arquivos]
```

## Common Options
Aqui estão algumas opções comuns do `grep`:

- `-i`: Ignora a distinção entre maiúsculas e minúsculas.
- `-v`: Inverte a busca, retornando linhas que **não** contêm o padrão.
- `-r` ou `-R`: Busca recursivamente em diretórios.
- `-n`: Exibe o número da linha onde o padrão foi encontrado.
- `-l`: Lista apenas os nomes dos arquivos que contêm o padrão.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `grep`:

1. **Buscar uma palavra em um arquivo:**

```bash
grep "palavra" arquivo.txt
```

2. **Buscar ignorando maiúsculas e minúsculas:**

```bash
grep -i "palavra" arquivo.txt
```

3. **Buscar recursivamente em um diretório:**

```bash
grep -r "palavra" /caminho/do/diretorio
```

4. **Buscar e mostrar o número da linha:**

```bash
grep -n "palavra" arquivo.txt
```

5. **Listar arquivos que contêm um padrão:**

```bash
grep -l "palavra" *.txt
```

## Tips
- Utilize aspas ao redor do padrão de busca se ele contiver espaços ou caracteres especiais.
- Combine `grep` com outros comandos usando pipes (`|`) para filtrar saídas, como em `dmesg | grep "erro"`.
- Para buscas mais complexas, considere usar expressões regulares, que permitem padrões mais sofisticados.