# [Linux] Bash mount uso: Montar sistemas de arquivos

## Overview
O comando `mount` é utilizado para montar sistemas de arquivos em um diretório específico do sistema Linux. Isso permite que o sistema acesse e utilize os dados armazenados em dispositivos de armazenamento, como discos rígidos, pen drives e partições.

## Usage
A sintaxe básica do comando `mount` é a seguinte:

```bash
mount [opções] [dispositivo] [ponto de montagem]
```

## Common Options
Aqui estão algumas opções comuns do comando `mount`:

- `-t tipo`: Especifica o tipo de sistema de arquivos a ser montado (por exemplo, `ext4`, `ntfs`).
- `-o opções`: Permite especificar opções adicionais, como `ro` (somente leitura) ou `rw` (leitura e escrita).
- `-a`: Monta todos os sistemas de arquivos listados no arquivo `/etc/fstab`.
- `-r`: Monta o sistema de arquivos como somente leitura.

## Common Examples

### Montar um dispositivo USB
Para montar um dispositivo USB localizado em `/dev/sdb1` no diretório `/mnt/usb`, você pode usar:

```bash
sudo mount /dev/sdb1 /mnt/usb
```

### Montar uma partição NTFS
Se você deseja montar uma partição NTFS em `/dev/sdc1` no diretório `/media/ntfs`, utilize:

```bash
sudo mount -t ntfs-3g /dev/sdc1 /media/ntfs
```

### Montar todos os sistemas de arquivos
Para montar todos os sistemas de arquivos definidos no arquivo `/etc/fstab`, execute:

```bash
sudo mount -a
```

### Montar um sistema de arquivos somente leitura
Para montar um sistema de arquivos como somente leitura, você pode usar a opção `-o ro`:

```bash
sudo mount -o ro /dev/sda1 /mnt/read_only
```

## Tips
- Sempre verifique se o ponto de montagem está vazio antes de montar um dispositivo, para evitar a perda de dados.
- Use o comando `df -h` para verificar quais sistemas de arquivos estão montados e seu uso de espaço.
- Para desmontar um sistema de arquivos, utilize o comando `umount` seguido do ponto de montagem ou do dispositivo. Por exemplo:

```bash
sudo umount /mnt/usb
```