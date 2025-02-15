# [리눅스] Bash fg 사용법

## Overview
O comando `fg` no Bash é utilizado para trazer um processo em segundo plano para o primeiro plano. Isso é especialmente útil quando você tem um processo em execução que foi enviado para o fundo (usando `&` ou `Ctrl + Z` seguido de `bg`) e deseja interagir com ele novamente. O `fg` permite que você retome a execução do processo, permitindo que ele receba a entrada do terminal.

## Usage
A sintaxe básica do comando `fg` é a seguinte:

```bash
fg [job_spec]
```

- `job_spec`: Este parâmetro é opcional e pode ser usado para especificar qual trabalho você deseja trazer para o primeiro plano. Se não for especificado, o `fg` trará o último trabalho em segundo plano.

### Opções Comuns
- `%n`: Refere-se ao trabalho com o número `n`, que pode ser encontrado usando o comando `jobs`.
- `%-`: Refere-se ao último trabalho que foi colocado em segundo plano.

## Examples
### Exemplo 1: Retomar o último trabalho em segundo plano
Se você tiver um trabalho em segundo plano, como um editor de texto, você pode trazê-lo de volta ao primeiro plano com:

```bash
fg
```

### Exemplo 2: Retomar um trabalho específico
Se você tiver vários trabalhos em segundo plano e quiser retomar um específico, primeiro você pode listar os trabalhos em segundo plano:

```bash
jobs
```

Suponha que você veja uma saída como esta:

```
[1]+  12345 Stopped                 nano
[2]-  12346 Running                 sleep 100 &
```

Para trazer o trabalho `nano` (que é o trabalho 1) de volta ao primeiro plano, você usaria:

```bash
fg %1
```

## Tips
- Sempre verifique os trabalhos em segundo plano com o comando `jobs` antes de usar `fg`, para garantir que você está trazendo o trabalho correto para o primeiro plano.
- Se você frequentemente alterna entre vários processos, considere usar `bg` para continuar a execução de um trabalho em segundo plano enquanto você trabalha em outro.
- Lembre-se de que, ao trazer um trabalho para o primeiro plano, ele pode interromper a execução de outros processos que você estava utilizando no terminal.