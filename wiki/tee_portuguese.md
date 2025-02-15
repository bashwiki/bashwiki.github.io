# [리눅스] Bash tee 사용법

## Overview
O comando `tee` é uma ferramenta do Bash que permite ler da entrada padrão e gravar simultaneamente em um ou mais arquivos. É especialmente útil em situações onde você deseja visualizar a saída de um comando no terminal enquanto a grava em um arquivo. O nome "tee" vem da forma como o comando divide a saída, semelhante a uma bifurcação em um tubo em forma de "T".

## Usage
A sintaxe básica do comando `tee` é a seguinte:

```bash
tee [opções] [arquivo...]
```

### Opções Comuns:
- `-a`, `--append`: Adiciona a saída ao final do arquivo em vez de sobrescrevê-lo.
- `-i`, `--ignore-interrupts`: Ignora sinais de interrupção.
- `-p`, `--output-error`: Controla o que fazer em caso de erro ao gravar em um arquivo.

## Examples
### Exemplo 1: Gravar a saída de um comando em um arquivo
```bash
echo "Olá, mundo!" | tee arquivo.txt
```
Neste exemplo, a string "Olá, mundo!" é exibida no terminal e também gravada no arquivo `arquivo.txt`. Se o arquivo não existir, ele será criado.

### Exemplo 2: Adicionar saída a um arquivo existente
```bash
echo "Nova linha" | tee -a arquivo.txt
```
Aqui, a string "Nova linha" é adicionada ao final do arquivo `arquivo.txt` sem apagar o conteúdo existente, graças à opção `-a`.

## Tips
- Utilize `tee` em combinação com outros comandos para registrar logs ou saídas de processos longos. Por exemplo:
  ```bash
  long_running_command | tee log.txt
  ```
- Para evitar a sobrescrição acidental de arquivos importantes, sempre verifique se você está usando a opção `-a` quando necessário.
- O comando `tee` pode ser usado em scripts para monitorar a saída de comandos enquanto os registra, facilitando a depuração e a análise posterior.