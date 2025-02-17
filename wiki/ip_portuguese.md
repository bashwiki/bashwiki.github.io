# [Linux] Bash ip uso: Gerenciar configurações de rede

## Overview
O comando `ip` é uma ferramenta poderosa utilizada para gerenciar e configurar interfaces de rede no Linux. Ele permite que os usuários visualizem e modifiquem configurações de rede, como endereços IP, rotas e muito mais.

## Usage
A sintaxe básica do comando `ip` é a seguinte:

```bash
ip [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `ip`:

- `link`: Gerencia interfaces de rede.
- `addr`: Exibe ou modifica endereços IP.
- `route`: Manipula a tabela de rotas do sistema.
- `neigh`: Gerencia a tabela de vizinhança (ARP).
- `maddr`: Gerencia endereços multicast.

## Common Examples

### Exibir todas as interfaces de rede
Para listar todas as interfaces de rede disponíveis no sistema, use o seguinte comando:

```bash
ip link show
```

### Adicionar um endereço IP a uma interface
Para adicionar um endereço IP a uma interface específica, como `eth0`, utilize:

```bash
ip addr add 192.168.1.10/24 dev eth0
```

### Remover um endereço IP de uma interface
Para remover um endereço IP de uma interface, use o comando:

```bash
ip addr del 192.168.1.10/24 dev eth0
```

### Exibir a tabela de rotas
Para visualizar a tabela de rotas do sistema, execute:

```bash
ip route show
```

### Adicionar uma rota
Para adicionar uma nova rota, utilize o seguinte comando:

```bash
ip route add 10.0.0.0/8 via 192.168.1.1
```

## Tips
- Sempre verifique as configurações atuais antes de fazer alterações, utilizando `ip addr show` e `ip route show`.
- Use `sudo` se você encontrar problemas de permissão ao executar comandos que alteram configurações de rede.
- Familiarize-se com as opções de ajuda do comando, usando `ip help`, para explorar mais funcionalidades.