# [Linux] Bash tar Uso: Comprimir e descomprimir arquivos

## Overview
O comando `tar` é utilizado para agrupar e compactar arquivos em um único arquivo, facilitando o armazenamento e a transferência. Ele é amplamente utilizado em sistemas Unix e Linux para criar arquivos de backup e distribuir conjuntos de arquivos.

## Usage
A sintaxe básica do comando `tar` é a seguinte:

```bash
tar [opções] [arquivos]
```

## Common Options
Aqui estão algumas opções comuns do comando `tar`:

- `-c`: Cria um novo arquivo tar.
- `-x`: Extrai arquivos de um arquivo tar existente.
- `-f`: Especifica o nome do arquivo tar.
- `-v`: Exibe os nomes dos arquivos durante a operação (modo verbose).
- `-z`: Compacta ou descompacta usando gzip.
- `-j`: Compacta ou descompacta usando bzip2.

## Common Examples

### Criar um arquivo tar
Para criar um arquivo tar chamado `meus_arquivos.tar` a partir de uma pasta chamada `documentos`, use:

```bash
tar -cvf meus_arquivos.tar documentos/
```

### Extrair um arquivo tar
Para extrair o conteúdo de um arquivo tar chamado `meus_arquivos.tar`, use:

```bash
tar -xvf meus_arquivos.tar
```

### Criar um arquivo tar.gz
Para criar um arquivo tar compactado com gzip, use:

```bash
tar -czvf meus_arquivos.tar.gz documentos/
```

### Extrair um arquivo tar.gz
Para extrair um arquivo tar.gz, use:

```bash
tar -xzvf meus_arquivos.tar.gz
```

### Criar um arquivo tar.bz2
Para criar um arquivo tar compactado com bzip2, use:

```bash
tar -cjvf meus_arquivos.tar.bz2 documentos/
```

### Extrair um arquivo tar.bz2
Para extrair um arquivo tar.bz2, use:

```bash
tar -xjvf meus_arquivos.tar.bz2
```

## Tips
- Sempre verifique o conteúdo de um arquivo tar antes de extrair, usando `tar -tvf arquivo.tar`.
- Utilize a opção `-C` para extrair arquivos em um diretório específico: `tar -xvf arquivo.tar -C /caminho/do/diretorio`.
- Para backups, considere usar a combinação de `tar` com `cron` para agendar tarefas de backup automáticas.