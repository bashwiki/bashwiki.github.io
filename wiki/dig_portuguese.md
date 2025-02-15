# [리눅스] Bash dig 사용법

## Overview
O comando `dig` (Domain Information Groper) é uma ferramenta de linha de comando utilizada para consultar informações sobre registros DNS (Domain Name System). Ele permite que engenheiros e desenvolvedores verifiquem a resolução de nomes de domínio, obtenham detalhes sobre registros específicos e diagnostiquem problemas relacionados ao DNS. O `dig` é amplamente utilizado devido à sua simplicidade e à riqueza de informações que pode fornecer.

## Usage
A sintaxe básica do comando `dig` é a seguinte:

```
dig [opções] [nome_do_domínio] [tipo_de_registro]
```

### Opções Comuns:
- `@servidor`: Especifica um servidor DNS para realizar a consulta. Por exemplo, `@8.8.8.8` utiliza o servidor DNS público do Google.
- `-t tipo`: Define o tipo de registro DNS a ser consultado, como `A`, `AAAA`, `MX`, `CNAME`, entre outros. Se não for especificado, o tipo padrão é `A`.
- `+short`: Exibe uma saída mais concisa, mostrando apenas os resultados principais da consulta.
- `+trace`: Realiza uma consulta completa, mostrando cada passo do processo de resolução do nome.

## Examples
### Exemplo 1: Consulta de um registro A
Para consultar o endereço IP associado ao domínio `example.com`, você pode usar o seguinte comando:

```bash
dig example.com A
```

### Exemplo 2: Consulta com servidor específico e saída curta
Para consultar o registro MX do domínio `example.com` utilizando o servidor DNS do Google e obter uma saída mais curta, o comando seria:

```bash
dig @8.8.8.8 example.com MX +short
```

## Tips
- Utilize a opção `+trace` para entender como a resolução de um nome de domínio é realizada, especialmente útil para diagnosticar problemas de DNS.
- Sempre verifique se o servidor DNS que você está utilizando está acessível e respondendo corretamente.
- Combine o `dig` com outros comandos de rede, como `ping` e `nslookup`, para obter uma visão mais abrangente sobre a conectividade e resolução de nomes de domínio.
- Salve as saídas do `dig` em um arquivo para análise posterior, utilizando a redireção de saída, por exemplo: `dig example.com > resultado.txt`.