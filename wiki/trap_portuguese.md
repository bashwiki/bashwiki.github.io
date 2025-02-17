# [Linux] Bash trap uso: Captura de sinais e execução de comandos

## Overview
O comando `trap` no Bash é utilizado para capturar sinais e executar comandos específicos quando esses sinais são recebidos. Isso é útil para gerenciar o comportamento de scripts em situações como interrupções ou saídas inesperadas.

## Usage
A sintaxe básica do comando `trap` é a seguinte:

```bash
trap [comando] [sinal]
```

## Common Options
Aqui estão algumas opções comuns para o comando `trap`:

- `SIGINT`: Captura a interrupção do terminal (Ctrl+C).
- `SIGTERM`: Captura o sinal de término.
- `EXIT`: Executa um comando quando o script termina, independentemente do motivo.

## Common Examples

### Exemplo 1: Capturar SIGINT
Este exemplo mostra como capturar a interrupção do terminal e executar um comando específico.

```bash
trap 'echo "Interrupção recebida!"' SIGINT
while true; do
    echo "Executando..."
    sleep 1
done
```

### Exemplo 2: Limpeza ao sair
Neste exemplo, o comando `trap` é usado para garantir que um diretório temporário seja removido quando o script termina.

```bash
trap 'rm -rf /tmp/meu_diretorio_temporario' EXIT
mkdir /tmp/meu_diretorio_temporario
# Outras operações...
```

### Exemplo 3: Capturar SIGTERM
Aqui, o script captura o sinal de término e executa uma mensagem antes de sair.

```bash
trap 'echo "Sinal de término recebido. Saindo..."' SIGTERM
while true; do
    echo "Executando..."
    sleep 1
done
```

## Tips
- Utilize `trap` para garantir que recursos sejam liberados adequadamente ao final de um script.
- Sempre teste seu script em um ambiente seguro antes de usá-lo em produção, especialmente ao usar `trap` com comandos que alteram o sistema.
- Combine `trap` com outros comandos para criar scripts mais robustos e responsivos a eventos do sistema.