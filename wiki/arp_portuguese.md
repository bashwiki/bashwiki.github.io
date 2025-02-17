# [Linux] Bash arp Uso: Gerenciar a tabela ARP

O comando `arp` é utilizado para gerenciar a tabela ARP (Address Resolution Protocol) em sistemas operacionais baseados em Unix, permitindo visualizar e manipular as associações entre endereços IP e endereços MAC.

## Overview
O comando `arp` é usado para exibir e modificar a tabela ARP, que mapeia endereços IP para endereços MAC. Essa tabela é fundamental para a comunicação em redes locais, pois permite que dispositivos encontrem uns aos outros.

## Usage
A sintaxe básica do comando `arp` é a seguinte:

```bash
arp [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `arp`:

- `-a`: Exibe a tabela ARP completa.
- `-d <endereço>`: Remove uma entrada específica da tabela ARP.
- `-s <endereço> <endereço_mac>`: Adiciona uma nova entrada à tabela ARP.
- `-n`: Exibe endereços IP em formato numérico, sem tentar resolver nomes de host.

## Common Examples

### Exibir a tabela ARP
Para visualizar todas as entradas da tabela ARP, use:

```bash
arp -a
```

### Remover uma entrada da tabela ARP
Para remover uma entrada específica, como por exemplo o IP `192.168.1.10`, execute:

```bash
arp -d 192.168.1.10
```

### Adicionar uma nova entrada à tabela ARP
Para adicionar um novo mapeamento de IP para MAC, como o IP `192.168.1.20` com o MAC `00:11:22:33:44:55`, use:

```bash
arp -s 192.168.1.20 00:11:22:33:44:55
```

### Exibir a tabela ARP sem resolver nomes
Para exibir a tabela ARP em formato numérico, utilize:

```bash
arp -an
```

## Tips
- Sempre verifique a tabela ARP após fazer alterações para garantir que as entradas estão corretas.
- Use o comando `ping` antes de adicionar uma entrada ARP para garantir que o dispositivo está acessível na rede.
- Lembre-se de que as alterações feitas com `arp` podem não persistir após a reinicialização do sistema, dependendo da configuração da rede.