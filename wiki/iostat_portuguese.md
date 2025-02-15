# [리눅스] Bash iostat 사용법

## Overview
O comando `iostat` é uma ferramenta do sistema que fornece informações sobre a utilização de CPU e estatísticas de entrada/saída (I/O) para dispositivos e partições. Ele é parte do pacote `sysstat` e é amplamente utilizado para monitorar o desempenho do sistema, ajudando engenheiros e desenvolvedores a identificar gargalos de I/O e a otimizar o uso de recursos.

## Usage
A sintaxe básica do comando `iostat` é a seguinte:

```bash
iostat [opções] [intervalo] [contagem]
```

### Opções Comuns:
- `-c`: Exibe apenas as estatísticas de CPU.
- `-d`: Exibe apenas as estatísticas de dispositivos.
- `-x`: Exibe estatísticas de dispositivos com informações adicionais (extensas).
- `-m`: Exibe as estatísticas em megabytes por segundo.
- `-p [dispositivo]`: Exibe estatísticas para um dispositivo específico.
- `intervalo`: O intervalo em segundos entre as atualizações das estatísticas.
- `contagem`: O número de vezes que as estatísticas devem ser exibidas.

## Examples
### Exemplo 1: Estatísticas de CPU e I/O
Para exibir as estatísticas de CPU e I/O a cada 2 segundos, por 5 vezes, você pode usar o seguinte comando:

```bash
iostat 2 5
```

### Exemplo 2: Estatísticas detalhadas de um dispositivo específico
Para obter informações detalhadas sobre um dispositivo específico (por exemplo, `/dev/sda`), você pode usar:

```bash
iostat -x -p /dev/sda 2 3
```

Este comando exibirá as estatísticas detalhadas do dispositivo `/dev/sda` a cada 2 segundos, por 3 vezes.

## Tips
- Utilize a opção `-m` para visualizar as estatísticas em megabytes, facilitando a interpretação dos dados de I/O.
- Combine `iostat` com outras ferramentas de monitoramento, como `top` ou `vmstat`, para obter uma visão mais abrangente do desempenho do sistema.
- Salve a saída do `iostat` em um arquivo para análise posterior, utilizando a redireção de saída:

```bash
iostat -x 1 10 > iostat_output.txt
```

Isso pode ser útil para auditorias de desempenho ou para identificar padrões de uso ao longo do tempo.