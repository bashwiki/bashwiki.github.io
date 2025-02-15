# [리눅스] Bash disown 사용법

## Overview
O comando `disown` no Bash é utilizado para remover um ou mais jobs da lista de jobs do shell, permitindo que esses jobs continuem a ser executados em segundo plano mesmo após o shell ser encerrado. Isso é especialmente útil quando você inicia um processo em segundo plano e deseja garantir que ele não seja interrompido quando você sair da sessão do terminal.

## Usage
A sintaxe básica do comando `disown` é a seguinte:

```bash
disown [opções] [job_spec]
```

### Opções Comuns:
- `-h`: Esta opção impede que o job especificado receba um sinal SIGHUP quando o shell é encerrado.
- `-a`: Aplica o comando a todos os jobs em segundo plano.
- `-r`: Aplica o comando apenas aos jobs que estão em execução.

Se você não especificar um `job_spec`, o `disown` irá aplicar-se ao job mais recente.

## Examples

### Exemplo 1: Desconectar um job específico
Suponha que você tenha iniciado um processo em segundo plano, como um servidor Python:

```bash
python -m http.server &
```

Você pode verificar os jobs em segundo plano com o comando `jobs`. Para desconectar este job específico, você pode usar:

```bash
disown %1
```

Aqui, `%1` refere-se ao primeiro job listado.

### Exemplo 2: Desconectar todos os jobs
Se você tiver vários jobs em segundo plano e quiser desconectar todos eles de uma vez, você pode usar a opção `-a`:

```bash
disown -a
```

Isso garantirá que todos os jobs em segundo plano continuem a ser executados mesmo após o encerramento do shell.

## Tips
- Sempre verifique a lista de jobs em segundo plano usando o comando `jobs` antes de usar `disown`, para garantir que você está desconectando o job correto.
- Use `disown -h` se você deseja que um job continue rodando mesmo após o shell ser encerrado, mas não quer que ele receba um sinal SIGHUP.
- Lembre-se de que uma vez que um job é desconectado, você não poderá mais trazê-lo de volta para o controle do shell. Portanto, use o `disown` com cautela.