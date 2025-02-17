# [Linux] Bash pwd Uso equivalente: Exibir o diretório atual

## Overview
O comando `pwd` (print working directory) é utilizado no Bash para exibir o caminho completo do diretório de trabalho atual. É uma ferramenta essencial para navegação no sistema de arquivos, permitindo que os usuários saibam exatamente onde estão dentro da estrutura de diretórios.

## Usage
A sintaxe básica do comando `pwd` é a seguinte:

```bash
pwd [opções]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o comando `pwd`:

- `-L`: Exibe o caminho lógico do diretório atual, que pode incluir links simbólicos.
- `-P`: Exibe o caminho físico do diretório atual, resolvendo todos os links simbólicos.

## Common Examples
Aqui estão alguns exemplos práticos do uso do comando `pwd`:

1. **Exibir o diretório atual:**
   ```bash
   pwd
   ```

2. **Exibir o caminho lógico do diretório atual:**
   ```bash
   pwd -L
   ```

3. **Exibir o caminho físico do diretório atual:**
   ```bash
   pwd -P
   ```

## Tips
- Use `pwd` frequentemente para confirmar sua localização no sistema de arquivos, especialmente ao trabalhar em diretórios aninhados.
- Combine `pwd` com outros comandos, como `cd`, para garantir que você está mudando para o diretório correto.
- Lembre-se de que o uso da opção `-P` pode ser útil quando você está lidando com links simbólicos e precisa saber o caminho real.