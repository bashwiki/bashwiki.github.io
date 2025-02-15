# [리눅스] Bash popd 사용법

## Overview
O comando `popd` é utilizado no Bash para remover diretórios do topo da pilha de diretórios. Ele é frequentemente utilizado em conjunto com o comando `pushd`, que adiciona diretórios à pilha. O principal propósito do `popd` é facilitar a navegação entre diretórios, permitindo que os usuários retornem rapidamente ao diretório anterior que foi armazenado na pilha.

## Usage
A sintaxe básica do comando `popd` é a seguinte:

```bash
popd [opções]
```

### Opções Comuns
- `+N`: Remove o diretório na posição N da pilha, onde N é um número que representa a posição do diretório na pilha (começando de 0).
- `-N`: Remove o diretório na posição N a partir do final da pilha.

Se nenhuma opção for fornecida, o `popd` remove o diretório que está no topo da pilha.

## Examples
### Exemplo 1: Usando popd sem opções
```bash
# Adicionando diretórios à pilha
pushd /home/usuario/projetos
pushd /home/usuario/documentos

# Retornando ao diretório anterior
popd
```
Neste exemplo, após executar `popd`, o diretório `/home/usuario/projetos` será o diretório atual, pois o diretório `/home/usuario/documentos` foi removido da pilha.

### Exemplo 2: Usando popd com a opção +
```bash
# Adicionando diretórios à pilha
pushd /home/usuario/projetos
pushd /home/usuario/documentos
pushd /home/usuario/imagens

# Removendo o segundo diretório da pilha
popd +1
```
Aqui, o diretório `/home/usuario/documentos` é removido da pilha, e o diretório `/home/usuario/imagens` se torna o diretório atual.

## Tips
- Utilize `dirs` para visualizar a pilha de diretórios antes de usar `popd`, isso pode ajudar a entender melhor a estrutura atual da pilha.
- Combine `pushd` e `popd` para criar scripts que navegam entre múltiplos diretórios de forma eficiente.
- Lembre-se de que a pilha de diretórios é uma estrutura LIFO (Last In, First Out), então o último diretório adicionado será o primeiro a ser removido com `popd`.