# [리눅스] Bash htop 사용법

## Overview
O `htop` é uma ferramenta de monitoramento interativo de processos para sistemas Unix. Ele fornece uma visão em tempo real do uso da CPU, memória e outros recursos do sistema, permitindo que os usuários visualizem e gerenciem processos de maneira mais intuitiva em comparação com o comando `top`. A interface do `htop` é baseada em texto e permite navegação com as teclas de seta, facilitando a interação e a visualização das informações.

## Usage
A sintaxe básica do comando `htop` é bastante simples:

```bash
htop
```

Quando executado, o `htop` inicia uma interface gráfica no terminal. Além disso, existem algumas opções comuns que podem ser usadas ao iniciar o `htop`:

- `-d <delay>`: Define o atraso entre as atualizações em décimos de segundo. Por exemplo, `htop -d 10` atualiza a cada 1 segundo.
- `-p <pid>`: Permite que você visualize apenas o processo com o ID especificado. Exemplo: `htop -p 1234`.
- `--help`: Exibe a ajuda e as opções disponíveis.

## Examples
Aqui estão alguns exemplos práticos de como usar o `htop`:

1. **Iniciar o htop**:
   Para iniciar o `htop`, basta digitar o comando no terminal:

   ```bash
   htop
   ```

   Isso abrirá a interface do `htop`, onde você poderá ver todos os processos em execução, uso de CPU e memória.

2. **Visualizar um processo específico**:
   Se você deseja monitorar um processo específico, pode usar a opção `-p`. Por exemplo, para monitorar o processo com ID 1234:

   ```bash
   htop -p 1234
   ```

   Isso mostrará apenas as informações do processo com o ID 1234.

## Tips
- **Navegação**: Use as teclas de seta para navegar entre os processos. Você pode pressionar `F9` para matar um processo selecionado.
- **Filtragem**: Pressione `F3` para buscar um processo específico pelo nome, tornando mais fácil encontrar o que você está procurando.
- **Ordenação**: Você pode ordenar os processos por diferentes critérios pressionando as teclas de função, como `F6` para escolher a coluna de ordenação.
- **Personalização**: O `htop` permite que você personalize a visualização. Pressione `F2` para acessar o menu de configuração e ajustar as opções de exibição conforme suas necessidades.

O `htop` é uma ferramenta poderosa para monitorar e gerenciar processos em sistemas Unix, oferecendo uma interface amigável e recursos avançados para desenvolvedores e engenheiros.