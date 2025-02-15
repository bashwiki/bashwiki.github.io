# [리눅스] Bash lsusb 사용법

## Overview
O comando `lsusb` é uma ferramenta de linha de comando utilizada em sistemas Linux para listar todos os dispositivos USB conectados ao sistema. Ele fornece informações detalhadas sobre cada dispositivo, como o ID do fabricante, ID do produto e a classe do dispositivo. O principal propósito do `lsusb` é ajudar engenheiros e desenvolvedores a diagnosticar problemas relacionados a dispositivos USB e a obter informações sobre a configuração do hardware.

## Usage
A sintaxe básica do comando `lsusb` é a seguinte:

```bash
lsusb [opções]
```

### Opções Comuns:
- `-v`: Modo verbose. Exibe informações detalhadas sobre cada dispositivo USB.
- `-t`: Exibe a árvore de dispositivos USB, mostrando a hierarquia de conexão.
- `-s <bus>:<device>`: Lista apenas o dispositivo especificado pelo número do barramento e do dispositivo.
- `-d <vendor>:<product>`: Filtra a lista para mostrar apenas o dispositivo com o ID do fabricante e do produto especificados.

## Examples
### Exemplo 1: Listar todos os dispositivos USB
Para listar todos os dispositivos USB conectados ao sistema, basta executar o comando:

```bash
lsusb
```

A saída mostrará uma lista de dispositivos, incluindo informações como o ID do fabricante e do produto.

### Exemplo 2: Exibir informações detalhadas sobre um dispositivo específico
Para obter informações detalhadas sobre um dispositivo USB, você pode usar a opção `-v`. Por exemplo:

```bash
lsusb -v -s 001:002
```

Neste exemplo, `001:002` representa o número do barramento e do dispositivo que você deseja inspecionar.

## Tips
- Utilize o comando `lsusb` em conjunto com outras ferramentas, como `dmesg`, para obter uma visão mais completa sobre o funcionamento dos dispositivos USB.
- Quando estiver depurando problemas com dispositivos USB, o modo verbose (`-v`) pode fornecer informações valiosas que ajudam a identificar falhas ou configurações incorretas.
- Familiarize-se com os IDs de fabricante e produto, pois eles são úteis para pesquisar drivers ou suporte para dispositivos específicos.