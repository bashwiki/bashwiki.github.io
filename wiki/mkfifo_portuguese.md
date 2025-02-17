# [Linux] Bash mkfifo Uso: Criação de arquivos FIFO

## Overview
O comando `mkfifo` é utilizado para criar arquivos FIFO (First In, First Out) no sistema operacional Linux. Esses arquivos são usados para comunicação entre processos, permitindo que um processo escreva dados em um arquivo enquanto outro processo lê esses dados.

## Usage
A sintaxe básica do comando `mkfifo` é a seguinte:

```bash
mkfifo [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `mkfifo`:

- `-m, --mode=MODE`: Define as permissões do arquivo FIFO criado, onde `MODE` é especificado em formato octal.
- `--help`: Exibe uma mensagem de ajuda com informações sobre o comando.
- `--version`: Mostra a versão do comando `mkfifo`.

## Common Examples

### Exemplo 1: Criar um arquivo FIFO simples
```bash
mkfifo meu_fifo
```
Este comando cria um arquivo FIFO chamado `meu_fifo`.

### Exemplo 2: Criar um arquivo FIFO com permissões específicas
```bash
mkfifo -m 644 meu_fifo
```
Aqui, o arquivo FIFO `meu_fifo` é criado com permissões de leitura e escrita para o proprietário e apenas leitura para o grupo e outros.

### Exemplo 3: Usar um arquivo FIFO para comunicação entre processos
Para exemplificar a comunicação, você pode usar dois terminais. No primeiro terminal, execute:
```bash
cat > meu_fifo
```
No segundo terminal, execute:
```bash
cat meu_fifo
```
Agora, tudo que você digitar no primeiro terminal aparecerá no segundo.

## Tips
- Sempre verifique se o arquivo FIFO já existe antes de criar um novo, para evitar erros.
- Use permissões adequadas ao criar arquivos FIFO, especialmente em ambientes multiusuário.
- Lembre-se de que arquivos FIFO permanecem abertos até que todos os processos que os utilizam sejam finalizados.