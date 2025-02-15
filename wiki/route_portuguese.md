# [리눅스] Bash route 사용법

## Overview
O comando `route` é utilizado para visualizar e manipular a tabela de roteamento do kernel em sistemas operacionais baseados em Unix, como Linux. A tabela de roteamento é uma estrutura de dados que contém informações sobre como os pacotes de dados devem ser encaminhados para diferentes redes. O principal objetivo do comando `route` é permitir que os administradores de sistema e desenvolvedores configurem rotas de rede, verifiquem o estado atual das rotas e realizem diagnósticos de conectividade.

## Usage
A sintaxe básica do comando `route` é a seguinte:

```
route [opções] [comando] [destino] [gateway] [máscara] [interface]
```

### Comandos Comuns:
- `-n`: Exibe as rotas sem tentar resolver os nomes de host, mostrando apenas endereços IP.
- `add`: Adiciona uma nova rota à tabela de roteamento.
- `del`: Remove uma rota existente da tabela de roteamento.
- `show`: Mostra a tabela de roteamento atual.

## Examples
### Exemplo 1: Visualizar a tabela de roteamento
Para visualizar a tabela de roteamento atual, você pode usar o seguinte comando:

```bash
route -n
```

Este comando exibirá a tabela de roteamento sem resolver os endereços IP para nomes de host, permitindo uma visualização mais rápida e direta.

### Exemplo 2: Adicionar uma nova rota
Para adicionar uma nova rota, você pode usar o comando `add`. Por exemplo, para adicionar uma rota para a rede `192.168.1.0` através do gateway `192.168.0.1`, você pode executar:

```bash
sudo route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.0.1
```

Este comando informa ao sistema que, para alcançar a rede `192.168.1.0`, deve-se usar o gateway `192.168.0.1`.

## Tips
- Sempre use o comando `route` com privilégios de superusuário (sudo) ao adicionar ou remover rotas, pois essas operações requerem permissões administrativas.
- Utilize a opção `-n` para evitar a resolução de nomes, especialmente em redes grandes, onde a resolução de nomes pode causar atrasos.
- Após fazer alterações na tabela de roteamento, é uma boa prática verificar a tabela novamente usando `route -n` para garantir que as alterações foram aplicadas corretamente.
- Considere o uso de ferramentas mais modernas, como `ip route`, que oferecem funcionalidades mais avançadas e são recomendadas para uso em sistemas Linux mais recentes.