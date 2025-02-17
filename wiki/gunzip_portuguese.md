# [Linux] Bash gunzip uso: Descompactar arquivos gzip

## Overview
O comando `gunzip` é utilizado para descompactar arquivos que foram comprimidos no formato gzip. Ele é uma ferramenta essencial para gerenciar arquivos compactados, permitindo que os usuários recuperem os dados originais de forma rápida e eficiente.

## Usage
A sintaxe básica do comando `gunzip` é a seguinte:

```bash
gunzip [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `gunzip`:

- `-c`: Envia a saída descompactada para o stdout (saída padrão) em vez de substituir o arquivo original.
- `-f`: Força a descompactação, mesmo que o arquivo de destino já exista.
- `-k`: Mantém o arquivo original após a descompactação.
- `-r`: Descompacta arquivos recursivamente em diretórios.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `gunzip`:

1. **Descompactar um arquivo gzip**:
   ```bash
   gunzip arquivo.gz
   ```

2. **Descompactar e manter o arquivo original**:
   ```bash
   gunzip -k arquivo.gz
   ```

3. **Descompactar e enviar a saída para o stdout**:
   ```bash
   gunzip -c arquivo.gz > arquivo.txt
   ```

4. **Descompactar arquivos em um diretório recursivamente**:
   ```bash
   gunzip -r pasta/
   ```

## Tips
- Sempre verifique se você tem espaço suficiente em disco antes de descompactar arquivos grandes.
- Use a opção `-k` se você quiser manter o arquivo original após a descompactação.
- Para visualizar o conteúdo de um arquivo gzip sem descompactá-lo, você pode usar o comando `zcat`, que é equivalente a `gunzip -c`.