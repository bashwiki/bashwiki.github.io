# [리눅스] Bash killall 사용법

## Visão Geral
O comando `killall` é utilizado no sistema operacional Linux para encerrar processos em execução com base no nome do processo. Diferente do comando `kill`, que encerra processos usando o ID do processo (PID), o `killall` permite que você finalize todos os processos que correspondem a um nome específico, tornando-o uma ferramenta útil para gerenciar múltiplas instâncias de um aplicativo ou serviço.

## Uso
A sintaxe básica do comando `killall` é a seguinte:

```bash
killall [opções] nome_do_processo
```

### Opções Comuns
- `-u nome_do_usuario`: Encerra apenas os processos pertencentes ao usuário especificado.
- `-i`: Solicita confirmação antes de encerrar cada processo.
- `-q`: Executa o comando em modo silencioso, sem mensagens de erro.
- `-s sinal`: Especifica o sinal a ser enviado para os processos. O sinal padrão é `TERM` (15), que solicita a finalização graciosa do processo.

## Exemplos
### Exemplo 1: Encerrar todos os processos de um aplicativo
Se você deseja encerrar todos os processos do Firefox, você pode usar o seguinte comando:

```bash
killall firefox
```

### Exemplo 2: Encerrar processos de um usuário específico
Para encerrar todos os processos do usuário "joao", você pode usar:

```bash
killall -u joao
```

## Dicas
- Sempre tenha cuidado ao usar o `killall`, especialmente em sistemas de produção, pois encerrar processos inadvertidamente pode causar perda de dados ou instabilidade no sistema.
- Utilize a opção `-i` para evitar encerramentos acidentais, pois isso solicitará confirmação antes de cada processo ser finalizado.
- Verifique os processos em execução com o comando `ps` ou `pgrep` antes de usar o `killall`, para garantir que você está encerrando os processos corretos.