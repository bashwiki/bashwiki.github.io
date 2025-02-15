# [리눅스] Bash times 사용법

## Overview
O comando `times` no Bash é utilizado para exibir o tempo de CPU consumido pelo shell atual e por todos os processos filhos que foram iniciados a partir dele. Ele fornece uma visão geral do tempo de execução, permitindo que engenheiros e desenvolvedores monitorem o desempenho de seus scripts e processos. O principal propósito do comando é ajudar na análise de desempenho, especialmente em ambientes onde a eficiência do código é crítica.

## Usage
A sintaxe básica do comando `times` é bastante simples:

```bash
times
```

Quando executado, ele não aceita opções ou argumentos adicionais. O comando simplesmente retorna o tempo de CPU utilizado em três categorias:

- **Usuário**: O tempo de CPU gasto em processos do usuário.
- **Sistema**: O tempo de CPU gasto em processos do sistema.
- **Total**: O tempo total de CPU utilizado.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `times`.

### Exemplo 1: Uso básico
Para ver o tempo de CPU consumido pelo shell atual e seus processos filhos, basta digitar:

```bash
times
```

A saída será algo como:

```
   0m0.123s  0m0.456s  0m0.579s
```

Aqui, você verá os tempos de CPU em minutos e segundos para as categorias mencionadas.

### Exemplo 2: Comparando tempos antes e depois de um comando
Você pode usar `times` para medir o tempo de execução de um comando específico. Por exemplo, se você quiser medir o tempo de execução de um script chamado `meu_script.sh`, você pode fazer o seguinte:

```bash
bash meu_script.sh
times
```

Após a execução do script, o comando `times` mostrará o tempo total de CPU utilizado durante a execução do script.

## Tips
- Utilize o comando `times` após a execução de scripts ou comandos que você suspeita que possam estar consumindo muitos recursos. Isso ajudará a identificar gargalos de desempenho.
- O comando `times` é mais útil em scripts e ambientes de desenvolvimento onde o desempenho é uma preocupação. Considere integrá-lo em seus scripts para monitorar o uso de CPU automaticamente.
- Lembre-se de que `times` mostra apenas o tempo de CPU, e não o tempo real de execução. Para medir o tempo total de execução, você pode usar o comando `time`.

Com essas informações, você deve estar apto a utilizar o comando `times` para monitorar e otimizar o desempenho de seus scripts e processos no Bash.