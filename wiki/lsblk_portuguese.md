# [리눅스] Bash lsblk 사용법

## Overview
O comando `lsblk` é uma ferramenta utilizada no Linux para listar todos os dispositivos de bloco disponíveis no sistema. Dispositivos de bloco incluem discos rígidos, partições, unidades flash USB e outros dispositivos de armazenamento. O principal objetivo do `lsblk` é fornecer uma visão clara e organizada da hierarquia dos dispositivos de armazenamento, permitindo que engenheiros e desenvolvedores identifiquem facilmente as unidades e suas respectivas partições.

## Usage
A sintaxe básica do comando `lsblk` é a seguinte:

```bash
lsblk [opções]
```

Algumas opções comuns incluem:

- `-a`, `--all`: Exibe todos os dispositivos, incluindo aqueles que não estão montados.
- `-f`, `--fs`: Mostra informações sobre o sistema de arquivos, como tipo e UUID.
- `-l`, `--list`: Exibe a saída em formato de lista em vez da visualização padrão em árvore.
- `-o`, `--output`: Permite especificar quais colunas exibir na saída.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `lsblk`:

1. Para listar todos os dispositivos de bloco disponíveis no sistema:

```bash
lsblk
```

2. Para exibir informações detalhadas sobre os sistemas de arquivos dos dispositivos:

```bash
lsblk -f
```

3. Para listar todos os dispositivos, incluindo aqueles que não estão montados, em formato de lista:

```bash
lsblk -a -l
```

## Tips
- Utilize a opção `-o` para personalizar a saída e focar nas informações mais relevantes para suas necessidades. Por exemplo, `lsblk -o NAME,SIZE,TYPE,MOUNTPOINT` mostrará apenas o nome, tamanho, tipo e ponto de montagem dos dispositivos.
- Combine o `lsblk` com outros comandos, como `grep`, para filtrar resultados específicos. Por exemplo, `lsblk | grep sda` para encontrar informações sobre o dispositivo `sda`.
- Lembre-se de que o `lsblk` não requer privilégios de superusuário para ser executado, o que o torna uma ferramenta acessível para todos os usuários do sistema.