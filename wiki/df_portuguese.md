# [리눅스] Bash df 사용법

## Overview
O comando `df` (disk free) é uma ferramenta do sistema Linux que exibe informações sobre o espaço em disco disponível e utilizado em sistemas de arquivos montados. O principal objetivo do `df` é fornecer uma visão geral do uso do espaço em disco, permitindo que engenheiros e desenvolvedores monitorem a capacidade de armazenamento e tomem decisões informadas sobre gerenciamento de espaço.

## Usage
A sintaxe básica do comando `df` é a seguinte:

```
df [opções] [arquivo...]
```

### Opções Comuns:
- `-h`: Exibe os tamanhos em um formato legível por humanos (por exemplo, em KB, MB, GB).
- `-T`: Mostra o tipo de sistema de arquivos.
- `-a`: Inclui sistemas de arquivos com 0 blocos.
- `-i`: Exibe informações sobre inodes em vez de blocos.

## Examples
### Exemplo 1: Exibir uso de disco em formato legível
Para ver o espaço em disco disponível e utilizado em um formato mais compreensível, você pode usar:

```bash
df -h
```

Este comando mostrará informações como o tamanho total, usado, disponível e o ponto de montagem de cada sistema de arquivos em uma forma que é fácil de ler.

### Exemplo 2: Exibir informações detalhadas do sistema de arquivos
Se você quiser saber o tipo de sistema de arquivos junto com o uso do disco, você pode usar:

```bash
df -hT
```

Este comando fornece uma tabela que inclui o tipo de sistema de arquivos, além das informações habituais de uso de disco.

## Tips
- Utilize a opção `-h` sempre que possível para facilitar a leitura das informações, especialmente em sistemas com grandes volumes de dados.
- Combine opções para obter relatórios mais detalhados e úteis. Por exemplo, `df -hT` é uma combinação prática que fornece tanto a legibilidade quanto o tipo de sistema de arquivos.
- Regularmente verifique o uso do disco em servidores para evitar problemas de espaço que podem afetar o desempenho e a operação do sistema.