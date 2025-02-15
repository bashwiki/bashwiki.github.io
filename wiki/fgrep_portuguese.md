# [리눅스] Bash fgrep 사용법

## Overview
O comando `fgrep` é uma ferramenta de busca no Unix/Linux que permite procurar por strings fixas em arquivos de texto. Ao contrário do `grep`, que interpreta expressões regulares, o `fgrep` busca por padrões exatos, o que o torna mais rápido quando você precisa encontrar uma sequência específica de caracteres sem a complexidade das expressões regulares.

## Usage
A sintaxe básica do comando `fgrep` é a seguinte:

```bash
fgrep [opções] "padrão" [arquivo...]
```

### Opções Comuns:
- `-i`: Ignora a distinção entre maiúsculas e minúsculas durante a busca.
- `-v`: Inverte a busca, mostrando as linhas que **não** contêm o padrão.
- `-c`: Conta o número de linhas que contêm o padrão.
- `-n`: Mostra o número da linha junto com as linhas que contêm o padrão.
- `-r` ou `-R`: Realiza a busca recursivamente em diretórios.

## Examples
### Exemplo 1: Busca Simples
Para buscar a string "erro" em um arquivo chamado `log.txt`, você pode usar o seguinte comando:

```bash
fgrep "erro" log.txt
```

Este comando irá listar todas as linhas do arquivo `log.txt` que contêm a palavra "erro".

### Exemplo 2: Busca Ignorando Maiúsculas
Se você quiser buscar a mesma string, mas ignorando a distinção entre maiúsculas e minúsculas, use a opção `-i`:

```bash
fgrep -i "Erro" log.txt
```

Este comando irá encontrar "erro", "Erro", "ERRO", etc., no arquivo `log.txt`.

## Tips
- Utilize `fgrep` quando você tiver certeza de que não precisa de expressões regulares, pois isso pode melhorar a performance da busca.
- Combine opções para refinar sua busca. Por exemplo, usar `-n` junto com `-v` pode ser útil para identificar quais linhas não contêm um determinado padrão e ainda mostrar suas posições.
- Para buscas em múltiplos arquivos, você pode usar curingas, como `*.txt`, para buscar em todos os arquivos de texto em um diretório.

Com essas informações, você deve estar preparado para usar o `fgrep` de forma eficaz em suas tarefas de busca em arquivos de texto.