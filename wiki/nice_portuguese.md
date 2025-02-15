# [리눅스] Bash nice 사용법

## Overview
O comando `nice` no Bash é utilizado para executar um programa com uma prioridade de agendamento alterada. O principal objetivo do `nice` é permitir que os usuários controlem a quantidade de recursos do sistema que um processo pode consumir, especialmente em ambientes multitarefa. Ao ajustar a prioridade, os usuários podem garantir que processos menos importantes não interfiram em tarefas críticas, melhorando assim a eficiência do sistema.

## Usage
A sintaxe básica do comando `nice` é a seguinte:

```bash
nice [opções] [comando]
```

### Opções Comuns:
- `-n, --adjustment=N`: Especifica o valor de ajuste da prioridade. O valor padrão é 10. Valores negativos aumentam a prioridade do processo, enquanto valores positivos a diminuem.
- `-h, --help`: Exibe a ajuda sobre o comando.
- `--version`: Mostra a versão do `nice`.

Por exemplo, para executar um comando com uma prioridade mais baixa, você pode usar:

```bash
nice -n 19 comando
```

## Examples
### Exemplo 1: Executar um script com prioridade baixa
Se você deseja executar um script chamado `backup.sh` com prioridade baixa, você pode usar o seguinte comando:

```bash
nice -n 19 ./backup.sh
```

Neste exemplo, o script `backup.sh` será executado com a menor prioridade, permitindo que outros processos mais importantes tenham mais acesso aos recursos do sistema.

### Exemplo 2: Executar um comando com prioridade alta
Para executar um comando com prioridade alta, como o `make`, você pode usar:

```bash
nice -n -5 make
```

Aqui, o comando `make` será executado com uma prioridade maior, o que pode ser útil se você deseja que a compilação ocorra mais rapidamente em relação a outros processos em execução.

## Tips
- Use o `nice` em conjunto com o comando `renice` para ajustar a prioridade de processos já em execução.
- Lembre-se de que apenas usuários com permissões adequadas podem aumentar a prioridade de um processo (valores negativos).
- Ao usar `nice`, é uma boa prática monitorar o uso de recursos do sistema para garantir que o desempenho geral não seja afetado.
- Utilize o comando `top` ou `htop` para visualizar as prioridades dos processos em tempo real e ajustar conforme necessário.