# [리눅스] Bash du 사용법

## Overview
O comando `du` (Disk Usage) é uma ferramenta do sistema operacional Linux que permite aos usuários estimar e relatar o uso de espaço em disco de arquivos e diretórios. O principal objetivo do `du` é fornecer informações sobre a quantidade de espaço em disco que cada arquivo ou diretório ocupa, ajudando os engenheiros e desenvolvedores a gerenciar melhor o armazenamento e a identificar arquivos ou diretórios que consomem muito espaço.

## Usage
A sintaxe básica do comando `du` é a seguinte:

```bash
du [opções] [caminho]
```

### Opções Comuns:
- `-h`: Exibe os tamanhos em um formato legível para humanos (por exemplo, KB, MB, GB).
- `-s`: Mostra apenas o total para cada argumento, sem listar os subdiretórios.
- `-a`: Inclui arquivos além de diretórios na saída.
- `-c`: Exibe um total cumulativo no final da saída.
- `-d N`: Limita a profundidade da listagem a N níveis de diretórios.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `du`:

1. Para exibir o uso de disco de um diretório específico de forma legível:

```bash
du -h /caminho/para/diretorio
```

Este comando mostrará o espaço em disco usado por todos os subdiretórios e arquivos dentro do diretório especificado, utilizando unidades compreensíveis como KB, MB e GB.

2. Para obter apenas o total de espaço usado por um diretório, sem listar os subdiretórios:

```bash
du -sh /caminho/para/diretorio
```

Este comando retornará apenas o total de espaço ocupado pelo diretório, facilitando a visualização do uso de disco.

## Tips
- Utilize a opção `-h` sempre que possível para facilitar a leitura dos resultados, especialmente em diretórios grandes.
- Combine as opções `-s` e `-c` para obter um resumo do uso de disco de múltiplos diretórios de forma rápida e eficiente.
- Ao trabalhar com diretórios muito grandes, considere usar `du -h --max-depth=1` para limitar a profundidade da listagem e obter uma visão geral sem sobrecarregar a saída.
- Lembre-se de que o `du` calcula o espaço em disco usado, que pode ser diferente do tamanho do arquivo devido à fragmentação e à alocação de blocos no sistema de arquivos.

Com essas informações, você poderá utilizar o comando `du` de forma eficaz para monitorar e gerenciar o uso de espaço em disco em seu sistema.