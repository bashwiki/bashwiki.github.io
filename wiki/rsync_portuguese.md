# [Linux] Bash rsync Uso: Sincronização de arquivos e diretórios

O comando `rsync` é uma ferramenta poderosa para sincronizar arquivos e diretórios entre diferentes locais, seja no mesmo sistema ou entre sistemas remotos.

## Overview
O `rsync` é utilizado para transferir e sincronizar arquivos de forma eficiente, minimizando a quantidade de dados copiados ao usar um algoritmo que apenas copia as partes alteradas dos arquivos. Isso o torna ideal para backups e transferências de grandes volumes de dados.

## Usage
A sintaxe básica do comando `rsync` é:

```bash
rsync [opções] [origem] [destino]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `rsync`:

- `-a`: Modo arquivamento; preserva permissões, timestamps e links simbólicos.
- `-v`: Modo verbose; exibe informações detalhadas sobre o que está sendo transferido.
- `-z`: Comprime os dados durante a transferência, economizando largura de banda.
- `-r`: Sincroniza diretórios recursivamente.
- `--delete`: Remove arquivos no destino que não estão mais na origem.

## Common Examples
Aqui estão alguns exemplos práticos de uso do `rsync`:

1. Sincronizar um diretório local para outro diretório local:
   ```bash
   rsync -av /caminho/para/origem/ /caminho/para/destino/
   ```

2. Sincronizar um diretório local para um servidor remoto:
   ```bash
   rsync -av /caminho/para/origem/ usuario@servidor:/caminho/para/destino/
   ```

3. Sincronizar um diretório remoto para um diretório local:
   ```bash
   rsync -av usuario@servidor:/caminho/para/origem/ /caminho/para/destino/
   ```

4. Sincronizar e excluir arquivos no destino que não estão na origem:
   ```bash
   rsync -av --delete /caminho/para/origem/ /caminho/para/destino/
   ```

## Tips
- Sempre faça um teste com a opção `--dry-run` (`-n`) para ver o que será transferido sem realmente realizar a cópia.
- Utilize a opção `-z` para transferências pela internet, especialmente se a largura de banda for limitada.
- Considere usar `rsync` com SSH para transferências seguras entre sistemas remotos.