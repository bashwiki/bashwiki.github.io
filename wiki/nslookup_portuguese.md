# [Linux] Bash nslookup Uso: Consulta de endereços DNS

## Overview
O comando `nslookup` é uma ferramenta de linha de comando utilizada para consultar informações sobre servidores DNS. Ele permite que os usuários obtenham detalhes sobre domínios, como endereços IP, registros de MX, entre outros.

## Usage
A sintaxe básica do comando `nslookup` é a seguinte:

```bash
nslookup [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `nslookup`:

- `-type=tipo`: Especifica o tipo de registro DNS a ser consultado (por exemplo, A, AAAA, MX).
- `-timeout=segundos`: Define o tempo limite para a consulta em segundos.
- `-retry=n`: Define o número de tentativas em caso de falha na consulta.
- `-debug`: Ativa o modo de depuração, mostrando informações detalhadas sobre a consulta.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `nslookup`:

1. **Consultar o endereço IP de um domínio:**

```bash
nslookup www.exemplo.com
```

2. **Consultar um registro MX para um domínio:**

```bash
nslookup -type=MX exemplo.com
```

3. **Consultar um registro específico (AAAA) para um domínio:**

```bash
nslookup -type=AAAA www.exemplo.com
```

4. **Definir um servidor DNS específico para a consulta:**

```bash
nslookup www.exemplo.com 8.8.8.8
```

5. **Ativar o modo de depuração:**

```bash
nslookup -debug www.exemplo.com
```

## Tips
- Sempre verifique se você está usando o servidor DNS correto, especialmente em redes corporativas.
- Utilize o modo de depuração para resolver problemas de consulta e entender melhor o que está acontecendo.
- Combine `nslookup` com outras ferramentas de rede, como `ping` e `traceroute`, para uma análise mais completa da conectividade.