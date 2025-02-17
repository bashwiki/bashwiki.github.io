# [Linux] Bash netstat Uso: Exibir conexões de rede e estatísticas

## Overview
O comando `netstat` é uma ferramenta de linha de comando que exibe informações sobre conexões de rede, tabelas de roteamento, estatísticas de interface e muito mais. Ele é útil para monitorar e diagnosticar problemas de rede em sistemas operacionais baseados em Unix.

## Usage
A sintaxe básica do comando `netstat` é a seguinte:

```bash
netstat [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `netstat`:

- `-a`: Exibe todas as conexões e escuta as portas.
- `-t`: Mostra apenas as conexões TCP.
- `-u`: Mostra apenas as conexões UDP.
- `-n`: Exibe endereços e números de porta em formato numérico, sem tentar resolver nomes.
- `-l`: Mostra apenas os sockets que estão escutando.
- `-p`: Exibe o PID e o nome do programa ao qual cada socket pertence.

## Common Examples

Aqui estão alguns exemplos práticos do uso do `netstat`:

1. **Exibir todas as conexões e portas em escuta:**

   ```bash
   netstat -a
   ```

2. **Mostrar apenas conexões TCP:**

   ```bash
   netstat -t
   ```

3. **Mostrar apenas conexões UDP:**

   ```bash
   netstat -u
   ```

4. **Exibir conexões em formato numérico:**

   ```bash
   netstat -n
   ```

5. **Mostrar apenas sockets que estão escutando:**

   ```bash
   netstat -l
   ```

6. **Exibir conexões com o PID do processo:**

   ```bash
   netstat -p
   ```

## Tips
- Utilize a opção `-n` para acelerar a execução do comando, evitando a resolução de nomes de host.
- Combine opções para obter informações mais detalhadas, como `netstat -tunlp` para ver todas as conexões TCP e UDP com detalhes do processo.
- Para uma visualização mais organizada, você pode canalizar a saída do `netstat` para o comando `less`:

  ```bash
  netstat -a | less
  ``` 

Essas dicas podem ajudar a otimizar o uso do `netstat` e facilitar a análise das informações de rede.