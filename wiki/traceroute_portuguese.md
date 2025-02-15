# [리눅스] Bash traceroute 사용법

## Overview
O comando `traceroute` é uma ferramenta de rede utilizada para rastrear a rota que os pacotes de dados percorrem de um host de origem até um host de destino. Ele fornece informações sobre cada salto (ou "hop") que os pacotes fazem através da rede, incluindo o tempo que leva para chegar a cada ponto. O principal propósito do `traceroute` é ajudar a diagnosticar problemas de conectividade e desempenho em redes IP, permitindo que engenheiros e desenvolvedores identifiquem onde ocorrem atrasos ou falhas na comunicação.

## Usage
A sintaxe básica do comando `traceroute` é a seguinte:

```bash
traceroute [opções] destino
```

### Opções Comuns:
- `-m <número>`: Define o número máximo de saltos a serem realizados. O padrão é 30.
- `-p <porta>`: Especifica a porta UDP a ser usada. O padrão é 33434.
- `-n`: Faz com que o `traceroute` não resolva os endereços IP em nomes de host, exibindo apenas endereços numéricos.
- `-w <segundos>`: Define o tempo de espera para cada resposta. O padrão é 5 segundos.

## Examples
### Exemplo 1: Rastreando um domínio
Para rastrear a rota até o domínio `example.com`, você pode usar o seguinte comando:

```bash
traceroute example.com
```

Este comando mostrará cada salto que os pacotes fazem até chegar ao `example.com`, juntamente com os tempos de resposta.

### Exemplo 2: Rastreando com um número máximo de saltos
Se você quiser limitar o número de saltos a 15, pode usar a opção `-m`:

```bash
traceroute -m 15 example.com
```

Isso fará com que o `traceroute` pare após 15 saltos, mesmo que o destino não tenha sido alcançado.

## Tips
- Utilize a opção `-n` se você deseja acelerar o processo de rastreamento, evitando a resolução de nomes de host.
- Combine o `traceroute` com outras ferramentas de rede, como `ping`, para obter uma visão mais completa da conectividade e desempenho da rede.
- Lembre-se de que alguns roteadores podem estar configurados para não responder a pacotes de `traceroute`, resultando em saltos que não aparecem na saída do comando.