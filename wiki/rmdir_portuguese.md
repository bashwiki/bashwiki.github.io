# [리눅스] Bash rmdir 사용법

## Overview
O comando `rmdir` é utilizado no sistema operacional Linux para remover diretórios vazios. Sua principal finalidade é facilitar a limpeza de estruturas de diretórios, permitindo que os usuários excluam pastas que não contêm arquivos ou subdiretórios. É importante notar que o `rmdir` não pode remover diretórios que contêm arquivos ou outros diretórios, garantindo assim que não haja perda acidental de dados.

## Usage
A sintaxe básica do comando `rmdir` é a seguinte:

```bash
rmdir [opções] <diretório>
```

### Opções Comuns
- `-p` ou `--parents`: Remove o diretório especificado e, se estiver vazio, também remove os diretórios pai, se eles também estiverem vazios.
- `--ignore-fail-on-non-empty`: Ignora erros se o diretório não estiver vazio.

## Examples
### Exemplo 1: Remover um diretório vazio
Para remover um diretório chamado `meu_diretorio`, você pode usar o seguinte comando:

```bash
rmdir meu_diretorio
```

Se `meu_diretorio` estiver vazio, ele será removido com sucesso.

### Exemplo 2: Remover diretórios vazios em cadeia
Se você deseja remover um diretório e seus diretórios pai, desde que estejam vazios, você pode usar a opção `-p`:

```bash
rmdir -p meu_diretorio/pasta1/pasta2
```

Se `pasta2`, `pasta1` e `meu_diretorio` estiverem vazios, todos eles serão removidos.

## Tips
- Sempre verifique se o diretório que você está tentando remover está realmente vazio. Você pode usar o comando `ls` para listar os conteúdos do diretório antes de removê-lo.
- Utilize `rmdir` com cautela, especialmente ao usar a opção `-p`, pois isso pode remover vários diretórios de uma só vez.
- Para evitar a perda de dados, considere usar o comando `rm -r` se você precisar remover diretórios que contêm arquivos, mas esteja ciente de que isso não é reversível.