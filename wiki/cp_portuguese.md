# [리눅스] Bash cp 사용법

## Overview
O comando `cp` no Bash é utilizado para copiar arquivos e diretórios. Seu propósito principal é permitir que os usuários façam cópias de arquivos de um local para outro, facilitando a duplicação de dados e a organização de arquivos no sistema de arquivos.

## Usage
A sintaxe básica do comando `cp` é a seguinte:

```bash
cp [opções] origem destino
```

### Opções Comuns:
- `-r` ou `--recursive`: Copia diretórios recursivamente. Necessário ao copiar diretórios.
- `-i` ou `--interactive`: Pergunta ao usuário antes de sobrescrever arquivos existentes.
- `-u` ou `--update`: Copia apenas se o arquivo de origem for mais recente que o arquivo de destino ou se o arquivo de destino não existir.
- `-v` ou `--verbose`: Exibe os detalhes da operação de cópia, mostrando quais arquivos estão sendo copiados.

## Examples
### Exemplo 1: Copiando um arquivo simples
Para copiar um arquivo chamado `documento.txt` para um novo arquivo chamado `copia_documento.txt`, você pode usar o seguinte comando:

```bash
cp documento.txt copia_documento.txt
```

### Exemplo 2: Copiando um diretório recursivamente
Para copiar um diretório chamado `projetos` e todo o seu conteúdo para um novo diretório chamado `copia_projetos`, utilize a opção `-r`:

```bash
cp -r projetos copia_projetos
```

## Tips
- Sempre use a opção `-i` se você estiver preocupado em sobrescrever arquivos existentes. Isso pode evitar a perda acidental de dados.
- Ao copiar arquivos para um diretório que já contém arquivos com o mesmo nome, considere usar a opção `-u` para garantir que apenas arquivos mais recentes sejam copiados.
- Utilize a opção `-v` para acompanhar o progresso da cópia, especialmente ao lidar com muitos arquivos ou diretórios grandes.