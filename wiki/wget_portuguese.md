# [리눅스] Bash wget 사용법

## Overview
O `wget` é uma ferramenta de linha de comando utilizada para baixar arquivos da web. Ele suporta protocolos como HTTP, HTTPS e FTP, permitindo que os usuários façam downloads de arquivos de forma simples e eficiente. O principal propósito do `wget` é facilitar o download de conteúdo da internet, seja para uso pessoal, desenvolvimento ou automação de tarefas.

## Usage
A sintaxe básica do comando `wget` é a seguinte:

```bash
wget [opções] [URL]
```

### Opções Comuns
- `-O <arquivo>`: Especifica o nome do arquivo de saída.
- `-c`: Continua um download interrompido.
- `-q`: Executa o comando em modo silencioso, sem exibir mensagens.
- `--limit-rate=<taxa>`: Limita a taxa de download a um valor específico.
- `-r`: Ativa o download recursivo, permitindo baixar diretórios inteiros.

## Examples
### Exemplo 1: Baixando um arquivo simples
Para baixar um arquivo de uma URL específica e salvá-lo com o nome padrão:

```bash
wget https://example.com/arquivo.zip
```

### Exemplo 2: Continuando um download interrompido
Se um download foi interrompido, você pode continuar de onde parou usando a opção `-c`:

```bash
wget -c https://example.com/arquivo.zip
```

## Tips
- Utilize a opção `-q` para downloads em scripts, evitando a poluição do terminal com mensagens desnecessárias.
- Quando baixar arquivos grandes ou muitos arquivos, considere usar `--limit-rate` para não sobrecarregar sua conexão de internet.
- Para downloads recursivos, tenha cuidado com a profundidade do download e o número de arquivos, pois isso pode resultar em downloads indesejados. Use `-r -l <nível>` para limitar a profundidade.

Com essas informações, você pode começar a usar o `wget` de forma eficaz em seus projetos e tarefas diárias.