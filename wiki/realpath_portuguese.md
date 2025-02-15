# [리눅스] Bash realpath 사용법

## Overview
O comando `realpath` é utilizado para resolver caminhos de arquivos e diretórios, convertendo caminhos relativos em caminhos absolutos. Ele é especialmente útil para garantir que você esteja trabalhando com o caminho correto de um arquivo ou diretório, independentemente do diretório de trabalho atual. O `realpath` elimina referências como `.` (diretório atual) e `..` (diretório pai), resultando em um caminho limpo e absoluto.

## Usage
A sintaxe básica do comando `realpath` é a seguinte:

```bash
realpath [opções] <caminho>
```

### Opções Comuns:
- `-m`, `--canonicalize-missing`: Resolve o caminho e retorna um caminho absoluto, mesmo que o arquivo ou diretório não exista.
- `-q`, `--quiet`: Suprime mensagens de erro, retornando apenas o resultado.
- `-s`, `--strip`: Remove o caminho de prefixo, se especificado.

## Examples
### Exemplo 1: Caminho Absoluto
Para obter o caminho absoluto de um arquivo chamado `meuarquivo.txt` no diretório atual, você pode usar:

```bash
realpath meuarquivo.txt
```

Se o arquivo estiver localizado em `/home/usuario/documentos/meuarquivo.txt`, o comando retornará:

```
/home/usuario/documentos/meuarquivo.txt
```

### Exemplo 2: Caminho com Diretórios Relativos
Se você estiver em um diretório diferente e quiser resolver um caminho relativo, como `../documentos/meuarquivo.txt`, você pode usar:

```bash
realpath ../documentos/meuarquivo.txt
```

Isso retornará o caminho absoluto correspondente, por exemplo:

```
/home/usuario/documentos/meuarquivo.txt
```

## Tips
- Utilize o `realpath` em scripts para garantir que você sempre trabalhe com caminhos absolutos, evitando confusões com caminhos relativos.
- Combine o `realpath` com outros comandos, como `cd`, para mudar para o diretório de um caminho absoluto de forma segura.
- Se você estiver lidando com arquivos que podem não existir, considere usar a opção `-m` para evitar erros e ainda obter um caminho absoluto.