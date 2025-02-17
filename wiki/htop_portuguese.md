# [Linux] Bash htop Uso: Monitorar processos em tempo real

## Overview
O comando `htop` é uma ferramenta interativa de monitoramento de processos que permite visualizar em tempo real o uso de recursos do sistema, como CPU, memória e processos em execução. É uma alternativa mais amigável e visual ao comando `top`, oferecendo uma interface mais intuitiva e opções de interação.

## Usage
A sintaxe básica do comando `htop` é a seguinte:

```bash
htop [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `htop`:

- `-h`, `--help`: Exibe a ajuda do comando.
- `-s`, `--sort`: Permite ordenar os processos por uma coluna específica (por exemplo, CPU ou memória).
- `-p`, `--pid`: Monitora um ou mais processos específicos, identificados pelos seus IDs.
- `-u`, `--user`: Filtra os processos para mostrar apenas aqueles pertencentes a um usuário específico.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `htop`:

1. **Executar htop**:
   ```bash
   htop
   ```

2. **Ordenar processos por uso de CPU**:
   ```bash
   htop -s PERCENT_CPU
   ```

3. **Filtrar processos de um usuário específico**:
   ```bash
   htop -u nome_do_usuario
   ```

4. **Monitorar um processo específico pelo PID**:
   ```bash
   htop -p 1234
   ```

## Tips
- Utilize as teclas de atalho dentro do `htop` para facilitar a navegação, como `F10` para sair e `F3` para buscar processos.
- Você pode usar as setas do teclado para navegar entre os processos e `F9` para matar um processo selecionado.
- Personalize a exibição de colunas pressionando `F2` e ajustando as configurações conforme suas necessidades.

Com essas informações, você está pronto para usar o `htop` e monitorar os processos do seu sistema de forma eficiente!