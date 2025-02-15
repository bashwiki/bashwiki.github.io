# [리눅스] Bash fc 사용법

## Overview
O comando `fc` é uma ferramenta do Bash que permite ao usuário editar e reexecutar comandos previamente digitados no shell. Ele é especialmente útil para corrigir erros em comandos anteriores ou para reutilizar comandos sem precisar digitá-los novamente. O `fc` pode abrir um editor de texto para que o usuário faça alterações nos comandos selecionados, facilitando a edição e a execução.

## Usage
A sintaxe básica do comando `fc` é a seguinte:

```bash
fc [opções] [número_inicial] [número_final]
```

### Comum opções:
- `-l`: Lista os comandos anteriores. Você pode especificar um intervalo de números para listar apenas um conjunto específico de comandos.
- `-e editor`: Especifica qual editor de texto usar para editar os comandos. O editor padrão é o definido pela variável de ambiente `EDITOR`.
- `-s`: Executa o comando sem abrir um editor, útil para correções rápidas.

## Examples
### Exemplo 1: Listar comandos anteriores
Para listar os últimos 10 comandos executados, você pode usar:

```bash
fc -l -10
```

### Exemplo 2: Editar um comando específico
Se você deseja editar o comando de número 25 na sua lista de comandos anteriores, você pode fazer:

```bash
fc 25
```

Isso abrirá o comando 25 no editor de texto padrão, permitindo que você faça as alterações necessárias antes de executá-lo novamente.

## Tips
- Utilize `fc -l` frequentemente para revisar seus comandos anteriores e aprender com erros passados.
- Configure a variável `EDITOR` para um editor de sua preferência, como `vim` ou `nano`, para facilitar a edição dos comandos.
- O uso da opção `-s` pode acelerar o processo de correção de comandos simples, permitindo que você execute rapidamente sem abrir um editor.

Com essas informações, você deve estar apto a utilizar o comando `fc` de forma eficaz em suas atividades diárias no Bash.