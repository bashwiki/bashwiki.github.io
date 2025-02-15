# [리눅스] Bash jobs 사용법

## Overview
O comando `jobs` no Bash é utilizado para listar os trabalhos em segundo plano e em execução no shell atual. Ele permite que os usuários visualizem o estado dos processos que foram iniciados a partir do terminal, mostrando se estão em execução, suspensos ou finalizados. Isso é especialmente útil para gerenciar múltiplos processos sem a necessidade de abrir novas janelas de terminal.

## Usage
A sintaxe básica do comando `jobs` é a seguinte:

```bash
jobs [opções]
```

As opções mais comuns incluem:

- `-l`: Exibe o número do processo (PID) ao lado de cada trabalho listado.
- `-n`: Mostra apenas os trabalhos que mudaram de estado desde a última execução do comando.
- `-p`: Exibe apenas os IDs dos processos dos trabalhos.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `jobs`.

### Exemplo 1: Listar trabalhos em execução
Para listar todos os trabalhos em execução e suspensos no shell atual, basta digitar:

```bash
jobs
```

A saída pode ser algo como:

```
[1]+  12345 Running                 ./script.sh &
[2]-  12346 Stopped                 ./another_script.sh
```

### Exemplo 2: Listar trabalhos com PID
Para obter uma lista dos trabalhos em execução junto com seus IDs de processo, use a opção `-l`:

```bash
jobs -l
```

A saída pode ser:

```
[1]+  12345 Running                 ./script.sh &
[2]-  12346 Stopped                 ./another_script.sh
```

## Tips
- Utilize o comando `bg` para retomar um trabalho suspenso em segundo plano após visualizá-lo com `jobs`.
- Use `fg` seguido do número do trabalho para trazer um trabalho em segundo plano de volta para o primeiro plano.
- Lembre-se de que o comando `jobs` só mostra os trabalhos iniciados no shell atual. Se você abrir um novo terminal, não verá os trabalhos do terminal anterior.
- Para gerenciar eficientemente seus trabalhos, combine o uso do `jobs` com `bg` e `fg` para alternar entre diferentes estados de execução.

Com essas informações, você pode utilizar o comando `jobs` de forma eficaz para gerenciar seus processos em Bash.