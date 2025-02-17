# [Linux] Bash pushd Uso: Navegação entre diretórios de forma eficiente

## Overview
O comando `pushd` é utilizado para alterar o diretório atual e, ao mesmo tempo, armazenar o diretório anterior em uma pilha. Isso permite que você navegue facilmente entre diretórios sem perder o caminho anterior.

## Usage
A sintaxe básica do comando `pushd` é a seguinte:

```bash
pushd [opções] [argumentos]
```

## Common Options
- `+N`: Muda para o diretório na posição N da pilha.
- `-`: Retorna ao diretório anterior na pilha.
- `--help`: Exibe a ajuda do comando.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `pushd`:

1. **Navegando para um diretório específico e armazenando o anterior:**
   ```bash
   pushd /caminho/para/diretorio
   ```

2. **Retornando ao diretório anterior:**
   ```bash
   pushd -
   ```

3. **Mudando para um diretório na posição 1 da pilha:**
   ```bash
   pushd +1
   ```

4. **Exibindo a pilha de diretórios:**
   ```bash
   dirs
   ```

## Tips
- Utilize `popd` para remover o diretório atual da pilha e retornar ao anterior.
- Combine `pushd` e `popd` para criar scripts que navegam entre diretórios de forma eficiente.
- Lembre-se de que a pilha de diretórios é uma estrutura LIFO (Last In, First Out), então o último diretório que você adicionou será o primeiro a ser removido.