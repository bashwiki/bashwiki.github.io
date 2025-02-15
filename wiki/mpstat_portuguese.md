# [리눅스] Bash mpstat 사용법

## Visão Geral
O comando `mpstat` é uma ferramenta do pacote `sysstat` que fornece estatísticas de uso da CPU em sistemas Linux. Ele é especialmente útil para monitorar o desempenho do sistema, permitindo que engenheiros e desenvolvedores analisem a carga de trabalho em múltiplos processadores. O `mpstat` pode exibir informações sobre a utilização da CPU de forma detalhada, ajudando na identificação de gargalos e na otimização do desempenho do sistema.

## Uso
A sintaxe básica do comando `mpstat` é a seguinte:

```bash
mpstat [opções] [intervalo] [contagem]
```

### Opções Comuns:
- `-P ALL`: Mostra as estatísticas de todas as CPUs.
- `-u`: Exibe a utilização da CPU (esta é a opção padrão).
- `-h`: Exibe as estatísticas em um formato mais legível.
- `-V`: Mostra a versão do `mpstat`.

## Exemplos
### Exemplo 1: Estatísticas de CPU em Intervalos
Para monitorar a utilização da CPU a cada 2 segundos, você pode usar o seguinte comando:

```bash
mpstat 2
```

Este comando exibirá as estatísticas de utilização da CPU a cada 2 segundos até que você interrompa o processo.

### Exemplo 2: Estatísticas de Todas as CPUs
Para visualizar as estatísticas de todas as CPUs em um formato legível, utilize:

```bash
mpstat -P ALL -h 2 5
```

Neste exemplo, o `mpstat` mostrará as estatísticas de todas as CPUs a cada 2 segundos, totalizando 5 iterações.

## Dicas
- Utilize o `mpstat` em conjunto com outras ferramentas de monitoramento, como `top` ou `htop`, para obter uma visão mais abrangente do desempenho do sistema.
- Salve a saída do `mpstat` em um arquivo para análise posterior, redirecionando a saída com `>`:

```bash
mpstat -P ALL 2 5 > estatisticas_cpu.txt
```

- Familiarize-se com as diferentes métricas exibidas pelo `mpstat`, como `%idle`, `%iowait`, e `%system`, para entender melhor o comportamento do seu sistema sob carga.