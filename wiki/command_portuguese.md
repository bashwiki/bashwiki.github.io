# [리눅스] Bash command 사용법

## Overview
O comando `command` no Bash é utilizado para executar um comando, ignorando qualquer função ou alias que tenha o mesmo nome. Isso é útil quando você deseja garantir que está chamando o comando original do sistema, em vez de uma versão personalizada ou redefinida.

## Usage
A sintaxe básica do comando é a seguinte:

```bash
command [opções] comando [argumentos]
```

### Opções Comuns
- `-v`: Mostra a versão do comando, se disponível.
- `-p`: Ignora funções e aliases e procura o comando no caminho padrão do sistema.

## Examples
### Exemplo 1: Executar um comando ignorando funções
Se você tiver uma função chamada `ls` definida em seu ambiente, mas deseja usar o comando `ls` original, você pode fazer o seguinte:

```bash
command ls -l
```

### Exemplo 2: Usar o comando com a opção `-p`
Para garantir que você está chamando o comando `grep` do caminho padrão do sistema, você pode usar:

```bash
command -p grep "texto" arquivo.txt
```

## Tips
- Utilize o `command` quando houver conflitos entre comandos e funções ou aliases que você definiu.
- É uma boa prática verificar se um comando está sendo ofuscado por uma função ou alias, especialmente em scripts, para evitar comportamentos inesperados.
- Combine o `command` com outras ferramentas de linha de comando para garantir que você está utilizando a versão correta dos comandos em scripts complexos.