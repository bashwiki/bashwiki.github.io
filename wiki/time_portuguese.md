# [Linux] Bash time uso: mede o tempo de execução de comandos

## Overview
O comando `time` no Bash é utilizado para medir o tempo que um comando leva para ser executado. Ele fornece informações detalhadas sobre o tempo de execução, incluindo o tempo real, o tempo de CPU usado pelo usuário e o tempo de CPU usado pelo sistema.

## Usage
A sintaxe básica do comando `time` é a seguinte:

```bash
time [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `time`:

- `-p`: Exibe o tempo em um formato mais legível.
- `-o <arquivo>`: Redireciona a saída do tempo para um arquivo especificado.
- `-v`: Fornece uma saída detalhada com informações adicionais sobre o uso de recursos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `time`:

1. Medir o tempo de execução de um comando simples:
   ```bash
   time ls -l
   ```

2. Medir o tempo de execução de um script:
   ```bash
   time ./meu_script.sh
   ```

3. Usar a opção `-p` para um formato mais legível:
   ```bash
   time -p sleep 2
   ```

4. Redirecionar a saída do tempo para um arquivo:
   ```bash
   time -o tempo.txt sleep 3
   ```

5. Obter uma saída detalhada:
   ```bash
   time -v find / -name "arquivo.txt"
   ```

## Tips
- Utilize `time` para otimizar scripts e comandos, identificando gargalos de desempenho.
- Combine `time` com comandos que normalmente levam tempo, como `tar` ou `gzip`, para monitorar o desempenho.
- Lembre-se de que o tempo medido inclui o tempo de espera, portanto, para comandos que dependem de I/O, o tempo pode ser maior do que o esperado.