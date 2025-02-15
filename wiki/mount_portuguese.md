# [리눅스] Bash mount 사용법

## Overview
O comando `mount` no Linux é utilizado para montar sistemas de arquivos, permitindo que o usuário acesse e manipule dados armazenados em dispositivos de armazenamento, como discos rígidos, pen drives e partições. O principal objetivo do `mount` é conectar um sistema de arquivos a um ponto de montagem no diretório do sistema, tornando-o acessível para leitura e escrita.

## Usage
A sintaxe básica do comando `mount` é a seguinte:

```
mount [opções] dispositivo ponto_de_montagem
```

### Opções Comuns:
- `-t tipo`: Especifica o tipo do sistema de arquivos (por exemplo, `ext4`, `ntfs`, `vfat`, etc.).
- `-o opções`: Permite definir opções adicionais, como `ro` (somente leitura), `rw` (leitura e escrita), `noexec` (não permitir a execução de binários), entre outras.
- `-a`: Monta todos os sistemas de arquivos listados no arquivo `/etc/fstab`.
- `-r`: Monta o sistema de arquivos como somente leitura.

## Examples
### Exemplo 1: Montar um dispositivo USB
Para montar um dispositivo USB formatado em FAT32, você pode usar o seguinte comando:

```bash
sudo mount -t vfat /dev/sdb1 /mnt/usb
```

Neste exemplo, `/dev/sdb1` é o dispositivo USB e `/mnt/usb` é o ponto de montagem onde o conteúdo do dispositivo será acessível.

### Exemplo 2: Montar uma partição NTFS
Para montar uma partição NTFS, você pode usar:

```bash
sudo mount -t ntfs-3g /dev/sdc1 /mnt/ntfs
```

Aqui, `/dev/sdc1` representa a partição NTFS e `/mnt/ntfs` é o diretório onde ela será montada.

## Tips
- Sempre verifique se o ponto de montagem existe antes de usar o comando `mount`. Você pode criar um diretório usando `mkdir` se necessário.
- Use o comando `umount` para desmontar o sistema de arquivos quando não precisar mais dele, garantindo que todos os dados sejam salvos corretamente.
- Para evitar problemas de permissões, considere usar o `sudo` ao montar dispositivos que requerem privilégios de administrador.
- Consulte o arquivo `/etc/fstab` para configurações automáticas de montagem durante a inicialização do sistema.