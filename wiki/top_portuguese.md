# [리눅스] Bash top 사용법

## Overview
O comando `top` é uma ferramenta de monitoramento de sistema em tempo real que exibe informações sobre os processos em execução no sistema. Ele fornece uma visão dinâmica do uso da CPU, memória e outras métricas importantes, permitindo que engenheiros e desenvolvedores identifiquem processos que consomem muitos recursos e monitorem o desempenho geral do sistema.

## Usage
A sintaxe básica do comando `top` é simples:

```bash
top [opções]
```

Algumas das opções mais comuns incluem:

- `-d <segundos>`: Define o intervalo de atualização em segundos. Por exemplo, `-d 2` atualiza a saída a cada 2 segundos.
- `-n <número>`: Especifica o número de iterações a serem exibidas antes de sair. Por exemplo, `-n 5` executa o `top` por 5 atualizações e depois termina.
- `-u <usuário>`: Filtra a exibição para mostrar apenas os processos pertencentes a um usuário específico.

## Examples
Aqui estão alguns exemplos práticos de como usar o comando `top`:

1. Para iniciar o `top` com a atualização padrão (a cada 3 segundos):

   ```bash
   top
   ```

2. Para executar o `top` com um intervalo de atualização de 2 segundos e limitar a 10 iterações:

   ```bash
   top -d 2 -n 10
   ```

3. Para visualizar apenas os processos de um usuário específico, por exemplo, "joao":

   ```bash
   top -u joao
   ```

## Tips
- Utilize a tecla `h` enquanto o `top` está em execução para acessar a ajuda interativa, que fornece uma lista de comandos e opções disponíveis.
- Para ordenar os processos por uso de CPU, pressione a tecla `P`. Para ordenar por uso de memória, pressione a tecla `M`.
- Você pode sair do `top` a qualquer momento pressionando a tecla `q`.
- Considere usar o comando `htop`, que é uma versão melhorada do `top`, com uma interface mais amigável e recursos adicionais, se estiver disponível no seu sistema.