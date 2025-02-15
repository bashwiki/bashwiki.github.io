# [리눅스] Bash mkfifo 사용법

## Overview
O comando `mkfifo` é utilizado no sistema operacional Linux para criar um arquivo FIFO (First In, First Out), que é um tipo especial de arquivo que permite a comunicação entre processos. Os arquivos FIFO são utilizados para permitir que um processo escreva dados que podem ser lidos por outro processo, facilitando a troca de informações de maneira ordenada.

## Usage
A sintaxe básica do comando `mkfifo` é a seguinte:

```bash
mkfifo [opções] nome_do_fifo
```

### Opções Comuns
- `-m, --mode=MODE`: Define as permissões do arquivo FIFO criado. O modo deve ser especificado em formato octal (por exemplo, `0666`).
- `--help`: Exibe uma mensagem de ajuda com informações sobre o uso do comando.
- `--version`: Mostra a versão do `mkfifo` instalado.

## Examples
### Exemplo 1: Criando um arquivo FIFO simples
Para criar um arquivo FIFO chamado `meu_fifo`, você pode usar o seguinte comando:

```bash
mkfifo meu_fifo
```

Após a execução deste comando, um arquivo chamado `meu_fifo` será criado no diretório atual.

### Exemplo 2: Criando um arquivo FIFO com permissões específicas
Se você deseja criar um arquivo FIFO com permissões específicas, como `0666`, utilize a opção `-m`:

```bash
mkfifo -m 0666 meu_fifo
```

Isso garante que o arquivo FIFO tenha permissões de leitura e escrita para todos os usuários.

## Tips
- Sempre verifique se o arquivo FIFO já existe antes de tentar criá-lo, pois o `mkfifo` retornará um erro se o arquivo já estiver presente.
- Para testar a comunicação entre processos usando um FIFO, você pode usar comandos como `cat` ou `echo` em conjunto com o FIFO. Por exemplo, em um terminal, você pode usar `cat meu_fifo` para ler os dados e, em outro terminal, usar `echo "Olá, FIFO!" > meu_fifo` para enviar dados.
- Lembre-se de que os arquivos FIFO são bloqueantes: se um processo tenta ler de um FIFO e não há dados disponíveis, ele ficará bloqueado até que outro processo escreva dados nele.