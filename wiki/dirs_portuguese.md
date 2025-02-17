# [Linux] Bash dirs Uso: Exibir diretórios na pilha

## Overview
O comando `dirs` é utilizado no Bash para exibir a lista de diretórios que estão armazenados na pilha de diretórios. Essa pilha é manipulada por outros comandos como `pushd` e `popd`, permitindo que os usuários naveguem facilmente entre diretórios.

## Usage
A sintaxe básica do comando `dirs` é a seguinte:

```bash
dirs [opções] [argumentos]
```

## Common Options
- `-l`: Exibe a lista de diretórios em formato longo, mostrando o caminho completo.
- `-p`: Exibe a lista de diretórios em formato compacto, sem espaços extras.

## Common Examples

1. **Exibir a pilha de diretórios atual:**
   ```bash
   dirs
   ```

2. **Adicionar um diretório à pilha e exibir:**
   ```bash
   pushd /home/usuario
   dirs
   ```

3. **Exibir a pilha de diretórios em formato longo:**
   ```bash
   dirs -l
   ```

4. **Exibir a pilha de diretórios em formato compacto:**
   ```bash
   dirs -p
   ```

5. **Adicionar e depois exibir múltiplos diretórios:**
   ```bash
   pushd /var/log
   pushd /etc
   dirs
   ```

## Tips
- Utilize `pushd` e `popd` em conjunto com `dirs` para uma navegação eficiente entre diretórios.
- Lembre-se de que a pilha de diretórios é uma estrutura de dados LIFO (Last In, First Out), então o último diretório adicionado será o primeiro a ser removido.
- Experimente usar `dirs -l` para visualizar os caminhos completos, especialmente se você estiver trabalhando com diretórios aninhados.