# [리눅스] Bash mkdir 사용법

## Overview
O comando `mkdir` (make directory) é utilizado no Bash para criar novos diretórios no sistema de arquivos. Ele é uma ferramenta essencial para engenheiros e desenvolvedores que precisam organizar seus projetos e arquivos de maneira estruturada. Com o `mkdir`, você pode criar diretórios simples ou hierarquias de diretórios, facilitando a gestão de arquivos.

## Usage
A sintaxe básica do comando `mkdir` é a seguinte:

```bash
mkdir [opções] nome_do_diretorio
```

### Comum opções:
- `-p`: Cria diretórios pai conforme necessário. Se os diretórios intermediários não existirem, eles serão criados.
- `-v`: Modo verbose. Mostra uma mensagem para cada diretório que é criado.
- `-m`: Define as permissões do diretório criado, especificando um modo octal.

## Examples
### Exemplo 1: Criar um único diretório
Para criar um diretório chamado "projeto":

```bash
mkdir projeto
```

### Exemplo 2: Criar uma estrutura de diretórios
Para criar uma estrutura de diretórios chamada "projeto/src" e "projeto/bin", você pode usar a opção `-p`:

```bash
mkdir -p projeto/src projeto/bin
```

## Tips
- Sempre verifique se o diretório que você está tentando criar já existe para evitar mensagens de erro. Você pode usar o comando `ls` para listar os diretórios existentes.
- Utilize a opção `-v` para confirmar que os diretórios foram criados corretamente, especialmente ao criar múltiplos diretórios de uma só vez.
- Ao definir permissões com `-m`, esteja ciente das implicações de segurança e do acesso que você está concedendo aos diretórios criados.