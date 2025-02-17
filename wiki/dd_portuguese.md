# [Linux] Bash dd Uso: Copiar e converter arquivos

## Overview
O comando `dd` é uma ferramenta poderosa no Linux utilizada para copiar e converter arquivos. Ele é frequentemente usado para criar imagens de disco, fazer backups e transferir dados entre dispositivos.

## Usage
A sintaxe básica do comando `dd` é a seguinte:

```bash
dd [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `dd`:

- `if=`: Especifica o arquivo de entrada (input file).
- `of=`: Especifica o arquivo de saída (output file).
- `bs=`: Define o tamanho do bloco a ser lido e escrito.
- `count=`: Especifica o número de blocos a serem copiados.
- `status=`: Controla a saída de status (ex: `none`, `noxfer`, `progress`).

## Common Examples

### Copiar um arquivo
Para copiar um arquivo chamado `arquivo.txt` para `copia.txt`:

```bash
dd if=arquivo.txt of=copia.txt
```

### Criar uma imagem de disco
Para criar uma imagem de disco de um dispositivo, como `/dev/sda`, para um arquivo chamado `imagem.img`:

```bash
dd if=/dev/sda of=imagem.img bs=4M
```

### Restaurar uma imagem de disco
Para restaurar uma imagem de disco de volta para um dispositivo:

```bash
dd if=imagem.img of=/dev/sda bs=4M
```

### Copiar dados de um dispositivo USB
Para copiar dados de um dispositivo USB montado em `/dev/sdb` para um arquivo de imagem:

```bash
dd if=/dev/sdb of=usb_backup.img bs=1M
```

## Tips
- Sempre verifique se você está usando o dispositivo correto ao usar `dd`, pois ele pode sobrescrever dados importantes.
- Use a opção `status=progress` para monitorar o progresso da operação de cópia.
- Considere usar `sync` após o comando `dd` para garantir que todos os dados sejam gravados corretamente no disco.