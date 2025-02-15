# [리눅스] Bash netstat 사용법

## Overview
O comando `netstat` (Network Statistics) é uma ferramenta de linha de comando utilizada para exibir informações sobre conexões de rede, tabelas de roteamento, estatísticas de interface e muito mais. É amplamente utilizado por engenheiros e desenvolvedores para monitorar e diagnosticar problemas de rede, permitindo que os usuários vejam quais portas estão abertas, quais serviços estão escutando e quais conexões estão ativas.

## Usage
A sintaxe básica do comando `netstat` é a seguinte:

```bash
netstat [opções]
```

Algumas das opções mais comuns incluem:

- `-a`: Exibe todas as conexões e escuta as portas.
- `-t`: Mostra apenas as conexões TCP.
- `-u`: Mostra apenas as conexões UDP.
- `-n`: Exibe endereços e números de porta em formato numérico, evitando a resolução de nomes.
- `-l`: Exibe apenas as portas que estão em escuta.
- `-p`: Mostra o identificador do processo (PID) e o nome do programa que está usando a conexão.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `netstat`:

1. Para exibir todas as conexões de rede e as portas em escuta:

```bash
netstat -a
```

2. Para visualizar apenas as conexões TCP em formato numérico:

```bash
netstat -tn
```

3. Para listar as portas em escuta junto com o PID dos processos:

```bash
netstat -lpn
```

## Tips
- Utilize o comando `netstat` em combinação com `grep` para filtrar resultados específicos. Por exemplo, para encontrar conexões relacionadas ao SSH, você pode usar:

```bash
netstat -tna | grep :22
```

- Lembre-se de que o `netstat` pode não estar instalado por padrão em algumas distribuições modernas do Linux. Você pode precisar instalar o pacote `net-tools` para ter acesso a esse comando.
- Para uma análise mais detalhada das conexões de rede, considere usar o `ss`, que é uma ferramenta mais moderna e eficiente que pode substituir o `netstat` em muitos casos.