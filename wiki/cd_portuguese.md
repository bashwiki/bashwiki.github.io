# [리눅스] Bash cd 사용법

## Overview
O comando `cd` (change directory) é uma das instruções mais fundamentais no Bash e em outros shells do Unix. Sua principal função é alterar o diretório de trabalho atual do terminal. Isso permite que os usuários naveguem entre diferentes pastas no sistema de arquivos, facilitando o acesso a arquivos e subdiretórios.

## Usage
A sintaxe básica do comando `cd` é a seguinte:

```bash
cd [opções] [diretório]
```

### Opções Comuns:
- `..`: Muda para o diretório pai do diretório atual.
- `-`: Retorna ao diretório anterior.
- `~`: Muda para o diretório home do usuário atual.

## Examples
### Exemplo 1: Navegando para um diretório específico
Para mudar para um diretório chamado "projetos", você pode usar:

```bash
cd projetos
```

### Exemplo 2: Voltando para o diretório pai
Se você estiver em um diretório e quiser voltar para o diretório pai, use:

```bash
cd ..
```

### Exemplo 3: Retornando ao diretório anterior
Se você quiser voltar ao diretório onde estava anteriormente, utilize:

```bash
cd -
```

## Tips
- Utilize `cd ~` para acessar rapidamente seu diretório home.
- Para verificar qual é o diretório atual, você pode usar o comando `pwd` (print working directory) após usar `cd`.
- Para facilitar a navegação, considere usar autocompletar pressionando a tecla `Tab` após digitar parte do nome do diretório. Isso pode economizar tempo e evitar erros de digitação.