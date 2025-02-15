# [리눅스] Bash vmstat 사용법

## Overview
O comando `vmstat` (Virtual Memory Statistics) é uma ferramenta de monitoramento de desempenho no Linux que fornece informações sobre processos, memória, troca, I/O e CPU. Ele é útil para engenheiros e desenvolvedores que desejam analisar o desempenho do sistema e identificar gargalos. O `vmstat` coleta dados do sistema e os apresenta em um formato tabular, permitindo que os usuários visualizem rapidamente o estado atual do sistema.

## Usage
A sintaxe básica do comando `vmstat` é a seguinte:

```bash
vmstat [opções] [intervalo] [contagem]
```

- **opções**: Parâmetros que modificam o comportamento do comando.
- **intervalo**: O tempo em segundos entre as atualizações das estatísticas.
- **contagem**: O número de vezes que as estatísticas devem ser exibidas.

### Opções Comuns
- `-a`: Exibe informações sobre memória ativa e inativa.
- `-m`: Mostra estatísticas de memória de página.
- `-s`: Exibe um resumo das estatísticas de memória.
- `-d`: Mostra estatísticas de disco.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `vmstat`.

### Exemplo 1: Monitorar o sistema a cada 2 segundos
```bash
vmstat 2
```
Este comando exibirá as estatísticas do sistema a cada 2 segundos até que o usuário interrompa o processo (geralmente com `Ctrl+C`).

### Exemplo 2: Exibir estatísticas a cada 5 segundos, 10 vezes
```bash
vmstat 5 10
```
Neste exemplo, o `vmstat` irá mostrar as estatísticas do sistema a cada 5 segundos, totalizando 10 atualizações.

## Tips
- Utilize o `vmstat` em conjunto com outras ferramentas de monitoramento, como `top` ou `iostat`, para obter uma visão mais abrangente do desempenho do sistema.
- Para uma análise mais detalhada, combine o uso do `vmstat` com a opção `-a` para obter informações sobre a memória ativa e inativa.
- Salve a saída do `vmstat` em um arquivo para análise posterior, utilizando a redireção:
  ```bash
  vmstat 2 > vmstat_output.txt
  ```
- Fique atento a valores anormais, como altas taxas de troca, que podem indicar que o sistema está ficando sem memória e pode estar sofrendo degradação de desempenho.