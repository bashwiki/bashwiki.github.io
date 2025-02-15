# [리눅스] Bash renice 사용법

## Visão Geral
O comando `renice` é utilizado no sistema operacional Linux para alterar a prioridade de execução de processos em execução. A prioridade de um processo determina a quantidade de tempo de CPU que ele pode receber em comparação com outros processos. Um valor de prioridade mais baixo indica uma prioridade mais alta, enquanto um valor mais alto indica uma prioridade mais baixa. O principal objetivo do `renice` é permitir que administradores e usuários ajustem a prioridade de processos em execução, ajudando a gerenciar o desempenho do sistema.

## Uso
A sintaxe básica do comando `renice` é a seguinte:

```bash
renice [opções] prioridade -p PID
```

### Opções Comuns:
- `prioridade`: Um número que representa a nova prioridade que você deseja atribuir ao processo. Os valores podem variar de -20 (máxima prioridade) a 19 (mínima prioridade).
- `-p PID`: Especifica o ID do processo (PID) que você deseja alterar a prioridade.
- `-g GID`: Altera a prioridade de todos os processos pertencentes ao grupo de identificação especificado.
- `-u UID`: Altera a prioridade de todos os processos pertencentes ao usuário especificado.

## Exemplos

### Exemplo 1: Alterar a prioridade de um processo específico
Para alterar a prioridade de um processo com o PID 1234 para 10, você pode usar o seguinte comando:

```bash
renice 10 -p 1234
```

### Exemplo 2: Alterar a prioridade de todos os processos de um usuário
Para alterar a prioridade de todos os processos pertencentes ao usuário "joao" para 5, você pode usar:

```bash
renice 5 -u joao
```

## Dicas
- Use o comando `ps` para encontrar o PID dos processos que você deseja ajustar. Por exemplo, `ps aux | grep nome_do_processo`.
- Tenha cuidado ao definir prioridades muito altas para processos críticos, pois isso pode afetar negativamente o desempenho do sistema.
- Apenas o usuário root ou o proprietário do processo pode aumentar a prioridade de um processo (ou seja, definir um valor menor que o atual).
- Verifique a prioridade atual de um processo usando o comando `top` ou `htop`, que mostram as prioridades de todos os processos em execução.

Com essas informações, você deve estar apto a utilizar o comando `renice` para gerenciar as prioridades de processos no seu sistema Linux de forma eficaz.