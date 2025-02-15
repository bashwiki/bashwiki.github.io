# [리눅스] Bash lspci 사용법

## Overview
O comando `lspci` é uma ferramenta de linha de comando no Linux que lista todos os dispositivos PCI (Peripheral Component Interconnect) conectados ao sistema. Ele fornece informações detalhadas sobre cada dispositivo, incluindo o fabricante, o modelo e o tipo de dispositivo. O principal objetivo do `lspci` é ajudar engenheiros e desenvolvedores a diagnosticar e entender a configuração de hardware de um sistema.

## Usage
A sintaxe básica do comando `lspci` é a seguinte:

```bash
lspci [opções]
```

Algumas opções comuns incluem:

- `-v`: Mostra informações detalhadas sobre cada dispositivo.
- `-vv`: Fornece ainda mais detalhes, útil para depuração.
- `-k`: Exibe informações sobre os drivers associados a cada dispositivo.
- `-n`: Mostra os IDs de vendor e device em formato numérico, ao invés de nomes.
- `-t`: Exibe a árvore de dispositivos PCI, mostrando a hierarquia de conexão.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `lspci`:

1. Para listar todos os dispositivos PCI com informações detalhadas:

   ```bash
   lspci -v
   ```

2. Para visualizar a árvore de dispositivos PCI:

   ```bash
   lspci -t
   ```

3. Para listar dispositivos PCI com seus respectivos drivers:

   ```bash
   lspci -k
   ```

## Tips
- Utilize a opção `-v` para obter informações mais detalhadas sobre os dispositivos, especialmente se você estiver tentando resolver problemas de hardware.
- Combine opções para personalizar a saída. Por exemplo, `lspci -v -k` pode ser útil para ver tanto as informações detalhadas quanto os drivers associados.
- Se você estiver procurando por um dispositivo específico, pode usar o comando `grep` para filtrar a saída. Por exemplo:

  ```bash
  lspci | grep -i network
  ```

Isso irá listar apenas os dispositivos relacionados à rede, facilitando a localização de informações relevantes.