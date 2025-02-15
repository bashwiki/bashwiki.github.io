# [리눅스] Bash ufw 사용법

## Overview
O `ufw` (Uncomplicated Firewall) é uma ferramenta de configuração de firewall para sistemas operacionais baseados em Linux. Seu principal objetivo é facilitar a gestão de regras de firewall, permitindo que usuários e administradores configurem facilmente as regras de entrada e saída de tráfego de rede. O `ufw` é projetado para ser simples e intuitivo, tornando-o uma escolha popular para quem não possui experiência avançada em configuração de firewalls.

## Usage
A sintaxe básica do comando `ufw` é a seguinte:

```bash
ufw [opções] [comando]
```

### Comandos Comuns:
- `enable`: Ativa o firewall.
- `disable`: Desativa o firewall.
- `status`: Exibe o status atual do firewall e as regras ativas.
- `allow`: Permite o tráfego em uma porta ou serviço específico.
- `deny`: Bloqueia o tráfego em uma porta ou serviço específico.
- `delete`: Remove uma regra existente.

### Opções Comuns:
- `verbose`: Exibe informações detalhadas sobre as operações realizadas.
- `version`: Mostra a versão do `ufw` instalada.

## Examples
### Exemplo 1: Ativar o Firewall
Para ativar o firewall usando o `ufw`, você pode usar o seguinte comando:

```bash
sudo ufw enable
```

Este comando ativa o firewall e começa a aplicar as regras definidas.

### Exemplo 2: Permitir Acesso à Porta 22 (SSH)
Se você deseja permitir conexões SSH (porta 22), você pode usar o comando:

```bash
sudo ufw allow 22
```

Isso adiciona uma regra que permite o tráfego na porta 22, essencial para conexões remotas via SSH.

## Tips
- Sempre verifique o status do firewall após fazer alterações usando `ufw status`.
- É uma boa prática permitir o acesso SSH antes de ativar o firewall, para evitar ser bloqueado de acessar o servidor remotamente.
- Utilize o comando `ufw status verbose` para obter uma visão mais detalhada das regras e do status do firewall.
- Considere fazer backup das regras do firewall antes de realizar alterações significativas, para que você possa restaurá-las se necessário.