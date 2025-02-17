# [Linux] Bash tee Uso equivalente: redirecionar a saída para um ou mais arquivos

O comando `tee` é utilizado para ler da entrada padrão e gravar tanto na saída padrão quanto em um ou mais arquivos, permitindo que você visualize a saída enquanto a grava.

## Overview
O comando `tee` é uma ferramenta útil no Bash que permite dividir a saída de um comando, enviando-a para a tela e para um arquivo simultaneamente. Isso é especialmente prático quando você deseja monitorar a saída de um comando enquanto a armazena para uso posterior.

## Usage
A sintaxe básica do comando `tee` é a seguinte:

```bash
tee [opções] [arquivos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `tee`:

- `-a` ou `--append`: Adiciona a saída ao final do arquivo em vez de sobrescrevê-lo.
- `-i` ou `--ignore-interrupts`: Ignora sinais de interrupção.
- `--help`: Exibe uma mensagem de ajuda com informações sobre o uso do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `tee`:

1. **Gravar a saída de um comando em um arquivo:**

```bash
echo "Olá, mundo!" | tee arquivo.txt
```

Esse comando grava "Olá, mundo!" no arquivo `arquivo.txt` e também exibe a mensagem no terminal.

2. **Adicionar a saída a um arquivo existente:**

```bash
echo "Nova linha" | tee -a arquivo.txt
```

Neste caso, "Nova linha" será adicionada ao final de `arquivo.txt`, mantendo o conteúdo existente.

3. **Usar com outros comandos:**

```bash
ls -l | tee lista.txt
```

Esse comando lista os arquivos no diretório atual, exibindo a saída no terminal e gravando-a em `lista.txt`.

4. **Ignorar interrupções:**

```bash
some_command | tee -i output.txt
```

Aqui, `some_command` é executado e a saída é gravada em `output.txt`, ignorando sinais de interrupção.

## Tips
- Utilize a opção `-a` se precisar adicionar informações a um arquivo sem perder dados existentes.
- Combine `tee` com outros comandos para criar pipelines eficientes, permitindo que você monitore e armazene saídas ao mesmo tempo.
- Lembre-se de que `tee` pode ser usado em scripts para registrar logs de execução de comandos, facilitando a depuração posteriormente.