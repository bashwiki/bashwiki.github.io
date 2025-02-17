# [Linux] Bash ss uso equivalente: Exibir informações sobre conexões de rede

## Overview
O comando `ss` é uma ferramenta poderosa utilizada para investigar conexões de rede em sistemas Linux. Ele fornece informações detalhadas sobre sockets, permitindo que os usuários visualizem conexões TCP, UDP, e muito mais, de forma rápida e eficiente.

## Usage
A sintaxe básica do comando `ss` é a seguinte:

```bash
ss [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `ss`:

- `-t`: Exibe apenas conexões TCP.
- `-u`: Exibe apenas conexões UDP.
- `-l`: Mostra apenas sockets que estão escutando.
- `-p`: Mostra o processo associado a cada socket.
- `-n`: Exibe endereços e números de porta em formato numérico, evitando a resolução de nomes.

## Common Examples

### Exibir todas as conexões
Para listar todas as conexões de rede ativas, use:

```bash
ss -a
```

### Exibir conexões TCP
Para visualizar apenas as conexões TCP, execute:

```bash
ss -t
```

### Exibir conexões UDP
Para listar as conexões UDP, utilize:

```bash
ss -u
```

### Exibir sockets em escuta
Para mostrar apenas os sockets que estão escutando, use:

```bash
ss -l
```

### Exibir processos associados
Para ver quais processos estão associados a cada socket, execute:

```bash
ss -p
```

### Exibir informações em formato numérico
Para evitar a resolução de nomes e mostrar endereços e portas como números, utilize:

```bash
ss -n
```

## Tips
- Utilize a opção `-tuln` para obter uma visão abrangente das conexões TCP e UDP que estão escutando, sem resolução de nomes.
- Combine opções para filtrar resultados de forma mais eficaz, como `ss -tunlp` para ver todos os sockets TCP e UDP em escuta com informações de processo.
- O `ss` é mais rápido e fornece mais informações do que o comando `netstat`, tornando-se uma escolha preferida para administradores de sistema.