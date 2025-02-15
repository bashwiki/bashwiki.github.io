# [리눅스] Bash trap 사용법

## Overview
O comando `trap` no Bash é utilizado para especificar comandos que devem ser executados quando o script recebe sinais específicos ou quando ocorre uma condição de erro. Ele é especialmente útil para garantir que certos procedimentos de limpeza ou finalização sejam realizados, mesmo que o script seja interrompido de forma inesperada. Isso pode incluir a liberação de recursos, a remoção de arquivos temporários ou a exibição de mensagens de erro.

## Usage
A sintaxe básica do comando `trap` é a seguinte:

```bash
trap COMMAND SIGNAL
```

- `COMMAND`: O comando ou conjunto de comandos que você deseja executar quando o sinal especificado for recebido.
- `SIGNAL`: O sinal que deve acionar a execução do comando. Os sinais podem ser especificados pelo nome (como `SIGINT`, `SIGTERM`, etc.) ou pelo número do sinal.

### Sinais Comuns
Aqui estão alguns sinais comuns que podem ser usados com o `trap`:

- `SIGINT`: Interrupção (geralmente gerada pelo Ctrl+C).
- `SIGTERM`: Solicitação de término.
- `EXIT`: Executa o comando quando o script termina, independentemente do motivo.

## Examples
### Exemplo 1: Capturando SIGINT
Neste exemplo, vamos capturar o sinal `SIGINT` e exibir uma mensagem antes de sair do script.

```bash
#!/bin/bash

trap 'echo "Script interrompido. Saindo..."; exit' SIGINT

while true; do
    echo "Executando... Pressione Ctrl+C para interromper."
    sleep 1
done
```

### Exemplo 2: Limpeza ao sair
Neste exemplo, utilizamos o `trap` para garantir que um arquivo temporário seja removido quando o script é encerrado.

```bash
#!/bin/bash

temp_file="/tmp/meu_arquivo_temp.txt"
trap 'rm -f "$temp_file"; echo "Arquivo temporário removido."' EXIT

echo "Criando arquivo temporário..."
touch "$temp_file"

# Simulando algum processamento
sleep 5

echo "Processo concluído."
```

## Tips
- Sempre que possível, use `trap` para gerenciar a limpeza de recursos, especialmente em scripts que criam arquivos temporários ou abrem conexões de rede.
- Teste seu script para garantir que o `trap` funcione como esperado em diferentes cenários de interrupção.
- Utilize `trap` com o sinal `EXIT` para garantir que a limpeza ocorra independentemente da forma como o script termina, seja por erro ou por finalização normal.