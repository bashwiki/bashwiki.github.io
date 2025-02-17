# [Linux] Bash bzip2 Uso: Compactar e descompactar arquivos

## Overview
O comando `bzip2` é uma ferramenta de compressão de arquivos que utiliza o algoritmo de compressão Burrows-Wheeler. Ele é conhecido por oferecer uma taxa de compressão superior em comparação com outras ferramentas como `gzip`. O `bzip2` é frequentemente utilizado para reduzir o tamanho de arquivos, facilitando o armazenamento e a transferência.

## Usage
A sintaxe básica do comando `bzip2` é a seguinte:

```bash
bzip2 [opções] [arquivos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `bzip2`:

- `-d`, `--decompress`: Descomprime um arquivo `.bz2`.
- `-k`, `--keep`: Mantém o arquivo original após a compressão.
- `-f`, `--force`: Força a compressão ou descompressão, sobrescrevendo arquivos existentes.
- `-v`, `--verbose`: Exibe informações detalhadas sobre o processo de compressão ou descompressão.
- `-z`, `--compress`: Comprime um arquivo (opção padrão).

## Common Examples
Aqui estão alguns exemplos práticos do uso do `bzip2`:

1. **Comprimir um arquivo**:
   ```bash
   bzip2 arquivo.txt
   ```
   Isso criará um arquivo chamado `arquivo.txt.bz2` e removerá o `arquivo.txt` original.

2. **Descomprimir um arquivo**:
   ```bash
   bzip2 -d arquivo.txt.bz2
   ```
   Isso restaurará o `arquivo.txt` original e removerá o `arquivo.txt.bz2`.

3. **Manter o arquivo original ao comprimir**:
   ```bash
   bzip2 -k arquivo.txt
   ```
   O `arquivo.txt` será comprimido, mas o original permanecerá.

4. **Forçar a compressão**:
   ```bash
   bzip2 -f arquivo.txt
   ```
   Se `arquivo.txt.bz2` já existir, ele será sobrescrito.

5. **Exibir informações detalhadas durante a compressão**:
   ```bash
   bzip2 -v arquivo.txt
   ```
   Isso mostrará detalhes do processo de compressão.

## Tips
- Sempre verifique o espaço em disco disponível antes de comprimir arquivos grandes, pois a compressão pode exigir espaço adicional temporário.
- Use a opção `-k` se você não quiser perder o arquivo original após a compressão.
- Para arquivos muito grandes, considere usar `tar` em conjunto com `bzip2` para facilitar a manipulação de múltiplos arquivos. Por exemplo:
  ```bash
  tar -cvjf arquivos.tar.bz2 pasta/
  ```
  Isso cria um arquivo tar comprimido com bzip2 da pasta especificada.