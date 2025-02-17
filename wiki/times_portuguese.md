# [Linux] Bash times em português: Exibe o tempo de execução de processos

## Overview
O comando `times` no Bash é utilizado para exibir o tempo de CPU consumido pelos processos em segundo plano do shell atual. Ele fornece informações sobre o tempo total gasto em execução, incluindo o tempo de usuário e o tempo de sistema.

## Usage
A sintaxe básica do comando é a seguinte:

```bash
times [opções] [argumentos]
```

## Common Options
O comando `times` não possui muitas opções, mas aqui estão algumas que podem ser úteis:

- **-p**: Exibe os tempos em um formato mais legível, semelhante ao comando `printf`.

## Common Examples

### Exibir tempos de execução
Para simplesmente exibir os tempos de execução dos processos em segundo plano, você pode usar:

```bash
times
```

### Usar com o formato legível
Para exibir os tempos em um formato mais legível, utilize a opção `-p`:

```bash
times -p
```

### Comparar tempos antes e depois de um comando
Você pode usar o comando `times` para comparar o tempo de execução de um comando específico. Por exemplo:

```bash
sleep 2; times
```

Isso executará o comando `sleep` por 2 segundos e, em seguida, exibirá os tempos de CPU utilizados.

## Tips
- Utilize o comando `times` após a execução de scripts ou comandos longos para entender melhor o tempo de CPU que eles consumiram.
- Combine o `times` com outros comandos para monitorar o desempenho de tarefas específicas em scripts.
- Lembre-se de que o `times` só mostrará informações sobre os processos que foram executados no shell atual. Para processos em outros shells, você precisará executar o comando dentro daquele shell.