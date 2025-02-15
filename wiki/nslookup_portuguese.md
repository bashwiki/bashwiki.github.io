# [리눅스] Bash nslookup 사용법

## Overview
O comando `nslookup` (Name Server Lookup) é uma ferramenta de linha de comando utilizada para consultar servidores DNS (Domain Name System). Ele permite que os usuários obtenham informações sobre domínios, como endereços IP, registros de recursos e outros dados relacionados ao DNS. O `nslookup` é frequentemente utilizado por engenheiros de rede e desenvolvedores para diagnosticar problemas de resolução de nomes e verificar a configuração do DNS.

## Usage
A sintaxe básica do comando `nslookup` é a seguinte:

```
nslookup [opções] [nome_do_domínio] [servidor_DNS]
```

### Opções Comuns:
- `-type=tipo`: Especifica o tipo de registro DNS a ser consultado (por exemplo, A, AAAA, MX, TXT).
- `-debug`: Ativa o modo de depuração, fornecendo informações detalhadas sobre a consulta.
- `-timeout=segundos`: Define o tempo limite para aguardar uma resposta do servidor DNS.
- `-port=porta`: Especifica a porta a ser utilizada para a consulta DNS (o padrão é 53).

## Examples
### Exemplo 1: Consultar o endereço IP de um domínio
Para obter o endereço IP associado a um domínio, você pode usar o seguinte comando:

```bash
nslookup www.exemplo.com
```

Este comando retornará o endereço IP do domínio "www.exemplo.com", juntamente com informações sobre o servidor DNS que respondeu à consulta.

### Exemplo 2: Consultar registros MX de um domínio
Para verificar os registros de troca de correio (MX) de um domínio, utilize a opção `-type=MX`:

```bash
nslookup -type=MX exemplo.com
```

Esse comando retornará os registros MX do domínio "exemplo.com", que são utilizados para direcionar o tráfego de e-mail.

## Tips
- Sempre que possível, utilize o modo de depuração (`-debug`) para obter mais informações sobre a consulta, especialmente ao solucionar problemas de DNS.
- Experimente consultar diferentes tipos de registros para obter uma visão mais abrangente da configuração DNS de um domínio.
- Se você estiver enfrentando problemas de resolução de nomes, verifique se o servidor DNS que está sendo utilizado está funcionando corretamente ou experimente usar um servidor DNS público, como o Google DNS (8.8.8.8).