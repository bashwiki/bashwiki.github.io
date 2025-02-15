# [리눅스] Bash rsync 사용법

## Overview
O `rsync` é uma ferramenta poderosa de sincronização de arquivos e diretórios em sistemas Unix-like. Seu principal propósito é transferir e sincronizar arquivos de forma eficiente, minimizando a quantidade de dados que precisam ser copiados. Ele utiliza um algoritmo que verifica as diferenças entre os arquivos de origem e destino, transferindo apenas as partes que mudaram, o que o torna ideal para backups e replicação de dados.

## Usage
A sintaxe básica do comando `rsync` é a seguinte:

```bash
rsync [opções] origem destino
```

### Opções Comuns:
- `-a`: Modo de arquivamento; preserva permissões, timestamps, links simbólicos, etc.
- `-v`: Modo verbose; fornece mais informações sobre o que está sendo transferido.
- `-z`: Comprime os dados durante a transferência, economizando largura de banda.
- `-r`: Sincroniza diretórios recursivamente.
- `--delete`: Remove arquivos no destino que não estão mais na origem.
- `-n`: Modo de simulação; mostra o que seria feito sem realmente transferir os arquivos.

## Examples
### Exemplo 1: Sincronizar um diretório local
Para sincronizar um diretório local chamado `meus_dados` para um diretório de backup chamado `backup_dados`, você pode usar o seguinte comando:

```bash
rsync -av meus_dados/ backup_dados/
```

Neste exemplo, `-a` garante que todas as propriedades dos arquivos sejam preservadas e `-v` fornece uma saída detalhada do que está sendo transferido.

### Exemplo 2: Sincronizar para um servidor remoto
Para sincronizar arquivos de um diretório local para um servidor remoto, você pode usar:

```bash
rsync -avz meus_dados/ usuario@servidor:/caminho/para/backup/
```

Aqui, `-z` é utilizado para comprimir os dados durante a transferência, o que pode ser útil em conexões lentas.

## Tips
- Sempre teste suas operações com a opção `-n` para evitar perdas acidentais de dados, especialmente quando usar `--delete`.
- Considere usar `rsync` em scripts de backup automatizados para garantir que seus dados estejam sempre atualizados.
- Utilize a opção `--progress` para monitorar o progresso da transferência, especialmente em transferências grandes.
- Para transferências seguras, combine `rsync` com `ssh` para garantir que os dados sejam criptografados durante a transferência.