# [리눅스] Bash rar 사용법

## Overview
O comando `rar` é uma ferramenta de linha de comando utilizada para criar e manipular arquivos no formato RAR (Roshal Archive). Este formato é conhecido por sua alta taxa de compressão e é amplamente utilizado para compactar arquivos e pastas, facilitando o armazenamento e a transferência de dados. O `rar` permite não apenas a compressão, mas também a extração de arquivos de arquivos RAR existentes.

## Usage
A sintaxe básica do comando `rar` é a seguinte:

```bash
rar [opções] [comando] [arquivo(s)]
```

### Comandos Comuns:
- `a`: Adiciona arquivos a um arquivo RAR.
- `x`: Extrai arquivos de um arquivo RAR.
- `t`: Testa a integridade de um arquivo RAR.
- `d`: Remove arquivos de um arquivo RAR.

### Opções Comuns:
- `-v`: Cria volumes do arquivo RAR, permitindo dividir o arquivo em partes menores.
- `-m`: Define o nível de compressão (0 a 5, onde 0 é sem compressão e 5 é a máxima).
- `-p`: Define uma senha para o arquivo RAR.

## Examples

### Exemplo 1: Criar um arquivo RAR
Para criar um arquivo RAR chamado `meus_arquivos.rar` a partir de uma pasta chamada `documentos`, você pode usar o seguinte comando:

```bash
rar a meus_arquivos.rar documentos/
```

### Exemplo 2: Extrair um arquivo RAR
Para extrair o conteúdo de um arquivo RAR chamado `meus_arquivos.rar`, você pode usar o seguinte comando:

```bash
rar x meus_arquivos.rar
```

## Tips
- Sempre verifique a integridade do arquivo RAR após a criação usando o comando `rar t meus_arquivos.rar` para garantir que não houve erros durante a compressão.
- Considere usar a opção `-m5` para obter a melhor taxa de compressão, especialmente se você estiver lidando com arquivos grandes.
- Se você precisar compartilhar arquivos sensíveis, utilize a opção `-p` para proteger seu arquivo RAR com uma senha.

Com essas informações, você está pronto para utilizar o comando `rar` de forma eficaz em suas tarefas de compressão e extração de arquivos.