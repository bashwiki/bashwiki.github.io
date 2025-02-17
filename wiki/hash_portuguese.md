# [Linux] Bash hash uso: Armazenar e exibir comandos

## Overview
O comando `hash` no Bash é utilizado para gerenciar o cache de comandos executados. Ele armazena o caminho dos comandos que foram executados, permitindo que o shell os encontre mais rapidamente em execuções futuras.

## Usage
A sintaxe básica do comando `hash` é a seguinte:

```bash
hash [opções] [argumentos]
```

## Common Options
- `-r`: Limpa o cache de comandos armazenados.
- `-l`: Lista todos os comandos armazenados no cache.
- `-p`: Especifica um caminho para um comando, permitindo que você o adicione ao cache.

## Common Examples

### 1. Listar comandos armazenados
Para visualizar todos os comandos que estão atualmente no cache, você pode usar:

```bash
hash -l
```

### 2. Limpar o cache
Se você deseja remover todos os comandos armazenados no cache, execute:

```bash
hash -r
```

### 3. Adicionar um comando ao cache
Para adicionar um comando específico ao cache, você pode usar:

```bash
hash -p /usr/local/bin/meu_comando meu_comando
```

### 4. Verificar o caminho de um comando
Para verificar o caminho de um comando que já foi armazenado, você pode simplesmente usar:

```bash
hash meu_comando
```

## Tips
- Utilize `hash -r` após instalar novos programas para garantir que o cache esteja atualizado.
- O comando `hash` é especialmente útil em scripts onde a eficiência na execução de comandos é importante.
- Lembre-se de que o cache é específico para a sessão do shell; ao abrir um novo terminal, o cache será redefinido.