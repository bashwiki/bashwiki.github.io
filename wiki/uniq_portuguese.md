# [리눅스] Bash uniq 사용법

## Overview
O comando `uniq` é uma ferramenta do Bash utilizada para filtrar linhas duplicadas em um arquivo ou na entrada padrão. Seu principal propósito é simplificar a visualização de dados, removendo entradas repetidas e permitindo que o usuário veja apenas linhas únicas. O `uniq` geralmente é usado em conjunto com o comando `sort`, pois ele só remove duplicatas que estão adjacentes.

## Usage
A sintaxe básica do comando `uniq` é a seguinte:

```bash
uniq [opções] [entrada] [saída]
```

### Opções Comuns:
- `-c`: Conta o número de ocorrências de cada linha e exibe esse número antes da linha.
- `-d`: Exibe apenas as linhas que aparecem mais de uma vez.
- `-u`: Exibe apenas as linhas que são únicas, ou seja, que aparecem apenas uma vez.
- `-i`: Ignora diferenças entre maiúsculas e minúsculas ao comparar linhas.

## Examples

### Exemplo 1: Remover duplicatas de um arquivo
Suponha que você tenha um arquivo chamado `dados.txt` com o seguinte conteúdo:

```
maçã
banana
banana
laranja
maçã
```

Para remover as duplicatas e exibir apenas as linhas únicas, você pode usar o seguinte comando:

```bash
sort dados.txt | uniq
```

A saída será:

```
banana
laranja
maçã
```

### Exemplo 2: Contar ocorrências de linhas
Se você quiser contar quantas vezes cada linha aparece no arquivo, pode usar a opção `-c`:

```bash
sort dados.txt | uniq -c
```

A saída será:

```
      2 banana
      1 laranja
      2 maçã
```

## Tips
- Sempre use `sort` antes de `uniq` se você estiver lidando com um arquivo que pode conter linhas duplicadas não adjacentes. Isso garante que todas as duplicatas sejam removidas.
- Combine `uniq` com outros comandos, como `grep`, para filtrar ainda mais os resultados.
- Utilize a opção `-i` se você precisar ignorar a diferenciação entre maiúsculas e minúsculas, especialmente em conjuntos de dados onde a capitalização pode variar.

Com essas informações, você deve estar apto a utilizar o comando `uniq` de forma eficaz em suas tarefas de manipulação de texto no Bash.