# [리눅스] Bash builtin 사용법

## Overview
O comando `builtin` no Bash é utilizado para invocar comandos internos do shell, que são normalmente executados diretamente pelo Bash, em vez de serem executados como programas externos. O principal propósito do comando `builtin` é permitir que os usuários chamem explicitamente esses comandos internos, mesmo que haja um programa externo com o mesmo nome no caminho do sistema.

## Usage
A sintaxe básica do comando `builtin` é a seguinte:

```bash
builtin comando [argumentos]
```

### Opções Comuns
- `comando`: O nome do comando interno que você deseja executar.
- `argumentos`: Qualquer argumento que você queira passar para o comando.

## Examples
### Exemplo 1: Usando `builtin` para chamar `echo`
Suponha que você tenha um script que redefine o comando `echo`. Você pode usar `builtin` para garantir que o comando interno do Bash seja chamado:

```bash
#!/bin/bash

echo() {
    echo "Este é um comando echo redefinido."
}

# Chama o comando interno echo
builtin echo "Este é o comando echo interno."
```

### Exemplo 2: Usando `builtin` com `exit`
Você pode usar `builtin` para chamar o comando interno `exit`, mesmo que tenha um script que redefine o comportamento de saída:

```bash
#!/bin/bash

exit() {
    echo "Saindo do script."
}

# Chama o comando interno exit
builtin exit 0
```

## Tips
- Utilize `builtin` quando precisar garantir que você está chamando a versão interna do comando, especialmente se houver conflitos com comandos externos.
- É uma boa prática usar `builtin` em scripts complexos onde a redefinição de comandos pode causar confusão ou comportamento inesperado.
- Lembre-se de que nem todos os comandos têm uma versão interna; verifique a documentação do Bash para saber quais comandos são builtins.