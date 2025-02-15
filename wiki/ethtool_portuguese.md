# [리눅스] Bash ethtool 사용법

## Overview
O `ethtool` é uma ferramenta de linha de comando utilizada em sistemas Linux para consultar e modificar as configurações de interfaces de rede Ethernet. Seu principal propósito é fornecer informações detalhadas sobre a interface de rede, como velocidade, duplex, estatísticas de transmissão e recepção, e também permitir a configuração de parâmetros como modo de operação e ativação/desativação de recursos.

## Usage
A sintaxe básica do comando `ethtool` é a seguinte:

```bash
ethtool [opções] <interface>
```

Onde `<interface>` é o nome da interface de rede que você deseja consultar ou modificar (por exemplo, `eth0`, `enp3s0`, etc.).

### Opções Comuns
- `-i`: Exibe informações do driver da interface.
- `-S`: Mostra estatísticas detalhadas da interface.
- `-p`: Pisca o LED da interface para identificação.
- `-s`: Permite configurar parâmetros da interface, como velocidade e duplex.
- `-a`: Exibe ou altera as configurações de auto-negociação.

## Examples
### Exemplo 1: Consultar informações da interface
Para obter informações básicas sobre a interface de rede `eth0`, você pode usar o seguinte comando:

```bash
ethtool eth0
```

Este comando retornará detalhes como a velocidade da conexão, modo duplex e suporte a recursos.

### Exemplo 2: Exibir estatísticas da interface
Para visualizar estatísticas detalhadas da interface `eth0`, utilize:

```bash
ethtool -S eth0
```

Isso mostrará informações como pacotes transmitidos, pacotes recebidos e erros.

## Tips
- Sempre verifique se você tem permissões adequadas para executar o `ethtool`, pois algumas operações podem exigir privilégios de superusuário.
- Utilize o comando `man ethtool` para acessar o manual completo e explorar todas as opções disponíveis.
- Ao modificar configurações com a opção `-s`, tenha cuidado para não desativar acidentalmente a interface ou configurar parâmetros incompatíveis que possam causar perda de conectividade.