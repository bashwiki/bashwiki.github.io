# [리눅스] Bash hash 사용법

## Overview
O comando `hash` no Bash é utilizado para gerenciar o cache de comandos executados. Ele armazena o caminho completo dos comandos que foram executados, permitindo que o shell encontre esses comandos mais rapidamente em execuções futuras. O principal propósito do comando `hash` é otimizar o desempenho do shell, evitando a necessidade de procurar o caminho de um comando toda vez que ele é chamado.

## Usage
A sintaxe básica do comando `hash` é a seguinte:

```bash
hash [opções] [comando]
```

### Opções Comuns:
- `-r`: Limpa o cache de comandos armazenados. Isso é útil se você instalou novos programas e deseja que o Bash reconheça os novos caminhos.
- `-l`: Lista todos os comandos armazenados no cache, mostrando os caminhos completos.

## Examples
### Exemplo 1: Listar comandos armazenados
Para ver quais comandos estão atualmente armazenados no cache, você pode usar:

```bash
hash -l
```

Este comando exibirá uma lista de todos os comandos que foram executados e seus respectivos caminhos.

### Exemplo 2: Limpar o cache
Se você deseja limpar o cache de comandos, pode usar:

```bash
hash -r
```

Após executar este comando, o Bash não terá mais informações sobre os comandos armazenados anteriormente, e precisará procurar novamente os caminhos na próxima vez que um comando for chamado.

## Tips
- Utilize `hash -r` após instalar novos programas ou fazer alterações no PATH para garantir que o Bash reconheça as novas localizações dos comandos.
- Lembre-se de que o cache é específico para a sessão do shell. Se você abrir um novo terminal, o cache será reiniciado.
- O uso do comando `hash` é especialmente útil em scripts ou em ambientes onde a eficiência é crucial, pois reduz o tempo de busca por comandos frequentemente utilizados.