# [리눅스] Bash pushd 사용법

## Overview
O comando `pushd` é utilizado no Bash para alterar o diretório atual e, ao mesmo tempo, armazenar o diretório anterior em uma pilha. Isso permite que os usuários naveguem facilmente entre diretórios, podendo retornar ao diretório anterior com o comando `popd`. O principal propósito do `pushd` é facilitar a navegação em múltiplos diretórios sem perder o histórico de diretórios visitados.

## Usage
A sintaxe básica do comando `pushd` é a seguinte:

```bash
pushd [diretório]
```

### Opções Comuns
- `-n`: Não altera o diretório atual, apenas modifica a pilha de diretórios.
- `+n`: Acessa o n-ésimo diretório na pilha, onde n é um número inteiro que representa a posição na pilha (começando em 0).
- `-n`: Acessa o n-ésimo diretório na pilha, mas na ordem inversa.

## Examples
### Exemplo 1: Navegando entre diretórios
```bash
pushd /home/usuario/projetos
```
Neste exemplo, o diretório atual é alterado para `/home/usuario/projetos`, e o diretório anterior é armazenado na pilha.

### Exemplo 2: Retornando ao diretório anterior
```bash
pushd /var/log
popd
```
Aqui, o comando `pushd` muda para o diretório `/var/log`, e o comando `popd` retorna ao diretório anterior que foi armazenado na pilha.

## Tips
- Utilize `dirs` para visualizar a pilha de diretórios atual. Isso pode ajudar a entender onde você está e quais diretórios você pode acessar.
- Combine `pushd` e `popd` para criar scripts que navegam automaticamente por diretórios, facilitando tarefas repetitivas.
- Lembre-se de que a pilha de diretórios é limitada à sessão do terminal, então, ao fechar o terminal, a pilha será perdida.