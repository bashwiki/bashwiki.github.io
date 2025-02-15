# [리눅스] Bash sed 사용법

## Overview
O `sed` (Stream Editor) é uma ferramenta poderosa de edição de texto em fluxo que permite manipular e transformar texto em arquivos ou na entrada padrão. Ele é amplamente utilizado para realizar substituições, inserções, exclusões e outras operações em linhas de texto, tornando-o uma escolha popular para automação de tarefas e processamento de dados em scripts.

## Usage
A sintaxe básica do comando `sed` é a seguinte:

```bash
sed [opções] 'comando' arquivo
```

### Comandos Comuns
- `s/padrão/substituição/`: Substitui a primeira ocorrência do padrão por uma substituição na linha.
- `g`: Usado com o comando `s` para substituir todas as ocorrências do padrão na linha.
- `-i`: Edita os arquivos no local, ou seja, modifica o arquivo original.
- `-n`: Suprime a saída padrão, permitindo que você controle quais linhas são exibidas.

## Examples
### Exemplo 1: Substituição Simples
Para substituir a primeira ocorrência da palavra "foo" pela palavra "bar" em um arquivo chamado `exemplo.txt`, você pode usar o seguinte comando:

```bash
sed 's/foo/bar/' exemplo.txt
```

### Exemplo 2: Substituição Global
Se você deseja substituir todas as ocorrências da palavra "foo" por "bar" no mesmo arquivo, utilize a opção `g`:

```bash
sed 's/foo/bar/g' exemplo.txt
```

### Exemplo 3: Editar no Local
Para editar o arquivo `exemplo.txt` diretamente e substituir "foo" por "bar", você pode usar a opção `-i`:

```bash
sed -i 's/foo/bar/g' exemplo.txt
```

## Tips
- Sempre faça um backup do seu arquivo antes de usar a opção `-i`, pois as alterações são irreversíveis.
- Para testar suas expressões `sed` sem modificar o arquivo, execute o comando sem a opção `-i`.
- Você pode usar expressões regulares complexas para padrões mais sofisticados, aumentando a flexibilidade do `sed`.
- Combine `sed` com outros comandos do Unix, como `grep` e `awk`, para criar pipelines poderosos de processamento de texto.