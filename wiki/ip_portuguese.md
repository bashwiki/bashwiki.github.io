# [리눅스] Bash ip 사용법

## Overview
O comando `ip` é uma ferramenta poderosa utilizada em sistemas Linux para gerenciar e configurar interfaces de rede. Ele faz parte do pacote `iproute2`, que substitui o antigo comando `ifconfig`. O `ip` permite que os usuários visualizem e manipulem informações sobre endereços IP, rotas, dispositivos de rede e muito mais, oferecendo uma interface mais moderna e flexível para a administração de redes.

## Usage
A sintaxe básica do comando `ip` é a seguinte:

```
ip [OPTIONS] OBJECT { COMMAND | help }
```

### Principais opções:
- `link`: Manipula interfaces de rede (ativar, desativar, adicionar, remover).
- `addr`: Gerencia endereços IP associados às interfaces de rede.
- `route`: Manipula a tabela de roteamento do sistema.
- `neigh`: Gerencia a tabela de vizinhança (ARP).

## Examples
### Exemplo 1: Listar interfaces de rede
Para listar todas as interfaces de rede disponíveis no sistema, você pode usar o seguinte comando:

```bash
ip link show
```

Esse comando exibirá uma lista de interfaces, mostrando seu estado (up ou down) e outras informações relevantes.

### Exemplo 2: Adicionar um endereço IP a uma interface
Para adicionar um endereço IP a uma interface de rede específica, como `eth0`, você pode usar o seguinte comando:

```bash
ip addr add 192.168.1.10/24 dev eth0
```

Esse comando atribui o endereço IP `192.168.1.10` com uma máscara de sub-rede de `24` bits à interface `eth0`.

## Tips
- Utilize `ip -h` para obter ajuda sobre os comandos e opções disponíveis.
- Combine o comando `ip` com `grep` para filtrar resultados específicos, como endereços IP ou interfaces.
- Sempre verifique o estado das interfaces após realizar alterações, usando `ip link show`.
- Para remover um endereço IP, você pode usar o comando `ip addr del`, seguido do endereço e da interface, por exemplo:

```bash
ip addr del 192.168.1.10/24 dev eth0
```

Essas práticas ajudarão a garantir que você utilize o comando `ip` de forma eficaz e segura em suas tarefas de gerenciamento de rede.