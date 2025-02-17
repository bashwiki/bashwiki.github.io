# [Linux] Bash ethtool Uso: Ferramenta para gerenciar interfaces de rede

## Overview
O comando `ethtool` é uma ferramenta poderosa utilizada no Linux para consultar e modificar as configurações de interfaces de rede Ethernet. Ele permite que os usuários obtenham informações detalhadas sobre a interface, como velocidade, duplex, e estatísticas de tráfego, além de permitir ajustes em parâmetros da interface.

## Usage
A sintaxe básica do comando `ethtool` é a seguinte:

```bash
ethtool [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `ethtool`:

- `-s` : Modifica as configurações da interface de rede.
- `-i` : Exibe informações do driver da interface.
- `-p` : Pisca o LED da interface para identificação.
- `-t` : Executa um teste de loopback na interface.
- `-S` : Mostra estatísticas detalhadas da interface.

## Common Examples
Aqui estão alguns exemplos práticos de como usar o `ethtool`:

1. **Verificar informações da interface de rede**:
   ```bash
   ethtool eth0
   ```

2. **Modificar a velocidade e o modo duplex**:
   ```bash
   ethtool -s eth0 speed 100 duplex full
   ```

3. **Exibir informações do driver**:
   ```bash
   ethtool -i eth0
   ```

4. **Piscar o LED da interface para identificação**:
   ```bash
   ethtool -p eth0
   ```

5. **Mostrar estatísticas detalhadas da interface**:
   ```bash
   ethtool -S eth0
   ```

## Tips
- Sempre verifique as permissões necessárias, pois algumas operações do `ethtool` podem exigir privilégios de superusuário.
- Utilize o comando `man ethtool` para acessar a documentação completa e explorar mais opções disponíveis.
- Ao modificar configurações, tenha cuidado para não desativar acidentalmente a interface de rede, especialmente em servidores remotos.