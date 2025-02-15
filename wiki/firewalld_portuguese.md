# [리눅스] Bash firewalld 사용법

## Overview
O `firewalld` é um gerenciador de firewall dinâmico que fornece uma interface para gerenciar regras de firewall em sistemas Linux. Ele permite que os usuários configurem regras de firewall de forma mais flexível e intuitiva, utilizando zonas e serviços, em vez de regras de iptables estáticas. O principal propósito do `firewalld` é proteger sistemas e redes, controlando o tráfego de entrada e saída com base em políticas definidas pelo usuário.

## Usage
A sintaxe básica do comando `firewalld` é a seguinte:

```bash
firewall-cmd [OPÇÕES]
```

Algumas opções comuns incluem:

- `--zone=<zona>`: Especifica a zona na qual a regra será aplicada.
- `--add-service=<serviço>`: Adiciona um serviço à zona especificada.
- `--remove-service=<serviço>`: Remove um serviço da zona especificada.
- `--list-all`: Lista todas as configurações da zona atual, incluindo serviços, portas e regras.
- `--permanent`: Aplica as mudanças de forma permanente, ou seja, persiste após a reinicialização do sistema.

## Examples
### Exemplo 1: Adicionar um serviço à zona pública
Para adicionar o serviço HTTP à zona pública, você pode usar o seguinte comando:

```bash
sudo firewall-cmd --zone=public --add-service=http --permanent
```

Após adicionar o serviço, é necessário recarregar as configurações do `firewalld` para que as mudanças tenham efeito:

```bash
sudo firewall-cmd --reload
```

### Exemplo 2: Listar todas as configurações da zona atual
Para visualizar todas as configurações da zona atual, incluindo serviços e portas permitidas, utilize:

```bash
sudo firewall-cmd --list-all
```

## Tips
- Sempre utilize a opção `--permanent` ao adicionar ou remover serviços se você deseja que as mudanças persistam após a reinicialização do sistema.
- Use `firewall-cmd --state` para verificar se o `firewalld` está ativo e em execução.
- Considere a utilização de zonas para organizar melhor as regras de firewall, permitindo que diferentes interfaces de rede tenham diferentes níveis de segurança.
- Teste suas configurações em um ambiente seguro antes de aplicá-las em produção para evitar interrupções no serviço.