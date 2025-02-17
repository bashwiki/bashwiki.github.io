# [Linux] Bash iostat Uso: Monitora o desempenho de entrada e saída

## Overview
O comando `iostat` é uma ferramenta utilizada para monitorar o desempenho de entrada e saída de dispositivos e partições em sistemas Linux. Ele fornece informações sobre a utilização da CPU e estatísticas de I/O, permitindo que os usuários identifiquem gargalos e analisem o desempenho do sistema.

## Usage
A sintaxe básica do comando `iostat` é a seguinte:

```bash
iostat [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `iostat`:

- `-c`: Exibe apenas as estatísticas da CPU.
- `-d`: Mostra as estatísticas de dispositivos de bloco.
- `-x`: Exibe estatísticas detalhadas de dispositivos.
- `-m`: Mostra as estatísticas em megabytes por segundo.
- `-t`: Inclui a hora e a data na saída.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `iostat`:

1. **Exibir estatísticas básicas de CPU e I/O:**

```bash
iostat
```

2. **Mostrar apenas as estatísticas da CPU:**

```bash
iostat -c
```

3. **Exibir estatísticas detalhadas de dispositivos:**

```bash
iostat -x
```

4. **Mostrar estatísticas em megabytes por segundo:**

```bash
iostat -m
```

5. **Executar o iostat a cada 5 segundos:**

```bash
iostat 5
```

## Tips
- Utilize a opção `-x` para obter uma visão mais detalhada do desempenho de cada dispositivo, o que pode ajudar na identificação de problemas específicos.
- Combine o `iostat` com outras ferramentas de monitoramento, como `top` ou `vmstat`, para uma análise mais abrangente do desempenho do sistema.
- Salve a saída do `iostat` em um arquivo para análise posterior, utilizando a redireção de saída, como em `iostat > iostat_output.txt`.