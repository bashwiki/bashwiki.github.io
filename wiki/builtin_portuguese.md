# [Linux] Bash builtin : Executa comandos internos do Bash

## Overview
O comando `builtin` no Bash é utilizado para executar comandos internos do shell, permitindo que você chame uma versão específica de um comando que é parte do próprio Bash, em vez de uma versão externa que pode estar disponível no sistema.

## Usage
A sintaxe básica do comando `builtin` é a seguinte:

```bash
builtin [opções] [argumentos]
```

## Common Options
- `-h`, `--help`: Exibe uma mensagem de ajuda sobre o comando `builtin`.
- `-v`, `--verbose`: Exibe informações detalhadas sobre a execução do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `builtin`:

### Exemplo 1: Usando `builtin` para chamar `echo`
```bash
builtin echo "Este é um comando interno do Bash."
```

### Exemplo 2: Usando `builtin` para chamar `cd`
```bash
builtin cd /home/usuario
```

### Exemplo 3: Verificando a versão do `type`
```bash
builtin type -a echo
```

## Tips
- Use `builtin` quando você precisar garantir que está chamando a versão interna de um comando, especialmente se houver um comando externo com o mesmo nome.
- É útil para depuração, permitindo que você veja como o Bash lida com comandos internos.
- Lembre-se de que nem todos os comandos têm uma versão interna; verifique a documentação do Bash para mais informações sobre quais comandos são suportados.