# [리눅스] Bash pwd 사용법

## Overview
O comando `pwd` (print working directory) é uma ferramenta fundamental no Bash que exibe o diretório de trabalho atual do usuário. Ele é amplamente utilizado por engenheiros e desenvolvedores para verificar rapidamente em qual diretório estão trabalhando dentro do sistema de arquivos. Isso é especialmente útil ao navegar por múltiplos diretórios ou ao executar scripts que dependem de caminhos específicos.

## Usage
A sintaxe básica do comando `pwd` é bastante simples:

```bash
pwd [opções]
```

### Opções Comuns
- `-L`: Esta opção exibe o caminho lógico do diretório atual. É a opção padrão e mostra o caminho que o usuário vê, mesmo que o diretório seja um link simbólico.
- `-P`: Esta opção exibe o caminho físico do diretório atual, resolvendo todos os links simbólicos e mostrando o caminho real no sistema de arquivos.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `pwd`:

1. **Exibir o diretório atual**:
   ```bash
   pwd
   ```
   Saída esperada:
   ```
   /home/usuario/projetos
   ```

2. **Exibir o caminho físico do diretório atual**:
   ```bash
   pwd -P
   ```
   Saída esperada (caso haja links simbólicos):
   ```
   /mnt/disk1/home/usuario/projetos
   ```

## Tips
- Utilize `pwd` frequentemente ao trabalhar em scripts para garantir que você está no diretório correto antes de executar comandos que dependem de caminhos específicos.
- Combine `pwd` com outros comandos, como `cd`, para criar scripts que mudam de diretório e registram o caminho atual, facilitando o rastreamento do fluxo de trabalho.
- Lembre-se de que o uso da opção `-P` pode ser útil em ambientes onde links simbólicos são comuns, pois ajuda a evitar confusões sobre o caminho real do diretório.