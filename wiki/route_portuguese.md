# [Linux] Bash route uso equivalente: Gerenciar tabelas de roteamento

## Overview
O comando `route` é utilizado para exibir e manipular a tabela de roteamento do sistema. Ele permite que os usuários visualizem as rotas de rede e adicionem ou removam entradas conforme necessário, facilitando a configuração de como os pacotes de dados são direcionados.

## Usage
A sintaxe básica do comando `route` é a seguinte:

```bash
route [options] [arguments]
```

## Common Options
- `-n`: Exibe as rotas sem tentar resolver os nomes de host, mostrando apenas endereços IP.
- `add`: Adiciona uma nova rota à tabela de roteamento.
- `del`: Remove uma rota existente da tabela.
- `-ee`: Exibe informações detalhadas sobre as rotas.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `route`:

1. **Exibir a tabela de roteamento atual:**
   ```bash
   route -n
   ```

2. **Adicionar uma nova rota:**
   ```bash
   route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.0.1
   ```

3. **Remover uma rota existente:**
   ```bash
   route del -net 192.168.1.0 netmask 255.255.255.0
   ```

4. **Exibir informações detalhadas sobre as rotas:**
   ```bash
   route -ee
   ```

## Tips
- Sempre use a opção `-n` ao exibir rotas para acelerar o processo, especialmente em redes grandes, pois evita a resolução de nomes.
- Tenha cuidado ao adicionar ou remover rotas, pois isso pode impactar a conectividade da rede.
- Considere usar o comando `ip route` como uma alternativa moderna ao `route`, pois ele oferece mais funcionalidades e é mais amplamente suportado nas distribuições atuais.